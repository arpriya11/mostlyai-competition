import subprocess

def run_evaluation(original_path, synthetic_path, label):
    print(f"\n🚀 Evaluating {label} Dataset:")
    try:
        result = subprocess.run([
            "python", "-m", "mostlyai_qa",
            "--original", original_path,
            "--synthetic", synthetic_path
        ], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error evaluating {label}:")
        print(e.stderr)

if __name__ == "__main__":
    run_evaluation("data/flat-training.csv", "data/your-flat-submission01.csv", "FLAT")
    run_evaluation("data/sequential-training.csv", "data/your-sequential-submission01.csv", "SEQUENTIAL")
