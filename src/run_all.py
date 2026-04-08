"""runs the full pipeline end-to-end"""

import subprocess
import sys

def run_script(script_name, args=None):
    cmd = [sys.executable, f"src/{script_name}"]
    if args:
        cmd.extend(args)
    
    print(f"\n>>> Executing {script_name}...")
    result = subprocess.run(cmd, capture_output=False)
    
    if result.returncode != 0:
        print(f"Error: {script_name} failed with return code {result.returncode}")
        sys.exit(1)

def main():
    # 1. Clean data
    run_script("02_clean.py")
    
    # 2. Automated Grouping & Persona
    run_script("05_personas_auto.py")
    
    # 3. Generate Specifications
    run_script("06_spec_generate.py")
    
    # 4. Generate Tests
    run_script("07_tests_generate.py")
    
    # 5. Compute Metrics
    run_script("08_metrics.py", ["auto"])

    print("Automated Workflow Execution Complete!")

if __name__ == "__main__":
    main()