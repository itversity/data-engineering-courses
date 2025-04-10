---
title: "Lecture 4: Rename and Organize Uploaded Files"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Rename and Organize Uploaded Files

> Automatically clean and structure data lake file ingestion in GCS using Google Cloud Functions

---

## 🎯 What You’ll Learn

✅ Rename files on upload using a timestamp  
✅ Organize files in structured date-based folders  
✅ Use `google-cloud-storage` with `requirements.txt`  
✅ Deploy and test the function  
✅ Clean up GCP resources

---

## 🧭 Steps We'll Follow

1. Define renaming logic  
2. Write the function  
3. Add `requirements.txt`  
4. Create a new bucket  
5. Deploy Cloud Function  
6. Upload and test  
7. View logs  
8. Clean up

---

## Why Rename and Organize Files?

- Prevent name collisions  
- Enable partitioned folder structure  
- Prepare for downstream ETL  
- Add clarity to data lake design

---

## Folder Structure

Create a new folder:

```bash
mkdir gcf-rename-organize
cd gcf-rename-organize
```

---

## main.py – Cloud Function

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

## Step 2: Deploy the Cloud Function

```bash
gcloud functions deploy rename_and_organize \
  --runtime python311 \
  --trigger-resource $BUCKET_NAME \
  --trigger-event google.storage.object.finalize \
  --entry-point rename_and_organize \
  --source=. \
  --region us-central1
```

✅ Make sure `--source=.` is included to deploy with local `requirements.txt`

---

## Step 3: Upload and Trigger

```bash
echo "data,123" > orders.csv
gsutil cp orders.csv gs://$BUCKET_NAME/
```

---

## Step 4: Verify File Structure

```bash
gsutil ls -r gs://$BUCKET_NAME/structured/
```

✅ You should see:

```
structured/YYYY-MM-DD/orders_YYYYMMDD.csv
```

---

## Step 5: View Logs

```bash
gcloud functions logs read rename_and_organize --region us-central1
```

✅ Look for:

```
Moved file: orders.csv → structured/2025-04-08/orders_20250408.csv
```

---

## Step 6: Clean Up

```bash
gcloud functions delete rename_and_organize --region us-central1
gsutil rm -r gs://$BUCKET_NAME/
```

✅ Always clean up after testing

---

## ✅ Summary

- You renamed and structured files on upload  
- Used file metadata (`name`, `timeCreated`)  
- Used `google-cloud-storage` via requirements.txt  
- Set up a clean, automation-ready workflow

👉 Next: Validate uploaded files for naming and type
