---
title: "Securing GCS Buckets with IAM Roles and Policies"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Securing Your GCS Buckets

### Let’s control who can access your data

---

## What is IAM?

**IAM (Identity and Access Management)** lets you:

- Grant or restrict access to GCP resources
- Assign **roles** to **members** at the **project or bucket level**
- Audit access through permissions

---

## Common IAM Roles for GCS

| Role | Purpose |
|-----------------------------|------------------------------|
| roles/storage.admin | Full access to all storage |
| roles/storage.objectAdmin | Manage objects only |
| roles/storage.objectViewer | Read-only object access |

> Always follow the principle of least privilege.

---

## IAM Member Types

- **User** – e.g., user:john@example.com
- **Service Account** – e.g., serviceAccount:etl-bot@project.iam.gserviceaccount.com
- **Group** – e.g., group:data-team@example.com
- **Domain** – e.g., domain:example.com

---

## Assign IAM Role to a User (Project-Level)

```bash
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="user:your-email@gmail.com" \
  --role="roles/storage.objectViewer"
```

✅ This gives read-only access to **all buckets** in the project

---

## Assign IAM Role to a User (Bucket-Level)

```bash
gcloud storage buckets add-iam-policy-binding $BUCKET_NAME \
  --member="user:your-email@gmail.com" \
  --role="roles/storage.objectViewer"
```

✅ Use this to restrict access to just **one bucket**

---

## View Current IAM Policy (Bucket-Level)

```bash
gcloud storage buckets get-iam-policy $BUCKET_NAME
```

🔍 Helpful to confirm if bindings were applied correctly

---

## Revoke Access (Optional)

```bash
gcloud storage buckets remove-iam-policy-binding $BUCKET_NAME \
  --member="user:your-email@gmail.com" \
  --role="roles/storage.objectViewer"
```

---

## Summary

✅ You learned about IAM roles  
✅ Assigned access at both project and bucket level  
✅ Practiced fine-grained security with GCS

👉 Next: Automate cost control with lifecycle rules