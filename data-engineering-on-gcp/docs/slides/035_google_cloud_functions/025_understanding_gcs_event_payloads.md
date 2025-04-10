---
title: "Lecture 2: Understanding GCS Event Payloads"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Understanding GCS Event Payloads

> Learn to access and utilize metadata from uploaded files

---

## 🎯 What You’ll Learn

✅ Understand the `event` object passed to Cloud Functions  
✅ Learn how GCS triggers Cloud Functions with metadata  
✅ Extract key metadata: name, size, type, timestamp  
✅ Use this information to drive automation logic  
✅ View logs to confirm metadata structure  
✅ Set up a complete app: `gcf-inspect-event`

---

## Step 1: GCS Event Triggers

When a file is uploaded to GCS, it triggers your function with an `event` dictionary:

```python
def hello_gcs(event, context):
    ...
```

- `event`: file metadata (JSON from GCS)  
- `context`: trigger metadata (includes `event_id`, `timestamp`, etc.)

---

## Step 2: Sample Event Payload

```json
{
  "bucket": "demo-bucket",
  "name": "sales_20250410.csv",
  "size": "2048",
  "contentType": "text/csv",
  "timeCreated": "2025-04-10T10:45:00Z"
}
```

---

## Step 3: Key Fields in the `event`

| Field | Description |
|-------|-------------|
| `bucket` | GCS bucket name |
| `name` | Full path of the file |
| `size` | File size in bytes |
| `contentType` | MIME type of file |
| `timeCreated` | Timestamp when file was uploaded |

---

## Step 4: Create Application – `gcf-inspect-event`

```bash
mkdir gcf-inspect-event
cd gcf-inspect-event
```

Create `main.py` with the following:

```python
import json

def inspect_event(event, context):
    print("📦 Full GCS Event:")
    print(json.dumps(event, indent=2))

    print(f"📁 File: {event.get('name')}")
    print(f"🪣 Bucket: {event.get('bucket')}")
    print(f"📦 Size: {event.get('size')} bytes")
    print(f"📄 Type: {event.get('contentType')}")
    print(f"🕒 Created: {event.get('timeCreated')}")
```

✅ No `requirements.txt` needed

---

## Step 5: Create a GCS Bucket

```bash
BUCKET_NAME=gcf-inspect-bucket-$(date +%s)
gsutil mb -l us-central1 gs://$BUCKET_NAME/
```

---

## Step 6: Deploy the Function

```bash
gcloud functions deploy inspect_event \
  --runtime python311 \
  --trigger-resource $BUCKET_NAME \
  --trigger-event google.storage.object.finalize \
  --entry-point inspect_event \
  --source=. \
  --region us-central1
```

---

## Step 7: Upload a File to Trigger

```bash
echo "some data" > test.csv
gsutil cp test.csv gs://$BUCKET_NAME/
```

---

## Step 8: View Logs (CLI)

```bash
gcloud functions logs read inspect_event --region us-central1
```

✅ Should display full GCS event and extracted fields

---

## Step 9: View Logs (Console)

1. Open **Logs Explorer**
2. Use this filter:

```text
resource.type="cloud_function"
resource.labels.function_name="inspect_event"
```

---

## Step 10: Clean Up

```bash
gcloud functions delete inspect_event --region us-central1
gsutil rm -r gs://$BUCKET_NAME/
```

✅ Helps prevent billing issues

---

## ✅ Summary

- You extracted file metadata from GCS-triggered events  
- Understood key fields: `name`, `bucket`, `size`, `contentType`, `timeCreated`  
- Built a standalone app: `gcf-inspect-event`  
- Prepared to automate workflows based on metadata

👉 Next: Use this metadata to rename and organize files automatically
