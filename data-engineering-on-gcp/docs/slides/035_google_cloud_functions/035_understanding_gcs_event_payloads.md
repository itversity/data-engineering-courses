---
title: "Lecture 3: Understanding GCS Event Payloads"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Understanding GCS Event Payloads

> Learn how to access and use metadata sent from GCS

---

## 🎯 What You’ll Learn

✅ Understand the structure of the GCS event  
✅ Extract file name, size, type, timestamp  
✅ Prepare for validation and automation  
✅ Clean up deployed resources

---

## 🧭 Steps We'll Follow

1. Recap GCS event triggers  
2. Examine sample event payload  
3. Update function to print metadata  
4. Upload a file and check logs  
5. Clean up resources

---

## Step 1: Recap – GCS Triggers

- `google.storage.object.finalize` = trigger on upload  
- Sends file metadata as an `event` object to your function

```python
def hello_gcs(event, context):
    ...
```

- `event`: GCS metadata  
- `context`: trigger metadata

---

## Step 2: Sample Event Payload

```json
{
  "bucket": "gcf-demo-bucket",
  "name": "orders_20250408.csv",
  "size": "2048",
  "contentType": "text/csv",
  "timeCreated": "2025-04-08T10:45:00Z",
  "updated": "2025-04-08T10:45:00Z",
  "metageneration": "1"
}
```

---

## Step 3: Key Fields

| Key | Description |
|-----|-------------|
| `bucket` | GCS bucket name |
| `name` | File path or name |
| `size` | File size in bytes |
| `contentType` | MIME type |
| `timeCreated` | Upload time |
| `updated` | Metadata update time |

---

## Step 4: Update Function (`main.py`)

In `gcf-inspect-event/main.py`:

```python
import json

def inspect_event(event, context):
    print("🎯 Full GCS Event Payload:")
    print(json.dumps(event, indent=2))

    print(f"📁 File uploaded: {event.get('name')}")
    print(f"🪣 Bucket: {event.get('bucket')}")
    print(f"📦 Size: {event.get('size')} bytes")
    print(f"📄 Content type: {event.get('contentType')}")
    print(f"📅 Time created: {event.get('timeCreated')}")
```

---

## Step 5: Create Bucket & Deploy the Function

```bash
# Create a new bucket with a unique name
BUCKET_NAME=gcf-inspect-bucket-$(date +%s)
gsutil mb -l us-central1 gs://$BUCKET_NAME/
```

Now deploy the function:

```bash
gcloud functions deploy inspect_event \
  --runtime python311 \
  --trigger-resource $BUCKET_NAME \
  --trigger-event google.storage.object.finalize \
  --entry-point inspect_event \
  --region us-central1
```

---

## Step 6: Upload and Trigger

```bash
echo "id,amount" > sample.csv
gsutil cp sample.csv gs://$BUCKET_NAME/
```

---

## Step 7: View Logs (CLI)

```bash
gcloud functions logs read inspect_event --region us-central1
```

✅ Check output for:
- Full event JSON
- Extracted fields like filename, size, and type

---

## Step 7: View Logs (Console)

- Go to **Logs Explorer**  
- Filter by:
```text
resource.type="cloud_function"
resource.labels.function_name="inspect_event"
```

---

## Step 8: Clean Up

```bash
gcloud functions delete inspect_event --region us-central1
gsutil rm -r gs://$BUCKET_NAME/
```

✅ Always clean up to avoid unnecessary billing.

---

## ✅ Summary

- You inspected GCS file upload events  
- Logged detailed metadata  
- Prepared to automate file renaming, validation, and organization

👉 Next: Use this metadata to rename and organize uploaded files!
