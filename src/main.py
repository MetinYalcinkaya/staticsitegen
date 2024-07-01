from inline_markdown import (
    markdown_to_blocks,
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_links,
    split_nodes_images,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


def main():
    test_text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is a list item\n* This is another list item"
    print(markdown_to_blocks(test_text))


main()
