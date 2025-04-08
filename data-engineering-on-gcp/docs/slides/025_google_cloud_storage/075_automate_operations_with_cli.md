---
title: "Automate Common GCS Tasks using CLI"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Power Up Your GCS CLI Productivity!

Let’s streamline real-world tasks using `gcloud` and `gsutil` for scale and automation.

---

## gcloud vs gsutil

✅ `gcloud` is the general-purpose CLI for all Google Cloud services — including Storage  
✅ `gsutil` is a specialized, high-performance tool for Cloud Storage operations

Both tools are included with the Google Cloud SDK.

---

## Recursive Uploads (gcloud)

```bash
gcloud storage cp --recursive ./data/ \
  gs://$BUCKET_NAME/structured/
```

Uploads all files from local `data/` to your GCS bucket.

---

## Recursive Uploads (gsutil)

```bash
gsutil -m cp -r ./data \
  gs://$BUCKET_NAME/structured/
```

✅ `-m` enables parallel/multi-threaded uploads  
✅ Much faster for large datasets

---

## Download Files Recursively

```bash
gcloud storage cp --recursive \
  gs://$BUCKET_NAME/unstructured/ \
  ./downloads/unstructured/
```

OR using gsutil:

```bash
gsutil -m cp -r \
  gs://$BUCKET_NAME/unstructured/ \
  ./downloads/unstructured/
```

---

## Sync Local and Remote Buckets

```bash
gsutil rsync -r ./data \
  gs://$BUCKET_NAME/structured
```

- Syncs only changed/new files
- Ideal for backups and mirroring

Reverse sync:

```bash
gsutil rsync -r \
  gs://$BUCKET_NAME/structured \
  ./local-backup/
```

---

## Advanced File Listings

```bash
gcloud storage ls --recursive gs://$BUCKET_NAME/
```

```bash
gsutil ls -l gs://$BUCKET_NAME/**
gsutil ls gs://$BUCKET_NAME/**/*.csv
```

✅ Use wildcards for filtering  
✅ `-l` shows file size and timestamps

---

## Inspect Object Metadata

```bash
gcloud storage objects describe \
  gs://$BUCKET_NAME/structured/orders.csv
```

Or using:

```bash
gsutil stat gs://$BUCKET_NAME/structured/orders.csv
```

---

## Set Metadata (e.g., Cache-Control)

```bash
gsutil setmeta -h "Cache-Control:no-cache" \
  gs://$BUCKET_NAME/site/index.html
```

Used for:
- Static web hosting
- Controlling freshness for browsers

---

## Save Transfer Logs

```bash
gsutil -m cp -r ./data \
  gs://$BUCKET_NAME/structured/ \
  -L transfer-log.txt
```

Creates a log of all file transfer success/failures.

---

## Summary

✅ Use `gcloud` for simplicity and scripting  
✅ Use `gsutil` for power, speed, and automation  
✅ Combine both to build efficient GCS workflows

👉 Next: Hands-on with BigQuery