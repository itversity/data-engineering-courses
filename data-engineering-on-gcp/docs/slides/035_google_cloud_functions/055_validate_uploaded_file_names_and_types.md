---
title: "Lecture 5: Validate Uploaded File Names and Types"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Validate Uploaded File Names and Types

> Automatically quarantine invalid files using Google Cloud Functions

---

## 🎯 What You’ll Learn

✅ Validate files based on name pattern and extension  
✅ Move invalid files to `invalid/` folder  
✅ Use regex and string logic in Python  
✅ Deploy, test, and clean up a validation Cloud Function

---

## 🧭 Steps We'll Follow

1. Define validation rules  
2. Write the function  
3. Create `requirements.txt`  
4. Create a test bucket  
5. Deploy the function  
6. Upload and validate files  
7. View results and logs  
8. Clean up

---

## Why Validate Files?

- Prevent garbage files from polluting data lakes  
- Enforce naming and format standards  
- Build robust data ingestion pipelines

---

## Validation Rules

✅ Must be a `.csv` file  
✅ Must match `^sales_\d{8}\.csv$`  
❌ If not valid, move to `invalid/` folder  
❌ Skip reprocessing files already in `invalid/`

---

## Folder Setup

```bash
mkdir gcf-validate-files
cd gcf-validate-files
```

---

## main.py

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

## requirements.txt

```txt
google-cloud-storage
```

---

## Step 1: Create a GCS Bucket

```bash
BUCKET_NAME=gcf-validate-bucket-$(date +%s)
gsutil mb -l us-central1 gs://$BUCKET_NAME/
```

---

## Step 2: Deploy the Function

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

## Step 3: Upload Test Files

### ✅ Valid:

```bash
echo "id,amount" > sales_20250408.csv
gsutil cp sales_20250408.csv gs://$BUCKET_NAME/
```

### ❌ Invalid Extension:

```bash
echo "bad format" > wrong.txt
gsutil cp wrong.txt gs://$BUCKET_NAME/
```

### ❌ Invalid Pattern:

```bash
echo "bad pattern" > report.csv
gsutil cp report.csv gs://$BUCKET_NAME/
```

---

## Step 4: Verify Results

```bash
gsutil ls gs://$BUCKET_NAME/invalid/
```

✅ Should show: `wrong.txt`, `report.csv`

---

## Step 5: View Logs

```bash
gcloud functions logs read validate_file --region us-central1
```

✅ Look for:

```
🚫 File is invalid: wrong.txt. Reason: Invalid extension
Moved to: invalid/wrong.txt
```

---

## Step 6: Clean Up

```bash
gcloud functions delete validate_file --region us-central1
gsutil rm -r gs://$BUCKET_NAME/
```

✅ Always clean up after testing

---

## ✅ Summary

- You validated files using extension + regex  
- Invalid files are quarantined  
- Logs explain file rejections  
- You now have a basic quality control step in your data lake

👉 Next: Log metadata about each upload for auditing
