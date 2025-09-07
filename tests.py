from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

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
    # print(get_file_content(working_dir, "main.py"))
    # print(get_file_content(working_dir, "pkg/calculator.py"))
    # print(get_file_content(working_dir, "/bin/cat"))
    # print(file_content = get_file_content(working_dir, "pkg/does_not_exist.py"))
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    # print(run_python_file("calculator", "main.py"))
    # print(run_python_file("calculator", "main.py", ["3 + 5"]))
    # print(run_python_file("calculator", "tests.py"))
    # print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))

main()