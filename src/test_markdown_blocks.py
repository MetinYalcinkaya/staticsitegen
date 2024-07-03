import unittest

from markdown_blocks import *


class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks_me(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is a list item\n* This is another list item"
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is a list item\n* This is another list item",
        ]

        new_text = markdown_to_blocks(text)

        self.assertListEqual(new_text, expected)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italics*
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italics*\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]
        self.assertListEqual(blocks, expected)

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph






This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]
        self.assertListEqual(blocks, expected)

    # Boot.dev did it all in one, smart
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    # these were my tests
    def test_block_to_block_type_paragraph(self):
        block = "This is a **bolded** paragraph"
        block_type = block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        expected = block_type_heading
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_heading2(self):
        block = "#### This is a bigger heading"
        block_type = block_to_block_type(block)
        expected = block_type_heading
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_code(self):
        block = """
``` python
def main():
    print("hello world")
```
"""
        block_type = block_to_block_type(block)
        expected = block_type_code
        self.assertEqual(block_type, expected)

    def text_block_to_block_type_code2(self):
        block = """
```
def func(foo):
    return foo*2
```
"""
        block_type = block_to_block_type(block)
        expected = block_type_code
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_ulist(self):
        block = """
* This is a list
* with items
"""
        block_type = block_to_block_type(block)
        expected = block_type_ulist
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_ulist_outlier(self):
        block = """
This is a list **with bolded**
To try trick 
the **system**
"""
        block_type = block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_olist(self):
        block = """
1. One
2. Two
3. Three
4. Four
"""
        block_type = block_to_block_type(block)
        expected = block_type_olist
        self.assertEqual(block_type, expected)

    def test_block_to_block_type_olist_outlier(self):
        block = """
Testing 1. if
inline 3. numbers trigger
this 4. reg expr
"""
        block_type = block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(block_type, expected)

    def test_md_to_html_paragraph(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        expected = (
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>"
        )
        self.assertEqual(html, expected)

    def test_md_to_html_paragraphs(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        self.assertEqual(html, expected)

    def test_md_to_html_lists(self):
        markdown = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        expected = "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>"
        self.assertEqual(html, expected)

    def test_md_to_html_headings(self):
        markdown = """
# This is an H1

This is a paragraph text

## This is an H2
"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        expected = "<div><h1>This is an H1</h1><p>This is a paragraph text</p><h2>This is an H2</h2></div>"
        self.assertEqual(html, expected)

    def test_md_to_html_quote(self):
        markdown = """
> This is a
> blockquote block

This is a paragraph
"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        expected = "<div><blockquote>This is a blockquote block</blockquote><p>This is a paragraph</p></div>"
        self.assertEqual(html, expected)
