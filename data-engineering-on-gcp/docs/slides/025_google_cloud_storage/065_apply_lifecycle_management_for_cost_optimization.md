---
title: "Configure Lifecycle Policies for Cost Optimization"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Automate Bucket Management with Lifecycle Rules

Lifecycle rules help reduce storage cost and automate data retention.

---

## What Are Lifecycle Policies?

Rules that automatically:

- Delete old data
- Move objects to cheaper storage classes
- Optimize bucket cost management

Applied at the **bucket level** using JSON policy files

---

## Common Lifecycle Use Cases

- Delete files older than 30 days  
- Transition cold data to Nearline/Coldline  
- Auto-clean staging data folders  
- Enforce compliance policies

---

## Sample Policy: Delete Objects Older Than 30 Days

```json
{
  "rule": [
    {
      "action": {"type": "Delete"},
      "condition": {"age": 30}
    }
  ]
}
```

Save this as `lifecycle_config.json`

---

## Apply Lifecycle Policy

```bash
gcloud storage buckets update $BUCKET_NAME \
  --lifecycle-file=lifecycle_config.json
```

✅ The policy takes effect immediately  
🔍 Objects are only deleted during daily scans by GCS

---

## View Existing Lifecycle Policy

```bash
gcloud storage buckets describe $BUCKET_NAME \
  --format="default(lifecycle)"
```

---

## Remove Lifecycle Policy (Reset)

```bash
gcloud storage buckets update $BUCKET_NAME \
  --clear-lifecycle
```

---

## Summary

✅ Lifecycle rules automate retention and storage class transitions  
✅ Configured via JSON + CLI  
✅ Helps manage long-term cost effectively

👉 Next: Automate GCS tasks with CLI tips and scripting