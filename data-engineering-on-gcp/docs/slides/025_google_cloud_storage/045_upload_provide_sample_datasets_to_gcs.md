---
title: "Upload Provided Sample Datasets to GCS"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Let's Upload Sample Data to GCS

We’ll upload multiple file types to simulate a real-world data lake.

---

## Provided Sample Files

You’ll use data files provided by the instructor:

- `orders.csv` (Structured – CSV)
- `customers.json` (Structured – JSON)
- `products.parquet` (Structured – Parquet)
- `iot_data.jsonl` (Semi-structured – JSONL)
- `logs.txt` (Unstructured – Text)

Make sure all files are in a local `./data/` folder.

---

## Structured Data Upload – CSV

```bash
gcloud storage cp ./data/orders.csv \
  gs://$BUCKET_NAME/structured/orders.csv
```

Repeat for:
```bash
gcloud storage cp ./data/customers.json \
  gs://$BUCKET_NAME/structured/customers.json

gcloud storage cp ./data/products.parquet \
  gs://$BUCKET_NAME/structured/products.parquet
```

---

## ⚠️ Restoring BUCKET_NAME If Session Is Lost

If `$BUCKET_NAME` is not set (new terminal), do this:

```bash
## List your buckets
gcloud storage buckets list | grep `whoami`

## Set the bucket name again
export BUCKET_NAME=<BUCKET_NAME_ID>
```

---

## Semi-Structured and Unstructured Uploads

```bash
gcloud storage cp ./data/iot_data.jsonl \
  gs://$BUCKET_NAME/semi-structured/iot_data.jsonl

gcloud storage cp ./data/logs.txt \
  gs://$BUCKET_NAME/unstructured/logs.txt
```

---

## Folder Structure Recap

📁 structured/  
  ├── orders.csv  
  ├── customers.json  
  └── products.parquet  

📁 semi-structured/  
  └── iot_data.jsonl  

📁 unstructured/  
  └── logs.txt

> This simulates a multi-zone data lake: raw, curated, archival, etc.

---

## Verify Uploads in Console

- Go to [console.cloud.google.com/storage](https://console.cloud.google.com/storage)
- Navigate to your bucket
- Check folder paths and confirm each file is present

---

## Summary

✅ Uploaded all key file types  
✅ Structured, semi-structured, unstructured zones organized  
✅ GCS lake is ready for use in downstream pipelines

👉 Next: Secure GCS buckets using IAM policies