
# Instructor Notes – Lecture 2.3: Creating Buckets and Folder Structure using CLI

---

## 🎯 Objective

Guide learners through creating a uniquely named GCS bucket and simulating a folder structure using the `gcloud` CLI. Emphasize global uniqueness of bucket names and real-world naming best practices.

---

## 🧑‍🏫 Slide-by-Slide Teaching Notes

---

### Slide: Hands-On with GCS

> “Time to roll up our sleeves and build the backbone of our data lake.”

Briefly revisit what a bucket is and why we need one for uploading files.

---

### Slide: Prerequisites

> “Let’s make sure everything is ready.”

Confirm:
- gcloud is installed and initialized
- Active GCP project is selected
- Billing is linked and APIs are enabled

---

### Slide: Bucket Naming – Important Note

> “Bucket names must be globally unique across all GCP users.”

Explain that learners **will get errors** like `409 Bucket name already exists` if they use generic names like `gcs-data-lake-tutorials`.

---

### Slide: Naming Tip

> “Let’s make our bucket names unique using environment variables.”

Guide learners through:
```bash
BUCKET_NAME="gcs-data-lake-$(whoami)-$(date +%Y%m%d%H%M%S)"
```

- Explain: `whoami` = username, `date` adds uniqueness
- Show how to create the bucket using the `$BUCKET_NAME` variable

Emphasize: This technique avoids frustration in hands-on labs.

---

### Slide: Simulate Folder Structure in GCS

> “GCS has no true folders — we simulate them using object name prefixes.”

Explain and demonstrate:
```bash
echo "placeholder" | gcloud storage cp - gs://$BUCKET_NAME/structured/placeholder.txt
```

Repeat for `semi-structured/` and `unstructured/`.

---

### Slide: Verifying Your Work

> “Let’s head to the GCP Console and see the structure.”

Point learners to the Console → Storage → Buckets  
Confirm they can see folder-like views in their bucket.

---

### Slide: Optional – Lifecycle Rules Later

> “We’ll explore more automation later — for now, structure is in place.”

Remind learners:
- You can organize by business unit, data type, or time
- This prepares the bucket for lifecycle policies or IAM

---

### Slide: Summary

Reinforce:
- Bucket created with unique name
- Folder structure simulated
- Ready for uploading provided data files

> “In the next lecture, we’ll upload actual datasets to our GCS data lake.”

---

## 🛠️ Instructor Tips

- Check that learners are using their **own bucket names**
- If multiple learners are in the same org, suggest using initials or email prefix
- Encourage learners to save their bucket name in a shell variable for later use

---

## ✅ Outcomes

By the end of this lecture, learners should:
- Be able to create a GCS bucket using CLI
- Understand global uniqueness of bucket names
- Simulate folder structure with object naming

