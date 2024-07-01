# text_type_text = "text"
# text_type_bold = "bold"
# text_type_italic = "italic"
# text_type_code = "code"
# text_type_link = "link"
# text_type_image = "image"
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


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
    pass
