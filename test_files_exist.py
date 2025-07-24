import os

def test_required_files():
    required_files = {
        "screenshot_1_installation_check.png": 15,
        "screenshot_2_jupyter_home.png": 15,
        "my_first_notebook.ipynb": 30,
        "screenshot_3_notebook_complete.png": 10,
    }

    score = 0
    for filename, points in required_files.items():
        if os.path.isfile(filename):
            print(f"[✔] Found: {filename}")
            score += points
        else:
            print(f"[✘] Missing: {filename}")
    return score
