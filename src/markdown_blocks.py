import re

from htmlnode import *
from inline_markdown import *
from textnode import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown):
    # Strips raw markdown to a list of 'blocks' split by \n\n
    # then strips whitespace from leading/trailing of each block
    # and removes any empty blocks
    blocks = []
    for block in markdown.split("\n\n"):
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks


def block_to_block_type(markdown):
    # Takes a block of markdown and returns type of markdown it is
    if re.findall(r"^(#+\s)", markdown, re.MULTILINE) != []:
        return block_type_heading
    if re.findall(r"^```$|^```(?=\s)|(?<=\s)```$", markdown, re.MULTILINE) != []:
        return block_type_code
    if re.findall(r"^>", markdown, re.MULTILINE) != []:
        return block_type_quote
    if re.findall(r"^(\*|\-)", markdown, re.MULTILINE) != []:
        return block_type_ulist
    if re.findall(r"^([0-9]\. )", markdown, re.MULTILINE) != []:
        return block_type_olist
    return block_type_paragraph


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError(f"Invalid block type: {block_type}")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def text_to_child(text):
    text_nodes = text_to_textnodes(text)
    child = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        child.append(html_node)
    return child


def paragraph_to_html_node(block):
    split_block = block.split("\n")
    paragraph = " ".join(split_block)
    child = text_to_child(paragraph)
    return ParentNode("p", child)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_child(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code format, missing ``` start and/or end")
    text = block[3:-4]
    children = text_to_child(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_child(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_child(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid code block, missing > char")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_child(content)
    return ParentNode("blockquote", children)
