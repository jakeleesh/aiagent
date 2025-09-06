from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    working_dir = "calculator"
    # root_contents = get_files_info(working_dir)
    # print(root_contents)
    # root_contents = get_files_info(working_dir, "pkg")
    # print(root_contents)
    # root_contents = get_files_info(working_dir, "/bin")
    # print(root_contents)
    # root_contents = get_files_info(working_dir, "../")
    # print(root_contents)
    # file_content = get_file_content(working_dir, "lorem.txt")
    # print(file_content)
    file_content = get_file_content(working_dir, "main.py")
    print(file_content)
    file_content = get_file_content(working_dir, "pkg/calculator.py")
    print(file_content)
    file_content = get_file_content(working_dir, "/bin/cat")
    print(file_content)
    file_content = get_file_content(working_dir, "pkg/does_not_exist.py")
    print(file_content)

main()