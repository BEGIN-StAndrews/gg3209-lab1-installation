import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Grading config
GRADE = 0
MAX_GRADE = 100

# Define required files and points
required_files = {
    "screenshot_1_installation_check.png": 15,
    "screenshot_2_jupyter_home.png": 15,
    "my_first_notebook.ipynb": 30,
    "screenshot_3_notebook_complete.png": 10,
    "my_first_notebook.pdf": 10
}

notebook_filename = "my_first_notebook.ipynb"
notebook_execution_points = 20


def test_required_files_exist():
    global GRADE
    for filename, points in required_files.items():
        if os.path.isfile(filename):
            print(f"[✔] Found: {filename}")
            GRADE += points
        else:
            print(f"[✘] Missing: {filename}")


def test_notebook_runs():
    global GRADE
    if not os.path.isfile(notebook_filename):
        print("[!] Notebook not found, skipping execution test.")
        return

    with open(notebook_filename, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=120, kernel_name='python3')
    try:
        ep.preprocess(nb, {'metadata': {'path': './'}})
        print("[✔] Notebook executed successfully without errors.")
        GRADE += notebook_execution_points
    except Exception as e:
        print(f"[✘] Notebook execution failed: {e}")


if __name__ == "__main__":
    print("Running assignment autograder...\n")
    test_required_files_exist()
    test_notebook_runs()
    print(f"\nFinal Grade: {GRADE} / {MAX_GRADE}")
