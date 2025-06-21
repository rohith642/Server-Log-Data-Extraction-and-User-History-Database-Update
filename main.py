# main.py (MongoDB step skipped)
from src.extractor import extract_email_date_pairs
from src.sqlite_uploader import upload_to_sqlite
from src.analysis import run_queries
import os

def main():
    log_file = "data/mbox.txt"

    print(f"Checking if log file exists at: {log_file}")
    print("Exists:", os.path.exists(log_file))

    if not os.path.exists(log_file):
        print("❌ Log file not found. Exiting.")
        return

    with open(log_file, 'r') as f:
        print("📄 First 5 lines of mbox.txt:")
        for _ in range(5):
            print(f.readline().strip())

    # Task 1 & 2: Extract and Transform
    cleaned_data = extract_email_date_pairs(log_file)

    # ⏩ SKIPPING MongoDB — Direct SQLite upload
    upload_to_sqlite(cleaned_data)

    # Task 5: Analysis
    run_queries()

if __name__ == "__main__":
    main()

