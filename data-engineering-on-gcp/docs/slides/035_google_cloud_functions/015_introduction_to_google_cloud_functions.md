---
title: "Lecture 1: Introduction to Google Cloud Functions"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Introduction to Google Cloud Functions

> Automate and scale event-driven logic using serverless functions

- Zero infrastructure to manage
- Triggered by events (e.g., file uploads to GCS)
- Lightweight, fast, and cost-effective

---

## Why Cloud Functions?

- Automate file handling in your data lake
- Run custom logic on object creation
- Integrate with GCP Services such as GCS, BigQuery, Pub/Sub, HTTP, Firestore, and more

Use Cases:
- Rename or move files
- Validate uploaded content
- Trigger downstream workflows

---

## GCP Workflow Context

```
GCS → Cloud Function → BigQuery / Dataflow
```

- Cloud Function acts as the **automation bridge**
- Executes **in response to file uploads**
- **No manual intervention** required

---

## What Triggers a Cloud Function?

Cloud Functions can be triggered by:

✅ Google Cloud Storage  
✅ Pub/Sub  
✅ HTTP requests  
✅ Firebase events  
✅ Firestore / Cloud Scheduler

> In this module, we focus on **GCS-triggered functions**

---

## Serverless = No Infrastructure to Manage

- Automatically scales based on demand
- Billed per 100ms of execution time
- Supports multiple languages (we use Python)

Benefits:
- Easy to deploy
- Built-in logging and monitoring
- Works seamlessly with GCP services

---

## Anatomy of a Cloud Function (Python)

```python
def hello_gcs(event, context):
    file = event
    print(f"File {file['name']} uploaded to {file['bucket']}")
```

Parameters:
- `event`: metadata about the file (for GCS based events)
- `context`: info about the trigger (optional)

---

## Typical Cloud Function Flow

1. A file is uploaded to a GCS bucket
2. Cloud Function is triggered
3. Your code runs and processes the event
4. Optionally:
   - Rename/move the file
   - Log details
   - Trigger additional workflows

---

## What You'll Learn in This Module

- Create and deploy Python Cloud Functions
- Automate GCS workflows (rename, validate, log)
- Use Cloud Logging to view file upload events
- Prepare for integration with BigQuery and Dataflow

---

## Recap

Google Cloud Functions is:

- Event-driven
- Serverless
- Perfect for data automation

> Next: Let's deploy our **first Cloud Function** that prints a message when a file is uploaded!
