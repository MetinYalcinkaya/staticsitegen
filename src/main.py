from inline_markdown import *
from textnode import *
from markdown_blocks import *
import re


def main():
    # test_text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is a list item\n* This is another list item"
    # print(markdown_to_blocks(test_text))
    # print(block_to_block_type(test_text))
    text = """
        ``` python
        def main()
            pass
        ```
        """
    print(block_to_block_type(text))
    # exp = r"^(#+\s)"
    # print(re.findall(exp, text, re.MULTILINE))


main()
