---
title: "GCS Concepts and Fundamentals"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## GCS Structure and Terminology

Google Cloud Storage is organized as:

- **Buckets**: Top-level containers
- **Objects**: Files inside buckets
- **Folders**: Simulated using object prefixes (not real directories)

---

## Buckets

- Globally unique names (e.g., `gcs-data-lake-bucket`)
- Created in a specific location (region or multi-region)
- Associated with a GCP project
- Used to store one or more objects (files)

> Think of buckets like a top-level folder.

---

## Objects

- Binary data + metadata
- Immutable (you can overwrite but not edit in place)
- Accessed using URI: `gs://bucket-name/path/to/object`
- Can be any file type (CSV, JSON, Parquet, images, etc.)

---

## Storage Classes

| Class | Use Case | Cost | Availability |
|------------|-----------------------------|-------|--------------|
| Standard | Frequent access | $$$ | High |
| Nearline | Access ~ once per month | $$ | High |
| Coldline | Backup or DR (~quarterly) | $ | Medium |
| Archive | Long-term compliance | $ | Lower |

> You can set lifecycle rules to transition between classes.

---

## Locations

| Type | Example | Description |
|-----------------|----------------|------------------------------|
| Regional | us-central1 | Single region, low latency |
| Multi-regional | us | Redundant across regions |
| Dual-region | nam4 | Two nearby regions (active-active)

---

## Security: IAM and Encryption

- Access controlled using IAM roles (bucket-level or project-level)
- Object ACLs for fine-grained control (optional)
- Encryption:
  - Google-managed (default)
  - Customer-managed (CMEK)
  - Customer-supplied (CSEK)

---

## Metadata and Object Labels

- Each object has metadata: content type, size, creation time
- You can attach custom **labels** for:
  - Organization
  - Cost tracking
  - Workflow classification

---

## Simulating Folders with Prefixes

- GCS does not have real directories
- Use `/` in object names to simulate folders:
  - `structured/orders.csv`
  - `logs/2024/04/server.log`

> Tools like `gsutil` and GCP Console interpret these as folders.

---

## Summary

- GCS uses **buckets** to store **objects** with metadata
- Choose **storage classes** and **locations** based on access pattern
- Secure with **IAM** and automate with **lifecycle policies**

👉 Next: Create your first GCS bucket using CLI