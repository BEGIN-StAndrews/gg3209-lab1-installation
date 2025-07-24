import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def test_notebook_runs(notebook_filename="my_first_notebook.ipynb"):
    if not os.path.isfile(notebook_filename):
        print("[!] Notebook not found, skipping execution test.")
        return 0

    with open(notebook_filename, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=120, kernel_name='python3')
    try:
        ep.preprocess(nb, {'metadata': {'path': './'}})
        print("[✔] Notebook executed successfully.")
        return 20
    except Exception as e:
        print(f"[✘] Notebook execution failed: {e}")
        return 0
