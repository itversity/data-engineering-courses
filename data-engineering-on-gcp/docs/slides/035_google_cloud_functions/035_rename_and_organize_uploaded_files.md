---
title: "Lecture 3: Rename and Organize Uploaded Files"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Rename and Organize Uploaded Files

> Automatically clean and structure your data lake on file upload

---

## 🎯 What You’ll Learn

✅ Rename files with a timestamp suffix  
✅ Organize files into date-based folders  
✅ Use `google-cloud-storage` for file manipulation  
✅ Deploy and test a real automation use case

---

## Use Case Overview

We want to transform:

```
orders.csv
```

Into:

```
structured/YYYY-MM-DD/orders_YYYYMMDD.csv
```

Using the upload timestamp from the GCS `event`.

---

## Folder Setup

```bash
mkdir gcf-rename-organize
cd gcf-rename-organize
```

---

## main.py

```python
from google.cloud import storage
from datetime import datetime

def rename_and_organize(event, context):
    bucket_name = event['bucket']
    original_file_name = event['name']

    if original_file_name.startswith('structured/'):
        print(f"Skipping already organized file: {original_file_name}")
        return

    filename = original_file_name.split('/')[-1]
    if '.' not in filename:
        print(f"Skipping file without extension: {filename}")
        return

    base_name, ext = filename.rsplit('.', 1)
    created_date = event.get('timeCreated') or datetime.utcnow().isoformat()

    date_obj = datetime.strptime(created_date[:10], "%Y-%m-%d")
    today_str = date_obj.strftime('%Y-%m-%d')
    date_suffix = date_obj.strftime('%Y%m%d')

    new_filename = f"{base_name}_{date_suffix}.{ext}"
    destination_path = f"structured/{today_str}/{new_filename}"

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    source_blob = bucket.blob(original_file_name)
    destination_blob = bucket.blob(destination_path)

    bucket.copy_blob(source_blob, bucket, destination_blob.name)
    source_blob.delete()

    print(f"Moved file: {original_file_name} → {destination_path}")
```

---

## requirements.txt

```txt
google-cloud-storage
```

---

## Step 1: Create a Unique Bucket

```bash
BUCKET_NAME=gcf-rename-bucket-$(date +%s)
gsutil mb -l us-central1 gs://$BUCKET_NAME/
```

---

## Step 2: Deploy the Function

```bash
gcloud functions deploy rename_and_organize \
  --runtime python311 \
  --trigger-resource $BUCKET_NAME \
  --trigger-event google.storage.object.finalize \
  --entry-point rename_and_organize \
  --source=. \
  --region us-central1
```

---

## Step 3: Upload a Test File

```bash
echo "order_id,amount" > orders.csv
gsutil cp orders.csv gs://$BUCKET_NAME/
```

---

## Step 4: Verify the Outcome

```bash
gsutil ls -r gs://$BUCKET_NAME/structured/
```

✅ You should see the file renamed and moved into a structured path

---

## Step 5: View Logs

```bash
gcloud functions logs read rename_and_organize --region us-central1
```

✅ Look for:
```
Moved file: orders.csv → structured/YYYY-MM-DD/orders_YYYYMMDD.csv
```

---

## Step 6: Clean Up

```bash
gcloud functions delete rename_and_organize --region us-central1
gsutil rm -r gs://$BUCKET_NAME/
```

---

## ✅ Summary

- You renamed and organized uploaded files using timestamps  
- Used metadata from the event object  
- Employed GCS SDK for copying and deleting objects  
- Set the foundation for file validation and logging

👉 Next: Validate file names and log metadata to Cloud Logging
