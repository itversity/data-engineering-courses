# Instructor Notes – Lecture 2.7: Automate Common GCS Tasks using CLI (Enhanced)

---

## 🎯 Objective

Introduce learners to both `gcloud` and `gsutil` CLI tools for working with GCS, with a focus on real-world automation, efficiency, and scale. Explain when and why to use each tool.

---

## 🧑‍🏫 Slide-by-Slide Teaching Notes

---

### Slide: Power Up Your GCS CLI Productivity

> “Let’s unlock power-user techniques for managing GCS at scale.”

Frame this lecture as the "automation booster pack" for data engineers.

---

### Slide: gcloud vs gsutil

> “Both tools are included with the SDK — let’s look at where each shines.”

- `gcloud`: user-friendly, structured output, used throughout the course so far
- `gsutil`: faster, supports parallelization, advanced features
- Great time to introduce `-m`, `rsync`, and `setmeta`

---

### Slide: Recursive Uploads – gcloud

Demo:
```bash
gcloud storage cp --recursive ./data/ gs://$BUCKET_NAME/structured/
```

✅ Beginner-friendly  
⚠️ Slower for large file sets

---

### Slide: Recursive Uploads – gsutil

Demo:
```bash
gsutil -m cp -r ./data gs://$BUCKET_NAME/structured/
```

- Highlight `-m` for parallelism
- Explain why this scales better for automation

---

### Slide: Download Files Recursively

Compare `gcloud` and `gsutil` commands  
Let learners try both and observe speed differences.

---

### Slide: Sync Local and Remote Buckets

```bash
gsutil rsync -r ./data gs://$BUCKET_NAME/structured
```

Use case:  
- Staging → backup  
- Local → GCS mirroring

Reverse sync is also worth demoing.

---

### Slide: Advanced File Listings

Demo pattern matching with:
```bash
gsutil ls gs://$BUCKET_NAME/**/*.csv
```

Show how `-l` gives file sizes and timestamps, which is missing in `gcloud`.

---

### Slide: Inspect Object Metadata

```bash
gcloud storage objects describe ...
gsutil stat ...
```

Use both to demonstrate:
- Metadata structure
- Practical use in automation scripts

---

### Slide: Set Metadata

```bash
gsutil setmeta -h "Cache-Control:no-cache" gs://...
```

Scenario:  
- Hosting static content (e.g. index.html)
- Forcing browsers to bypass cache

---

### Slide: Save Transfer Logs

```bash
gsutil -m cp -r ./data gs://... -L log.txt
```

Call out use cases for:
- Auditing uploads
- Debugging failures in CI/CD

---

### Slide: Summary

Reinforce:
- `gcloud` is great for learning and scripting
- `gsutil` is a must-have for scale and performance
- Both are CLI superpowers for GCS automation

---

## 🛠️ Instructor Tips

- Encourage learners to test commands on subfolders and filtered paths
- Show how `gsutil` is script-friendly for crons or Airflow jobs
- Recap bucket structure from earlier labs before starting

---

## ✅ Outcomes

By the end of this lecture, learners should be able to:
- Confidently switch between `gcloud` and `gsutil`
- Choose the right CLI for the job
- Automate and optimize their data lake operations

