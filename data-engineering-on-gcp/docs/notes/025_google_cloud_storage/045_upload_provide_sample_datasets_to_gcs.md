
# Instructor Notes – Lecture 2.4: Upload Provided Sample Datasets to GCS

---

## 🎯 Objective

Guide learners through uploading real, instructor-provided datasets into Google Cloud Storage using the `gcloud` CLI. Ensure they understand how to reinitialize `BUCKET_NAME` if they switch terminals or lose session.

---

## 🧑‍🏫 Slide-by-Slide Teaching Notes

---

### Slide: Let’s Upload Sample Data to GCS

> “Now that your bucket and folder structure is ready, let’s upload the real data.”

Let learners know these files were curated to reflect real-world data types: CSV, JSON, Parquet, JSONL, TXT.

---

### Slide: Provided Sample Files

> “Make sure you’ve downloaded the files into a local `./data/` folder.”

Clarify:
- These are *not generated dynamically*
- They reflect structured, semi-structured, and unstructured categories

Encourage learners to preview files with `cat`, `head`, or a text editor.

---

### Slide: Structured Data Upload – CSV

> “We’ll start with structured files and upload them using the CLI.”

Walk through each command line by line:
```bash
gcloud storage cp ./data/orders.csv gs://$BUCKET_NAME/structured/orders.csv
```

Repeat for `customers.json` and `products.parquet`.  
Tip: Reinforce folder structure with object pathing.

---

### Slide: ⚠️ Restoring BUCKET_NAME If Session Is Lost

> “If you open a new terminal or forget the bucket name, here’s how to recover.”

Explain:
1. Use below command to find the bucket.

```bash
gcloud storage buckets list | grep `whoami`
```

2. Reassign it to a shell variable:

```bash
# Get id from the above commands output. Make sure to choose right one.
export BUCKET_NAME=<BUCKET_NAME_ID>
```

Make sure learners **do not prefix** with `gs://` when setting the name as a variable unless intended to.

---

### Slide: Semi-Structured and Unstructured Uploads

> “Now let’s finish with our sensor and log data.”

Walk through:
```bash
gcloud storage cp ./data/iot_data.jsonl gs://$BUCKET_NAME/semi-structured/iot_data.jsonl
gcloud storage cp ./data/logs.txt gs://$BUCKET_NAME/unstructured/logs.txt
```

Mention: JSONL is often used in streaming or ML pipelines.

---

### Slide: Folder Structure Recap

> “Here’s what your simulated data lake looks like now.”

Use this to reinforce naming conventions and bucket design patterns.

---

### Slide: Verify Uploads in Console

> “Always validate that your uploads succeeded.”

Instruct them to:
- Open the GCP Console → Storage → Buckets  
- Navigate inside their bucket  
- Confirm each file is in the correct folder

Optional: Ask them to download a file from the Console to test.

---

### Slide: Summary

Reiterate:
- All file types uploaded successfully
- Realistic data lake structure in GCS
- Sets the stage for downstream analytics

> “Up next, we’ll make sure this bucket is secure and properly permissioned.”

---

## 🛠️ Instructor Tips

- Ensure learners reassign the `$BUCKET_NAME` if their session is lost
- If a file upload fails, check:
  - File path or file presence in `./data`
  - gcloud auth/project config
  - IAM permission errors

---

## ✅ Outcomes

By the end of this lecture, learners should:
- Upload datasets to GCS correctly
- Understand how files are organized in object storage
- Know how to recover bucket name and reassign variables across terminals

