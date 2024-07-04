import os

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    split_markdown = markdown.split("\n")
    for line in split_markdown:
        if line.startswith("#"):
            return line.lstrip("# ")
    raise Exception("Could not find #/heading 1")


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} > {dest_path}")
    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    title = extract_title(markdown)

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown)
    html = node.to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    to_file = open(dest_path, "w")
    to_file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # if not os.path.exists(dest_dir_path):
    #     os.mkdir(dest_dir_path)

    for file in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if file.endswith(".md"):
            dest_path = os.path.join(dest_dir_path, file.rstrip(".md") + ".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
