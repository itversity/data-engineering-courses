---
title: "Creating Buckets and Folder Structure using CLI"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Hands-On with GCS

### Let's create our first bucket and simulate folder structure using the CLI!

---

## Prerequisites

✅ Google Cloud SDK installed  
✅ gcloud initialized with active project  
✅ Billing enabled  
✅ APIs enabled (storage.googleapis.com)

---

## Bucket Naming – Important Note

- GCS bucket names must be **globally unique**
- Even across all GCP users worldwide
- Common names like `gcs-data-lake-tutorials` may already be taken

---

## Naming Tip

Use your username or timestamp to ensure uniqueness:

```bash
BUCKET_NAME="gcs-data-lake-$(whoami)-$(date +%Y%m%d%H%M%S)"
gcloud storage buckets create gs://$BUCKET_NAME \
  --location=us-central1 \
  --default-storage-class=STANDARD
```

- Saves debugging time and avoids name collision

---

## Simulate Folder Structure in GCS

GCS doesn’t have folders, but you can **simulate them** using object prefixes.

Example:
```bash
echo "placeholder" | gcloud storage cp - \
  gs://$BUCKET_NAME/structured/placeholder.txt

echo "placeholder" | gcloud storage cp - \
  gs://$BUCKET_NAME/semi-structured/placeholder.txt

echo "placeholder" | gcloud storage cp - \
  gs://$BUCKET_NAME/unstructured/placeholder.txt
```

---

## Verifying Your Work

- Go to [console.cloud.google.com/storage](https://console.cloud.google.com/storage)
- Navigate to your bucket
- You should see the simulated folders and placeholder files

---

## Optional: Create Lifecycle Rules Later

Once the structure is in place, you can:

- Upload real data
- Set policies (lifecycle, IAM, encryption)
- Organize by time or project (e.g. `logs/2025/04/`)

---

## Summary

✅ You created a uniquely named bucket  
✅ Simulated folders using object prefixes  
✅ Ready to upload sample data in the next step

👉 Coming up next: Upload Provided Sample Datasets to GCS