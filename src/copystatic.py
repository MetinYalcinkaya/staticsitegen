import os
import shutil

# Constants for /static/ and /public/ folders
STATIC_DIR = os.path.abspath(os.path.join(__file__, "../..", "static"))
PUBLIC_DIR = os.path.abspath(os.path.join(__file__, "../..", "public"))


def copy_static(static_path=STATIC_DIR, public_path=PUBLIC_DIR):
    if not os.path.exists(public_path):
        print("Creating public directory...")
        os.mkdir(public_path)

    # Can refactor this down heavily, I'm basically checking if it's a file twice,
    # but I can just check if it's a file once, and then call recursive func
    # and instead of using creating the directory inside this section, create it
    # at the start of the function
    dir_contents = os.listdir(static_path)
    for dir_content in dir_contents:
        if os.path.isdir(os.path.join(static_path, dir_content)):
            if os.path.exists(os.path.join(public_path, dir_content)):
                print(
                    f"Path {os.path.join(public_path, dir_content)} already exists: {os.path.join(public_path, dir_content)}"
                )
            else:
                print(
                    f"Creating dir: {dir_content} from {static_path} to {os.path.join(public_path, dir_content)}"
                )
                os.mkdir(os.path.join(public_path, dir_content))
                # Start recursion until it hits a file rather than a folder
                copy_static(
                    os.path.join(static_path, dir_content),
                    os.path.join(public_path, dir_content),
                )
        elif os.path.isfile(os.path.join(static_path, dir_content)):
            if os.path.isfile(os.path.join(public_path, dir_content)):
                print(
                    f"File {dir_content} already exists at: {os.path.join(public_path, dir_content)}"
                )
            else:
                print(
                    f"Copying {dir_content} from {static_path} to {os.path.join(public_path, dir_content)}"
                )
                shutil.copy(
                    os.path.join(static_path, dir_content),
                    os.path.join(public_path, dir_content),
                )


# Solution
def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)
