---
title: "Lecture 1: Introduction and Setup"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Introduction and Setup

> Kickstart your Cloud Functions journey with a real deployment

---

## 🎯 What You’ll Learn

✅ What Cloud Functions are and why they matter  
✅ How to trigger functions with GCS events  
✅ Deploy your first Cloud Function  
✅ View logs and validate functionality  
✅ Clean up GCP resources

---

## What Are Google Cloud Functions?

- Serverless, event-driven compute  
- No infrastructure to manage  
- Triggered by events (e.g., file uploads)

```text
GCS → Cloud Function → BigQuery / Dataflow
```

---

## Why Use Cloud Functions?

- Automate ingestion, validation, transformation  
- Integrate seamlessly with GCS, BigQuery, Pub/Sub  
- Ideal for lightweight, stateless tasks

---

## Common Use Cases

- Rename or organize uploaded files  
- Validate file content or naming  
- Trigger Dataflow or BigQuery workflows  
- Log metadata for auditing

---

## Step 1: Enable Required APIs

```bash
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable storage.googleapis.com
```

✅ Run once per GCP project

---

## Step 2: Create a GCS Bucket

```bash
BUCKET_NAME=gcf-hello-bucket-$(date +%s)
gsutil mb -l us-central1 gs://$BUCKET_NAME/
```

---

## Step 3: Write a Basic Cloud Function

```bash
mkdir gcf-hello
cd gcf-hello
nano main.py
```

Paste the code:

```python
def hello_gcs(event, context):
    file = event
    print(f"📁 File uploaded: {file['name']}")
    print(f"🪣 Bucket: {file['bucket']}")
```

✅ Save: `Ctrl+O`, `Enter`, `Ctrl+X`

---

## Step 4: Deploy the Function

```bash
gcloud functions deploy hello_gcs \
  --runtime python311 \
  --trigger-resource $BUCKET_NAME \
  --trigger-event google.storage.object.finalize \
  --entry-point hello_gcs \
  --region us-central1
```

---

## Step 5: Upload a File to Trigger It

```bash
echo "hello world" > testfile.txt
gsutil cp testfile.txt gs://$BUCKET_NAME/
```

---

## Step 6: View Logs (CLI)

```bash
gcloud functions logs read hello_gcs --region us-central1
```

✅ Output should include:

```
📁 File uploaded: testfile.txt
🪣 Bucket: gcf-hello-bucket-...
```

---

## Step 6: View Logs (Console)

1. Open **Logs Explorer**
2. Filter with:

```text
resource.type="cloud_function"
resource.labels.function_name="hello_gcs"
```

---

## Step 7: Clean Up

```bash
gcloud functions delete hello_gcs --region us-central1
gsutil rm -r gs://$BUCKET_NAME/
```

✅ Always clean up unused functions and buckets

---

## ✅ Summary

- You deployed your first Cloud Function  
- Triggered it via GCS file upload  
- Viewed logs to confirm execution  
- Set up the foundation for file automation

👉 Next: Learn how to extract file metadata from the event payload
