---
title: "Lecture 4: Validate and Log File Uploads"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Validate and Log File Uploads

> Enforce standards and create audit trails for uploaded data

---

## 🎯 What You’ll Learn

✅ Validate file names and types using metadata  
✅ Quarantine invalid files to an `invalid/` folder  
✅ Log upload details to Cloud Logging  
✅ Deploy and test multiple automation functions

---

## Use Case 1: File Validation

**Valid if:**
- File ends with `.csv`
- Filename matches `^sales_\d{8}\.csv$`

If not valid:
- Move file to `invalid/` folder  
- Print reason to log

---

## Folder Setup

```bash
mkdir gcf-validate-log
cd gcf-validate-log
```

---

## main.py (Validation Function)

```python
import re
from google.cloud import storage

def validate_file(event, context):
    bucket_name = event['bucket']
    file_name = event['name']

    if file_name.startswith("invalid/"):
        print(f"Skipping already moved file: {file_name}")
        return

    if not file_name.endswith('.csv'):
        reason = "Invalid extension"
    elif not re.match(r'^sales_\d{8}\.csv$', file_name.split('/')[-1]):
        reason = "Invalid filename format"
    else:
        print(f"✅ File is valid: {file_name}")
        return

    print(f"🚫 File is invalid: {file_name}. Reason: {reason}")

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    source_blob = bucket.blob(file_name)
    destination_blob = bucket.blob(f"invalid/{file_name.split('/')[-1]}")

    bucket.copy_blob(source_blob, bucket, destination_blob.name)
    source_blob.delete()

    print(f"Moved to: invalid/{file_name.split('/')[-1]}")
```

---

## Use Case 2: Log Upload Events

```python
def log_file_metadata(event, context):
    print("📄 File Uploaded:")
    print(f"📁 Name       : {event.get('name')}")
    print(f"🪣 Bucket     : {event.get('bucket')}")
    print(f"📦 Size       : {event.get('size')} bytes")
    print(f"📄 Type       : {event.get('contentType')}")
    print(f"⏱️ Created At : {event.get('timeCreated')}")
```

---

## requirements.txt

```txt
google-cloud-storage
```

---

## Step 1: Create a GCS Bucket

```bash
BUCKET_NAME=gcf-validate-log-bucket-$(date +%s)
gsutil mb -l us-central1 gs://$BUCKET_NAME/
```

---

## Step 2: Deploy Validation Function

```bash
gcloud functions deploy validate_file \
  --runtime python311 \
  --trigger-resource $BUCKET_NAME \
  --trigger-event google.storage.object.finalize \
  --entry-point validate_file \
  --source=. \
  --region us-central1
```

---

## Step 3: Deploy Logging Function

```bash
gcloud functions deploy log_file_metadata \
  --runtime python311 \
  --trigger-resource $BUCKET_NAME \
  --trigger-event google.storage.object.finalize \
  --entry-point log_file_metadata \
  --source=. \
  --region us-central1
```

---

## Step 4: Upload Files for Testing

### ✅ Valid file

```bash
echo "id,amount" > sales_20250410.csv
gsutil cp sales_20250410.csv gs://$BUCKET_NAME/
```

### ❌ Invalid files

```bash
echo "oops" > wrong.txt
gsutil cp wrong.txt gs://$BUCKET_NAME/

echo "no date" > report.csv
gsutil cp report.csv gs://$BUCKET_NAME/
```

---

## Step 5: Check Invalid Folder

```bash
gsutil ls gs://$BUCKET_NAME/invalid/
```

✅ Should contain `wrong.txt` and `report.csv` only

---

## Step 6: View Logs

```bash
gcloud functions logs read validate_file --region us-central1
gcloud functions logs read log_file_metadata --region us-central1
```

✅ Logs will show reason for validation failures and full file metadata

---

## Step 7: Clean Up

```bash
gcloud functions delete validate_file --region us-central1
gcloud functions delete log_file_metadata --region us-central1
gsutil rm -r gs://$BUCKET_NAME/
```

---

## ✅ Summary

- You validated file names and extensions  
- Quarantined invalid files to `invalid/` folder  
- Logged upload metadata to Cloud Logging  
- Reinforced secure and observable ingestion patterns

👉 Next: Wrap up with packaging, permissions, and deployment best practices
