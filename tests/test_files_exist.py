import os
import sys

# Define required files and associated grading points
REQUIRED_FILES = {
    "screenshot_1_installation_check.png": 15,
    "screenshot_2_jupyter_home.png": 15,
    "my_first_notebook.ipynb": 30,
    "screenshot_3_notebook_complete.png": 10,
}

def test_required_files():
    score = 0
    max_score = sum(REQUIRED_FILES.values())

    print("Checking required files...\n")

    for filename, points in REQUIRED_FILES.items():
        if os.path.isfile(filename):
            print(f"[✔] Found: {filename}")
            score += points
        else:
            print(f"[✘] Missing: {filename}")

    print(f"\n✅ Score for required files: {score} / {max_score}")
    return score, max_score


if __name__ == "__main__":
    score, max_score = test_required_files()

    # Exit code 0 if full score, 1 if anything missing
    sys.exit(0 if score == max_score else 1)

