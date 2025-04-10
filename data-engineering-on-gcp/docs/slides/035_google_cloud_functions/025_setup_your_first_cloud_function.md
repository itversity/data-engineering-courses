---
title: "Lecture 2: Setting Up Your First Cloud Function"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Setting Up Your First Cloud Function

> Deploy your first event-driven automation on GCP

---

## 🎯 What You’ll Learn

By the end of this lecture, you will:

✅ Create a simple Python-based Cloud Function  
✅ Trigger it using a file upload to GCS  
✅ View logs in both CLI and Console  
✅ Understand how Cloud Functions fit into GCP pipelines

> Keep in mind we will deep dive about `event` in the subsequent lecture. For now we will focus on setting up the first cloud function on GCP.

---

## 🧭 What Are the Steps?

Here’s what we’ll do together:

1. Enable required GCP APIs  
2. Create a test GCS bucket  
3. Write a simple Python function  
4. Deploy it using `gcloud` CLI  
5. Upload a file to trigger it  
6. View execution logs  
7. (Optional) Clean up

---

## Step 1: Enable Required APIs

```bash
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable storage.googleapis.com
```

💡 *Run this once per project.*

---

## Step 2: Create a GCS Bucket

Bucket names must be globally unique.

```bash
BUCKET_NAME=gcf-hello-bucket-$(date +%s)
gsutil mb -l us-central1 gs://$BUCKET_NAME/
echo "✅ Bucket created: $BUCKET_NAME"

# Validate bucket
gsutil ls gs://$BUCKET_NAME/
```

---

## Step 3: Write the Cloud Function

Create the folder and file:

```bash
mkdir gcf-hello
cd gcf-hello
nano main.py
```

Paste this code:

```python
def hello_gcs(event, context):
    file = event
    print(f"📁 File uploaded: {file['name']}")
    print(f"🪣 Bucket: {file['bucket']}")
```

✅ Save: `Ctrl+O` → `Enter` → `Ctrl+X`

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

🧠 *Deploys the function and connects it to GCS file upload events.*

---

## Step 5: Upload a File to Trigger It

```bash
echo "hello world" > testfile.txt
gsutil cp testfile.txt gs://$BUCKET_NAME/

# Validate whether file is successfully copied or not
gsutil ls gs://$BUCKET_NAME/
```

---

## Step 6: View Logs – Option A (CLI)

```bash
gcloud functions logs read hello_gcs --region us-central1
```

✅ Output should include:
```
📁 File uploaded: testfile.txt
🪣 Bucket: gcf-hello-bucket-...
```

---

## Step 6: View Logs – Option B (Console)

Go to **Cloud Logging > Logs Explorer**  
Use this filter:

```text
resource.type="cloud_function"
resource.labels.function_name="hello_gcs"
```

---

## Step 7: Cleanup (Optional)

```bash
gcloud functions delete hello_gcs --region us-central1
gsutil rm -r gs://$BUCKET_NAME/
```

🚨 Clean up unused resources to avoid charges.

---

## ✅ Summary

You have:

- Created and deployed a Python Cloud Function  
- Triggered it using GCS file upload  
- Verified execution via Cloud Logging  
- Done it all without any external dependencies

👉 You’re ready to extract file metadata and automate even more!
