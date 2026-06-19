#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Word 文档批注工具 — 在 .docx 中插入真实的 Word 批注（Comments）。

用法：
    python add_docx_comments.py <输入.docx> <输出.docx> <批注清单.json>

批注清单.json 格式（列表）：
    [
        {
            "para_idx": 3,
            "comment": "这段AI味过重，建议改写",
            "author": "Reviewer"
        }
    ]

依赖：python-docx, lxml
"""
import json
import os
import sys
import zipfile
from datetime import datetime
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NSMAP = {'w': W}


def qn(local):
    return f'{{{W}}}{local}'


def get_max_comment_id(comments_root):
    max_id = 0
    for el in comments_root.iter():
        cid = el.get(qn('id'))
        if cid is not None:
            try:
                v = int(cid)
                if v > max_id:
                    max_id = v
            except (ValueError, TypeError):
                pass
    return max_id + 1


def make_comment_element(comment_id, author, date_str, comment_text):
    """Build a <w:comment> XML element."""
    comment = etree.Element(qn('comment'))
    comment.set(qn('id'), str(comment_id))
    comment.set(qn('author'), author)
    comment.set(qn('date'), date_str)

    p = etree.SubElement(comment, qn('p'))
    r = etree.SubElement(p, qn('r'))
    t = etree.SubElement(r, qn('t'))
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    t.text = comment_text

    return comment


def add_comments_to_docx(docx_path_in, docx_path_out, annotations):
    """
    Add Word comments to a .docx file.
    annotations: list of dict with keys: para_idx, comment, author (optional)
    """
    with zipfile.ZipFile(docx_path_in, 'r') as zin:
        zip_data = {name: zin.read(name) for name in zin.namelist()}

    # Parse document.xml
    doc_xml = etree.fromstring(zip_data['word/document.xml'])
    body = doc_xml.find(qn('body'))
    if body is None:
        raise ValueError('No body found in document.xml')

    paragraphs = body.findall(qn('p'))
    print(f"Document has {len(paragraphs)} paragraphs")

    # Handle comments.xml
    if 'word/comments.xml' in zip_data:
        comments_root = etree.fromstring(zip_data['word/comments.xml'])
    else:
        comments_root = etree.Element(qn('comments'))

    next_id = get_max_comment_id(comments_root)
    date_str = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    success_count = 0
    for ann in annotations:
        para_idx = ann['para_idx']
        comment_text = ann['comment']
        author = ann.get('author', 'Hermes Agent')

        if para_idx < 0 or para_idx >= len(paragraphs):
            print(f'[SKIP] para_idx {para_idx} out of range (0-{len(paragraphs) - 1})')
            continue

        para = paragraphs[para_idx]
        runs = para.findall(qn('r'))
        if not runs:
            print(f'[SKIP] para_idx {para_idx} has no runs')
            continue

        comment_id = next_id
        next_id += 1

        # 1. Add comment to comments.xml
        comment_el = make_comment_element(comment_id, author, date_str, comment_text)
        comments_root.append(comment_el)

        # 2. Insert comment markers into the paragraph XML
        # commentRangeStart as first child of para
        cs = etree.Element(qn('commentRangeStart'))
        cs.set(qn('id'), str(comment_id))
        para.insert(0, cs)

        # commentRangeEnd as last child of para
        ce = etree.Element(qn('commentRangeEnd'))
        ce.set(qn('id'), str(comment_id))
        para.append(ce)

        # commentReference in a new run at end of para
        ref_run = etree.SubElement(para, qn('r'))
        cr = etree.SubElement(ref_run, qn('commentReference'))
        cr.set(qn('id'), str(comment_id))

        print(f'[OK] Para {para_idx}: "{comment_text[:40]}..." (id={comment_id})')
        success_count += 1

    # Write back modified document.xml and comments.xml
    if success_count > 0:
        zip_data['word/document.xml'] = etree.tostring(
            doc_xml, xml_declaration=True, encoding='UTF-8', standalone=True
        )
        zip_data['word/comments.xml'] = etree.tostring(
            comments_root, xml_declaration=True, encoding='UTF-8', standalone=True
        )

        # Ensure content type for comments.xml exists
        ct_path = '[Content_Types].xml'
        if ct_path in zip_data:
            ct_xml = etree.fromstring(zip_data[ct_path])
            ct_ns = 'http://schemas.openxmlformats.org/package/2006/content-types'
            has_ct = any(
                child.get('PartName') == '/word/comments.xml'
                for child in ct_xml
                if child.tag == f'{{{ct_ns}}}Override'
            )
            if not has_ct:
                override = etree.SubElement(ct_xml, f'{{{ct_ns}}}Override')
                override.set('PartName', '/word/comments.xml')
                override.set('ContentType',
                             'application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml')
                zip_data[ct_path] = etree.tostring(
                    ct_xml, xml_declaration=True, encoding='UTF-8', standalone=True
                )

    # Write output docx
    with zipfile.ZipFile(docx_path_out, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name, data in zip_data.items():
            zout.writestr(name, data)

    print(f'\n{success_count} comments added → {docx_path_out}')
    return success_count


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)

    src, dst, ops_path = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(ops_path, 'r', encoding='utf-8') as f:
        annotations = json.load(f)

    add_comments_to_docx(src, dst, annotations)


if __name__ == '__main__':
    main()
