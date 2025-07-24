import os
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

NOTEBOOK_FILE = "my_first_notebook.ipynb"

VERIFICATION_STRINGS = [
    "datetime.datetime.now()",
    "platform.node()"
]

def test_notebook_exists():
    """Test if the notebook file exists"""
    print("1. Checking notebook existence...")
    
    if os.path.isfile(NOTEBOOK_FILE):
        print(f"[✔] Notebook found: {NOTEBOOK_FILE} (+10 points)")
        return 10
    else:
        print(f"[✘] Notebook not found: {NOTEBOOK_FILE} (0/10 points)")
        return 0

def test_notebook_runs():
    """Test if the notebook executes successfully"""
    print("\n2. Testing notebook execution...")
    
    if not os.path.isfile(NOTEBOOK_FILE):
        print(f"[✘] Cannot execute - notebook not found (0/30 points)")
        return 0

    try:
        with open(NOTEBOOK_FILE, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        # Execute notebook
        notebook_dir = os.path.abspath(os.path.join(NOTEBOOK_FILE, os.pardir))
        ep = ExecutePreprocessor(timeout=120, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': notebook_dir}})
        
        print("[✔] Notebook executed successfully (+30 points)")
        return 30
    except Exception as e:
        print(f"[✘] Notebook execution failed: {e} (15/30 points)")
        return 15

def check_verification_elements():
    """Check for anti-AI verification elements"""
    print("\n3. Checking for anti-AI verification elements...")

    if not os.path.isfile(NOTEBOOK_FILE):
        print(f"[✘] Cannot check - notebook not found (0/10 points)")
        return 0

    try:
        with open(NOTEBOOK_FILE, "r", encoding="utf-8") as f:
            content = f.read()

        found_count = 0
        for check in VERIFICATION_STRINGS:
            if check in content:
                print(f"[✔] Found: {check}")
                found_count += 1
            else:
                print(f"[✘] Missing: {check}")

        if found_count == len(VERIFICATION_STRINGS):
            print(f"[✔] All verification elements found (+10 points)")
            return 10
        elif found_count > 0:
            print(f"[◐] Some verification elements found (+5 points)")
            return 5
        else:
            print(f"[✘] No verification elements found (0/10 points)")
            return 0
            
    except Exception as e:
        print(f"[✘] Error reading notebook: {e} (0/10 points)")
        return 0

def main():
    print("=== Notebook Validation Tests ===\n")
    
    # Run all tests
    score1 = test_notebook_exists()
    score2 = test_notebook_runs()
    score3 = check_verification_elements()
    
    total_score = score1 + score2 + score3
    max_score = 50  # 10 + 30 + 10
    
    print(f"\n=== Final Results ===")
    print(f"Notebook exists: {score1}/10")
    print(f"Notebook executes: {score2}/30") 
    print(f"Anti-AI verification: {score3}/10")
    print(f"Total Score: {total_score}/{max_score}")
    print(f"Score assigned to: {total_score}")
    
    return total_score

if __name__ == "__main__":
    score = main()
    # Exit 0 for full score, 1 for partial/no score
    sys.exit(0 if score == 50 else 1)