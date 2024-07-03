import os
import shutil

from markdown_blocks import *


def extract_title(markdown):
    split_markdown = markdown.split("\n")
    for line in split_markdown:
        if line.startswith("#"):
            return line.lstrip("# ")
    raise Exception("Could not find #/heading 1")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} > {dest_path} using {template_path}")
    markdown = open(from_path).read()
    title = extract_title(markdown)
    template = open(template_path).read()
    content = markdown_to_html_node(markdown).to_html()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    # if not os.path.exists(dest_path):
    #     print(f"Creating dirs > {dest_path}")
    open(dest_path, "w").write(template)
