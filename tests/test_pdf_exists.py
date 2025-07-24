import os
import sys

def test_pdf_exists(pdf_name="my_first_notebook.pdf"):
    """Test if the required PDF file exists"""
    print("=== PDF Validation Test ===\n")
    print(f"Checking for PDF file: {pdf_name}")
    
    if os.path.isfile(pdf_name):
        print(f"[✔] PDF found: {pdf_name} (+25 points)")
        score = 25
    else:
        print(f"[✘] PDF missing: {pdf_name} (0/25 points)")
        score = 0
    
    print(f"\nFinal Score: {score}/25")
    print(f"Score assigned to: {score}")
    
    return score

if __name__ == "__main__":
    score = test_pdf_exists()
    
    # Exit 0 for success, 1 for failure
    sys.exit(0 if score == 25 else 1)