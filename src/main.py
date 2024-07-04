import os
import re
import shutil

from copystatic import copy_files_recursive, copy_static
from generatecontent import *
from inline_markdown import *
from markdown_blocks import *
from textnode import *

# Constants for /static/ and /public/ folders
STATIC_DIR = os.path.abspath(os.path.join(__file__, "../..", "static"))
PUBLIC_DIR = os.path.abspath(os.path.join(__file__, "../..", "public"))

# Solution vars
dir_path_static = "./static"
dir_path_public = "./public"

dir_path_markdown = "./content"
dir_path_template = "./template.html"
dir_path_dest = "./public"


def main():
    # markdown = "./content/index.md"
    # print(extract_title(open(markdown, "r").read()))
    # generate_page(dir_path_markdown, dir_path_template, dir_path_dest)
    generate_pages_recursive(dir_path_markdown, dir_path_template, dir_path_dest)


def main2():
    print("Deleting public directory...")
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
    print("Copying static files to public directory..")
    copy_static()

    # Solution main
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


main()
