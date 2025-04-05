## Instructor Script – Lecture 1.4: Understanding GCP Billing

---

### **Slide: Why Understand GCP Billing?**

**Instructor Notes:**

> “One of the biggest anxieties when learning cloud platforms is **cost** — ‘Will I get charged if I click the wrong button?’”

Explain:
- GCP’s billing can be confusing at first but is very manageable if you follow a few good practices.
- This lecture will help learners **gain confidence** using the platform without fear of surprise charges.

---

### **Slide: Accessing the Billing Console**

**Instructor Notes:**

> “Let’s start by seeing where you can track everything.”

Walk learners through:

1. Go to [console.cloud.google.com/billing](https://console.cloud.google.com/billing)
2. Select the **Billing Account** they linked earlier
3. Explore these sections:
   - **Reports** → “Visual breakdown of usage and spend”
   - **Budgets & Alerts** → “Set limits and get notified”
   - **Cost Table** → “See daily itemized charges”
   - **Transactions** → “Detailed invoice-level view”

Mention:
> “You’ll use this console a lot once you start running real pipelines.”

---

### **Slide: Free Tier vs Trial Credits**

**Instructor Notes:**

> “Let’s clear up two things that are often confused: **Trial credits vs Always Free tier.**”

Explain:

| Term          | Meaning                                  |
|---------------|-------------------------------------------|
| **Free Trial** | $300 credit, lasts for 90 days            |
| **Always Free** | Small amounts of usage for certain services, forever |

- Example: BigQuery always includes 1TB/month query and 10GB storage for free.
- Clarify:
  > “Even if your $300 expires, you can keep experimenting with Always Free services.”

---

### **Slide: Set Budget Alerts**

**Instructor Notes:**

> “The best way to avoid surprises? Set a budget.”

Walk them through (console steps, not CLI):

- Navigate to **Billing → Budgets & Alerts**
- Create a **budget for your project or billing account**
- Set thresholds:
  - 50% → mild alert
  - 80% → check usage
  - 100% → time to pause

Mention:
> “GCP won’t automatically stop services, but alerts give you time to act.”

Optional Tip: “Set a small $10 alert if you're just experimenting.”

---

### **Slide: View Cost by Service**

**Instructor Notes:**

> “This is where you find out which service is costing you the most.”

Demonstrate or explain how:

- Go to **Billing → Reports**
- Use filters:
  - By project (if working on multiple)
  - By service (e.g., BigQuery, GCS, Dataflow)

Encourage learners:
> “Get into the habit of checking this weekly when you’re building on GCP.”

---

### **Slide: Daily Cost Breakdown**

**Instructor Notes:**

> “Want to know what you spent *yesterday*? This is the place.”

Explain:

- Go to **Billing → Cost Table**
- Customize time ranges
- Helps identify spikes — e.g., large BigQuery scan or a background pipeline that didn’t stop

Tip:
> “Daily views help catch runaway costs early.”

---

### **Slide: Best Practices**

**Instructor Notes:**

Summarize with proactive habits:

- 🔒 **Restrict IAM permissions** — don’t let every user create high-cost resources
- 💳 **Check usage weekly** — especially for services with cost per query
- 📩 **Use budget alerts** — and adjust thresholds as needed
- 🧪 **Stick to Always Free limits** — especially during initial practice

If applicable, share a quick anecdote about someone getting charged unexpectedly — and how alerts could have helped.

---

### **Slide: Summary**

**Instructor Notes:**

> “You now know how to keep GCP costs under control.”

Reinforce:
- Where to access billing tools
- How to read usage reports
- How to stay within free-tier limits
- What alerts to configure

> “With that foundation, you can now start using GCP safely and confidently.”

---

Up next: “Google Cloud Storage — Scalable Data Lakes.”