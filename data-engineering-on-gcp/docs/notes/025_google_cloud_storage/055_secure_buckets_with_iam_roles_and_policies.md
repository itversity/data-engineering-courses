# Instructor Notes – Lecture 2.5: Securing GCS Buckets with IAM Roles and Policies

---

## 🎯 Objective

Teach learners how to use Google Cloud IAM to manage access to GCS buckets and objects. Provide hands-on experience assigning and revoking roles at the project and bucket level.

---

## 🧑‍🏫 Slide-by-Slide Teaching Notes

---

### Slide: Securing Your GCS Buckets

> “Security is key to protecting your cloud data.”

Explain why IAM matters — especially for shared projects, public data, and automation.

---

### Slide: What is IAM?

> “IAM stands for Identity and Access Management.”

Clarify:
- IAM controls *who* has *what* access to *which* resources
- Works at both the **project** and **resource** (e.g. bucket) level

---

### Slide: Common IAM Roles for GCS

> “These are the most common roles you’ll assign.”

Emphasize:
- `storage.admin` gives full control (use with caution)
- `objectAdmin` can create/delete objects
- `objectViewer` is safe for read-only access

Encourage “least privilege” principle.

---

### Slide: IAM Member Types

> “Members can be users, service accounts, or even domains.”

Give examples:
- Individual developers
- CI/CD tools via service accounts
- Whole teams via Google Groups

---

### Slide: Assign IAM Role (Project-Level)

> “Use this to give access across the project.”

Demo:
```bash
gcloud projects add-iam-policy-binding $PROJECT_ID   --member="user:<email>"   --role="roles/storage.objectViewer"
```

✅ Read access to all buckets in the project

---

### Slide: Assign IAM Role (Bucket-Level)

> “Use this for fine-grained control.”

Demo:
```bash
gcloud storage buckets add-iam-policy-binding $BUCKET_NAME   --member="user:<email>"   --role="roles/storage.objectViewer"
```

✅ Use case: grant access to a team for **one specific bucket**

---

### Slide: View Current IAM Policy

> “Always verify your changes.”

Run:
```bash
gcloud storage buckets get-iam-policy $BUCKET_NAME
```

Tip: Use this to copy/paste policy bindings or audit access.

---

### Slide: Revoke Access

> “If you gave access by mistake, you can remove it.”

Run:
```bash
gcloud storage buckets remove-iam-policy-binding $BUCKET_NAME   --member="user:<email>"   --role="roles/storage.objectViewer"
```

Optional: Explain audit logs for tracking changes.

---

### Slide: Summary

Reiterate:
- IAM roles control bucket/object access
- Apply roles at project or bucket level
- Use gcloud to assign, verify, and revoke roles

---

## 🛠️ Instructor Tips

- Test your command with your own email or a test user before the session
- If learners are using IAM for the first time, mention the **Storage Admin** role they might have by default
- Encourage viewing IAM from both CLI and GCP Console

---

## ✅ Outcomes

By the end of this lecture, learners should:
- Understand IAM concepts for GCS
- Assign roles at project and bucket levels
- Verify and revoke access when needed