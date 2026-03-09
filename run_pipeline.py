"""
run_pipeline.py

Runs the full automation pipeline.
"""

import subprocess


def run_script(script_name):

    print(f"Running {script_name}...")

    result = subprocess.run(["python", script_name])

    if result.returncode != 0:
        raise RuntimeError(f"{script_name} failed.")


def main():

    run_script("process_files.py")

    run_script("generate_summary.py")

    print("Automation pipeline completed successfully.")


if __name__ == "__main__":
    main()