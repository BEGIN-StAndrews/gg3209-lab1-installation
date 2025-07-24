import os
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

NOTEBOOK_FILE = os.path.join(".", "my_first_notebook.ipynb")

VERIFICATION_STRINGS = [
    "datetime.datetime.now()",
    "platform.node()"
]

def test_notebook_runs():
    print("Executing notebook...\n")
    
    if not os.path.isfile(NOTEBOOK_FILE):
        print(f"[✘] Notebook not found at: {NOTEBOOK_FILE}")
        print("Score assigned to: 0")
        return 0

    with open(NOTEBOOK_FILE, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    # Make sure execution happens relative to the notebook’s location
    notebook_dir = os.path.abspath(os.path.join(NOTEBOOK_FILE, os.pardir))

    ep = ExecutePreprocessor(timeout=120, kernel_name='python3')
    try:
        ep.preprocess(nb, {'metadata': {'path': notebook_dir}})
        print("[✔] Notebook executed successfully.")
        print("Score assigned to: 20")
        return 20
    except Exception as e:
        print(f"[✘] Notebook execution failed: {e}")
        print("Score assigned to: 10")
        return 10


def check_verification_elements():
    print("Checking for anti-AI verification elements...")

    if not os.path.isfile(NOTEBOOK_FILE):
        print(f"[✘] Notebook not found at: {NOTEBOOK_FILE}")
        print("Score assigned to: 0")
        return 0

    with open(NOTEBOOK_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    all_found = True
    for check in VERIFICATION_STRINGS:
        if check in content:
            print(f"[✔] Found: {check}")
            return 20
        else:
            print(f"[✘] Missing: {check}")
            all_found = False
            return 5

    print(f"Score assigned to: {20 if all_found else 5}")


if __name__ == "__main__":
    test_notebook_runs()
    check_verification_elements()
