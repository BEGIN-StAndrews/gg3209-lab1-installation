import os
import sys

# Define required files and associated grading points
REQUIRED_FILES = {
    "screenshot_1_installation_check.png": 25,
    "screenshot_2_jupyter_home.png": 25,
    "screenshot_3_notebook_complete.png": 25,
}

def test_required_files():
    score = 0
    max_score = sum(REQUIRED_FILES.values())

    print("Checking required screenshot files...\n")

    for filename, points in REQUIRED_FILES.items():
        if os.path.isfile(filename):
            print(f"[✔] Found: {filename} (+{points} points)")
            score += points
        else:
            print(f"[✘] Missing: {filename} (0/{points} points)")

    print(f"\nFinal Score: {score}/{max_score}")
    print(f"Score assigned to: {score}")
    
    return score

if __name__ == "__main__":
    score = test_required_files()
    
    # Exit with score as return code (GitHub Actions can use this)
    # Exit 0 for success, non-zero for issues
    sys.exit(0 if score == sum(REQUIRED_FILES.values()) else 1)