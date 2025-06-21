# Server-Log-Data-Extraction-and-User-History-Database-Update
# Server Log Data Extraction and User History Database Update

This Python project extracts email and timestamp information from a log file (`mbox.txt`), stores it in a local SQLite database, and performs basic analysis.

## ✅ Features

- Extracts email addresses and timestamps from log lines starting with `From `
- Cleans and transforms raw date data to a uniform format
- Stores structured data into a local SQLite database
- Analyzes user history with simple SQL queries
- MongoDB upload capability (currently disabled due to SSL issues)

---

## 🗂 Project Structure

Server Log Data Extraction and User History Database Update/
│
├── main.py # Entry point (MongoDB skipped)
├── data/
│ └── mbox.txt # Log file (input)
├── src/
│ ├── init.py
│ ├── extractor.py # Extracts and parses email/date from logs
│ ├── sqlite_uploader.py # Uploads data to SQLite DB
│ ├── mongodb_uploader.py # (Optional) Uploads data to MongoDB
│ └── analysis.py # Runs SQL queries for analysis
└── user_history.db # SQLite database (auto-created)

yaml
Copy
Edit

---

## ▶️ How to Run

### 1. Install dependencies

Only built-in modules + `pymongo` (optional):

```bash
pip install pymongo
2. Run the program
bash
Copy
Edit
python main.py
📊 Output
✅ Extracted records are stored in user_history.db

✅ Analysis results are printed in the terminal:

Unique email addresses

Email count per day

First & last activity per user

Total emails per domain

🔧 Optional: Enable MongoDB Upload
To enable uploading to MongoDB Atlas:

Ensure your system supports TLS/SSL properly.

Update main.py to include:

python
Copy
Edit
from src.mongodb_uploader import upload_to_mongodb
from pymongo import MongoClient
Add MongoDB URI and switch the logic accordingly.

