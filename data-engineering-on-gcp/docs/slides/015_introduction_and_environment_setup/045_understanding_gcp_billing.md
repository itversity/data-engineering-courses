---
title: "Understanding GCP Billing"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

# Why Understand GCP Billing?

- Cloud billing can be tricky if not monitored
- Important to know what services cost money
- Helps you stay within **free-tier limits** and avoid accidental charges

---

# Accessing the Billing Console

- Go to: [console.cloud.google.com/billing](https://console.cloud.google.com/billing)
- Select your **Billing Account**
- Navigate using:
  - **Reports**
  - **Budgets & Alerts**
  - **Cost Table**
  - **Transactions**

---

# Free Tier vs Trial Credits

| Type | What You Get |
|---------------|----------------------------------------|
| Free Trial | $300 credit for 90 days |
| Always Free | Limited usage of services (e.g., BigQuery, GCS) |

> ⚠️ Trial credits expire after 90 days even if unused!

---

# Set Budget Alerts

```bash
# Navigate: Billing → Budgets & alerts
```

- Create a **new budget** for a project or billing account
- Set thresholds (e.g., 50%, 80%, 100%)
- You’ll receive email notifications

✅ Helps you proactively monitor usage

---

# View Cost by Service

- Go to: **Billing → Reports**
- Filter by **Project** or **Service**
- Useful for identifying which service is costing more

---

# Daily Cost Breakdown

- Go to: **Billing → Cost Table**
- Track cost trends daily
- Use filters for time range and service

---

# Best Practices

- 🔒 **Set IAM permissions** carefully — don’t allow everyone to create resources
- 💳 **Monitor spending** weekly
- 📩 **Use budget alerts**
- 🧪 Stay within **Always Free Tier** during learning

---

# Summary

✅ You now know how to:  
- Access and navigate billing console  
- Monitor costs and set budget alerts  
- Stay within trial/free tier  
- Practice safe cloud usage 🧠

👉 Next: Dive into **Google Cloud Storage: Scalable Data Lakes**

---
