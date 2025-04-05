
# Instructor Notes – Lecture 2.6: Configure Lifecycle Policies for Cost Optimization

---

## 🎯 Objective

Introduce learners to lifecycle policies in Google Cloud Storage and guide them on how to configure, apply, view, and remove these policies using JSON configuration files and the gcloud CLI.

---

## 🧑‍🏫 Slide-by-Slide Teaching Notes

---

### Slide: Automate Bucket Management with Lifecycle Rules

> “Lifecycle rules automate object management. This helps reduce cost and avoid manual cleanup.”

Use relatable examples:
- Temporary files in staging areas
- A data lake with historical logs or sensor data
- Archiving infrequently used files

---

### Slide: What Are Lifecycle Policies?

> “They are JSON-defined rules evaluated daily by GCS for each bucket.”

Clarify:
- Not real-time → GCS evaluates lifecycle once a day
- Can automate both deletion and storage class transitions

---

### Slide: Common Lifecycle Use Cases

> “These use cases cover both cost-saving and compliance needs.”

Examples:
- Auto-delete old backups (age-based)
- Move objects to Coldline after 60 days (transition-based)
- Auto-clean folders like `tmp/` or `raw/`

---

### Slide: Sample Policy – Delete After 30 Days

> “This rule tells GCS to delete any object older than 30 days.”

Break down the JSON:
- `action.type`: Delete
- `condition.age`: 30

Show learners how to save this policy:
```bash
nano lifecycle_config.json
```

---

### Slide: Apply Lifecycle Policy

> “Apply the policy to your bucket using gcloud CLI.”

Command:
```bash
gcloud storage buckets update $BUCKET_NAME \
  --lifecycle-file=lifecycle_config.json
```

📝 Ensure learners verify `$BUCKET_NAME` is still set in the session.

---

### Slide: View Existing Lifecycle Policy

> “Verify that the policy was applied successfully.”

Command:
```bash
gcloud storage buckets describe $BUCKET_NAME \
  --format="default(lifecycle)"
```

Walk through the returned JSON format with them.

---

### Slide: Remove Lifecycle Policy (Reset)

> “You can always clear lifecycle rules.”

Command:
```bash
gcloud storage buckets update $BUCKET_NAME --clear-lifecycle
```

Important: Removing the rule doesn’t delete existing objects.

---

### Slide: Summary

Emphasize:
- Lifecycle policies are essential for automating storage management
- JSON + CLI = repeatable and production-ready
- Useful in dev, test, and prod environments

---

## 🛠️ Instructor Tips

- Use the Console UI if learners are struggling with CLI
- Walk around during lab time to help with editing or setting bucket name
- Offer additional examples like transition to Coldline or matching by prefix

---

## ✅ Outcomes

By the end of this session, learners will:
- Understand lifecycle rules and why they matter
- Know how to write and apply JSON-based policies using the CLI
- Be able to validate and remove policies with confidence

