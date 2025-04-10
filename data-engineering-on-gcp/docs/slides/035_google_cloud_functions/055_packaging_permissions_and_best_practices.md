---
title: "Lecture 5: Packaging, Permissions, and Best Practices"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Packaging, Permissions, and Best Practices

> Wrap up the Cloud Functions module with real-world tips and professional deployment hygiene

---

## 🎯 What You’ll Learn

✅ Package functions properly using `requirements.txt`  
✅ Assign minimal IAM roles for security  
✅ Follow project structure best practices  
✅ Avoid common mistakes  
✅ Clean up consistently after deployment

---

## requirements.txt

- Declare external dependencies
- Must be in the root of your function folder
- Example:

```txt
google-cloud-storage
```

✅ Include only what’s needed

---

## Use --source=. for Accurate Deployments

```bash
gcloud functions deploy <function-name> \
  --runtime python311 \
  --trigger-resource <bucket-name> \
  --trigger-event google.storage.object.finalize \
  --entry-point <entry-point> \
  --source=. \
  --region us-central1
```

✅ Ensures your `main.py` and `requirements.txt` are included

---

## IAM Roles for Cloud Functions

Use **least privilege**:

| Role | Purpose |
|------|---------|
| `roles/storage.objectViewer` | Read access to GCS |
| `roles/storage.objectCreator` | Write access to GCS |
| `roles/storage.objectAdmin` | Full access for copy/delete |

Assign to the service account tied to your function.

---

## Project Folder Structure

```bash
gcf-<use-case>/
├── main.py
├── requirements.txt
└── README.md (optional)
```

✅ Isolate each function for easier testing, version control, and reuse

---

## Avoid These Common Pitfalls

| Problem | Solution |
|--------|----------|
| Missing libraries | Add `requirements.txt` |
| Wrong trigger bucket | Double-check `--trigger-resource` |
| Infinite loops | Check for path prefixes (`structured/`, `invalid/`) |
| Function deploys but does nothing | Add `print()` to every logic branch |
| Unused resources incurring cost | Use `gcloud functions delete` & `gsutil rm -r` |

---

## Cleanup Routine (Always)

```bash
gcloud functions delete <function-name> --region us-central1
gsutil rm -r gs://<bucket-name>/
```

✅ Keep your environment clean and cost-effective

---

## ✅ Summary

- You now know how to build, package, deploy, and clean up Cloud Functions  
- You've applied security best practices with IAM  
- You're ready for real-world use and cloud automation workflows

🎓 Congratulations! You’ve completed the **Google Cloud Functions** module.

👉 Next: Capstone – Build an end-to-end GCP Data Pipeline
