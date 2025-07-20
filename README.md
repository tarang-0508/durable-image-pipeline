
# Durable Image Metadata Processing Pipeline

📁 **Course:** CST8917 – Serverless Computing  
🧠 **Assignment:** Durable Workflow for Image Metadata Processing  
📅 **Due Date:** July 19, 2025  
👨‍💻 **Author:** Tarang Savaj ([tarang-0508](https://github.com/tarang-0508))

---

## 📌 Overview

This project implements a **serverless image metadata processing pipeline** using **Azure Durable Functions** in Python. The solution automatically triggers when an image is uploaded to Azure Blob Storage, extracts its metadata (size, dimensions, format), and stores it in an **Azure SQL Database** using output bindings.

---

## 📂 Architecture

```text
         +-------------------------+
         |  Blob Storage Upload    |
         | (.jpg/.png/.gif files)  |
         +-----------+-------------+
                     |
                     v
         +-------------------------+
         |   BlobTriggerFunction   |
         | Starts the Orchestrator |
         +-----------+-------------+
                     |
                     v
         +-------------------------+
         |   OrchestratorFunction  |
         | Calls activity functions|
         +-----------+-------------+
                     |
     +---------------+--------------------+
     |                                    |
     v                                    v
+--------------+                  +------------------+
| ExtractMetadata |              |   StoreMetadata   |
| (Reads image &  |              |  (Writes metadata |
| extracts details)|             |   to SQL Table)   |
+----------------+               +------------------+
```

---

## 🛠️ Technologies Used

- Azure Durable Functions (Python)
- Azure Blob Storage
- Azure SQL Database
- Azurite for local blob testing
- VS Code + Azure Functions Core Tools
- Python 3.10

---

## 📦 Folder Structure

```bash
durable-image-pipeline/
│
├── BlobTriggerFunction/         # Triggers workflow on image upload
│   └── __init__.py
│   └── function.json
│
├── OrchestratorFunction/        # Coordinates activity functions
│   └── __init__.py
│   └── function.json
│
├── ExtractMetadata/             # Extracts image metadata
│   └── __init__.py
│   └── function.json
│
├── StoreMetadata/               # Stores metadata in SQL DB
│   └── __init__.py
│   └── function.json
│
├── host.json
├── requirements.txt
├── local.settings.json (excluded)
└── README.md
```

---

## 🧪 How to Run Locally

1. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Azurite for local storage**
   ```bash
   npm install -g azurite
   azurite
   ```

4. **Start Azure Functions locally**
   ```bash
   func start
   ```

5. **Upload a test image**  
   Upload `.jpg`, `.png`, or `.gif` image to the `images-input` container using Azure Storage Explorer.

6. **Check logs and SQL database**  
   Confirm that metadata was extracted and stored in your Azure SQL table.

---

## 🧾 SQL Table Schema

```sql
CREATE TABLE ImageMetadata (
    file_name NVARCHAR(255),
    file_size_kb INT,
    width INT,
    height INT,
    format NVARCHAR(50)
);
```

---

## 🔐 Sample `local.settings.json` (DO NOT commit this)

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "<your-blob-connection-string>",
    "SqlConnectionString": "<your-sql-connection-string>",
    "FUNCTIONS_WORKER_RUNTIME": "python"
  }
}
```

---

## 📽️ Demo Video

🔗 YouTube Demo Link Here  
_(Replace with your real YouTube demo before submission)_

---

