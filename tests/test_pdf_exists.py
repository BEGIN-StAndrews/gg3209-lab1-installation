import os

def test_pdf_exists(pdf_name="my_first_notebook.pdf"):
    if os.path.isfile(pdf_name):
        print(f"[✔] PDF found: {pdf_name}")
        return 10
    else:
        print(f"[✘] PDF missing: {pdf_name}")
        return 0

if __name__ == "__main__":
    test_pdf_exists()

