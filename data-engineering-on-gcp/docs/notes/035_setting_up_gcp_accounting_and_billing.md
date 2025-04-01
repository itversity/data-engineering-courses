## Instructor Script – Lecture 1.3: Setting Up GCP Account and Billing

---

### **Slide: Step 1 – Sign Up for Google Cloud**

**Instructor Notes:**

> “We’re now ready to get hands-on. The first step is creating a Google Cloud account.”

- Guide learners to [console.cloud.google.com](https://console.cloud.google.com)
- Clarify that a personal Gmail account is enough.
- Mention: “If you’re using a work email, make sure it doesn’t have enterprise restrictions.”

---

### **Slide: Step 2 – Activate Free Trial**

**Instructor Notes:**

> “GCP offers a generous free trial — $300 of credits, valid for 90 days.”

- Reassure learners: “You won’t be charged unless you explicitly upgrade to a paid account.”
- Mention that a **credit card is required**, but it’s only for validation.
- Recommend setting up budget alerts in a later lecture to avoid accidental charges.

---

### **Slide: Step 3 – Create Your First Project (Console)**

**Instructor Notes:**

> “Projects are the basic unit of organization in GCP — every resource must be attached to a project.”

- Walk through creating a new project using the console:
  - “Use a meaningful project name like `gcp-data-engineering`.”
  - “You may or may not see an organization dropdown — that’s okay.”

Optional: Show how to **pin the project** in the top nav for quick access.

---

### **Slide: Step 4 – Install Google Cloud SDK (CLI)**

**Instructor Notes:**

> “Let’s install the command-line interface — the `gcloud` CLI — which we’ll use throughout the course.”

Give OS-specific guidance:

- **macOS**: Uses Homebrew
- **Linux**: Debian/Ubuntu steps with GPG key setup
- **Windows**: Download from SDK page and run `.exe`

📝 Encourage learners to follow the install guide matching their OS and verify that the `gcloud` command is available in terminal/PowerShell.

---

### **Slide: Step 5 – Verify Installation**

**Instructor Notes:**

> “Let’s confirm that the CLI is installed.”

Ask learners to run:

```bash
gcloud --version
```

- Confirm it returns the version and installed components.
- If errors show up, advise them to recheck their shell configuration or PATH variable.

---

### **Slide: Step 6 – Initialize gcloud CLI**

**Instructor Notes:**

> “Now let’s connect the CLI to your Google account and set up defaults.”

Guide learners through:

```bash
gcloud init
```

- This opens a browser window for login.
- Instruct them to **select the correct project** during setup.
- Explain that this also sets their **default region/zone** (can be changed later).

---

### **Slide: Step 7 – Create a Project Using CLI**

**Instructor Notes:**

> “You can also create projects using the CLI. It’s good to know both console and CLI approaches.”

Show this command:

```bash
gcloud projects create gcp-data-engineering \
  --name="GCP Data Engineering"
```

Then:

```bash
gcloud config set project gcp-data-engineering
```

- Make sure to explain that this sets the active project context for all future commands.

---

### **Slide: Step 8 – Set Quota Project for ADC**

**Instructor Notes:**

> “This step ensures Application Default Credentials (ADC) associate correctly with the project for programmatic access.”

```bash
gcloud auth application-default set-quota-project gcp-data-engineering
```

Explain:
- “This becomes important when working with Python libraries like `google-cloud-storage` or `google-cloud-bigquery` later on.”

---

### **Slide: Step 9 – Link Billing Account**

**Instructor Notes:**

> “Let’s quickly link the billing account — we’ll dive deeper into cost control in the next lecture.”

Use this CLI flow:

```bash
gcloud beta billing accounts list
```

Then:

```bash
gcloud beta billing projects link gcp-data-engineering \
  --billing-account=XXXXXX-XXXXXX-XXXXXX
```

- Note: “Copy the billing account ID from the output of the first command.”

---

### **Slide: Step 10 – Enable Required APIs**

**Instructor Notes:**

> “Before using GCP services, we must enable their APIs.”

Run these:

```bash
gcloud services enable storage.googleapis.com
gcloud services enable bigquery.googleapis.com
gcloud services enable dataflow.googleapis.com
```

- Explain this is like “flipping a switch” to allow programmatic access.
- Mention: “Each GCP service has an associated API that needs to be turned on per project.”

---

### **Slide: Summary**

**Instructor Notes:**

> “To recap — we’ve created our GCP environment, installed the CLI, initialized it, and configured our first project.”

Checklist to reinforce:

- ✅ Account created and verified
- ✅ CLI installed and working
- ✅ Project created via console and CLI
- ✅ Billing and APIs configured

> “Now we’re ready to start building! In the next lesson, we’ll break down billing further and learn how to avoid surprises with cost.”
