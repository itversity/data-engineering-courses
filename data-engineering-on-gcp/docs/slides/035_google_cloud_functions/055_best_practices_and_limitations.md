---
title: "Lecture 5: Best Practices and Limitations of Google Cloud Functions"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Best Practices and Limitations of Google Cloud Functions

> Wrap up the Cloud Functions module with production readiness tips and architectural considerations

---

## 🎯 What You’ll Learn

✅ Package functions properly using `requirements.txt`  
✅ Assign minimal IAM roles for security  
✅ Follow best practices for deployment and organization  
✅ Understand limitations of Cloud Functions  
✅ Clean up consistently after testing

---

## Packaging with requirements.txt

- Declare dependencies clearly
- Required for libraries like `google-cloud-storage`
- File must be in the root of the function directory

```txt
google-cloud-storage
```

✅ Include only what’s necessary

---

## Use --source=. for Deployment

```bash
gcloud functions deploy <function-name> \
  --runtime python311 \
  --trigger-resource <bucket-name> \
  --trigger-event google.storage.object.finalize \
  --entry-point <entry-point> \
  --source=. \
  --region us-central1
```

✅ Ensures your code and dependencies are packaged properly

---

## IAM Role Best Practices

Use the **principle of least privilege**:

| Role | Description |
|------|-------------|
| `roles/storage.objectViewer` | Read-only access to objects |
| `roles/storage.objectCreator` | Upload-only permission |
| `roles/storage.objectAdmin` | Full control (read, write, delete) |

Assign only what's required to the service account used by your function.

---

## Recommended Project Structure

```bash
gcf-<use-case>/
├── main.py
├── requirements.txt
└── README.md (optional)
```

✅ Structure helps with Git, automation, and modularity

---

## Avoid Common Mistakes

| Mistake | Fix |
|--------|-----|
| Missing dependencies | Create `requirements.txt` |
| Trigger not firing | Double-check `--trigger-resource` |
| Recursion/infinite loop | Use folder prefix checks (`structured/`, `invalid/`) |
| No logs shown | Add `print()` in each condition |
| Cost overrun | Clean up unused buckets and functions

---

## Cleanup Best Practices

```bash
gcloud functions delete <function-name> --region us-central1
gsutil rm -r gs://<bucket-name>/
```

✅ Always clean up to control cost and prevent clutter

---

## 🔒 Limitations of Google Cloud Functions

| Limitation | Description |
|------------|-------------|
| Cold starts | Delay on first invocation after inactivity |
| Timeout limits | Max 9 minutes (540 seconds) per function |
| Memory limits | Max 16 GB per instance |
| Stateless | No persistent data between invocations |
| Limited concurrency | One request per instance (unless using 2nd gen) |
| Deployment delay | Deployments may take 1–2 minutes |
| Vendor lock-in | Tightly coupled with GCP eventing and IAM |

🔍 Consider alternatives (Cloud Run, App Engine) for long-running, stateful, or higher-performance needs

---

## ✅ Summary

- You now know how to build and deploy Cloud Functions securely  
- Followed packaging and IAM best practices  
- Learned about Cloud Function limitations  
- Set up a reliable and maintainable project foundation

🎓 You’ve completed the **Google Cloud Functions** module!

👉 Next: Capstone – Apply all these skills in an end-to-end pipeline
