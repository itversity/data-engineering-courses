---
title: "Setting Up GCP Account and Billing"
author: "Data Engineering Essentials using GCP"
theme: white
revealOptions:
  transition: slide
---

## Step 1: Sign Up for Google Cloud

- Go to 👉 [console.cloud.google.com](https://console.cloud.google.com)
- Sign in or create a **Google Account**
- Click **Activate** on the free trial banner

---

## Step 2: Activate Free Trial

- Get **$300 in credits** valid for **90 days**
- Enter required billing info (credit card verification only)
- You won’t be charged unless you upgrade
- ⚠️ Stay within **free-tier limits**

---

## Step 3: Create Your First Project (Using Console)

1. Navigate to the top bar and click **Project Selector**
2. Click **"New Project"**
3. Provide:
   - **Project name**
   - (Optional) **Organization**
4. Click **Create**

---

## Step 4: Install Google Cloud SDK (CLI)

### macOS

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install --cask google-cloud-sdk
```

Edit shell config:

```bash
nano ~/.zshrc
export PATH="/opt/homebrew/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/bin:$PATH"
source ~/.zshrc
```

---

### Linux (Debian/Ubuntu)

```bash
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt-get update && sudo apt-get install google-cloud-sdk
```

---

### Windows

- Download installer from [cloud.google.com/sdk](https://cloud.google.com/sdk/docs/install)
- Run `.exe` and follow installation prompts

---

## Step 5: Verify Installation

```bash
gcloud --version
```

✅ If version appears, the SDK is installed.

---

## Step 6: Initialize gcloud CLI

```bash
gcloud init
```

- Authenticate with your Google account  
- Choose default project and region

---

## Step 7: Create a Project (Using CLI)

```bash
## Create a GCP project
gcloud auth application-default login

PROJECT_NAME=gcp-data-engineering-$(date +%y%M%d%m)
gcloud projects create ${PROJECT_NAME} \
  --name="GCP Data Engineering"

## Project id (after create) cannot be more than 30 characters.
```

```bash
## Set it as the active project
gcloud config set project ${PROJECT_NAME}
```

---

## Step 8: Set Quota Project for ADC (Recommended)

```bash
gcloud auth application-default set-quota-project ${PROJECT_NAME}
```

Ensures Application Default Credentials (ADC) are associated correctly.

---

## Step 9: Link Billing Account

> We'll cover billing in detail later, but here's the minimal setup:

```bash
## List billing accounts
gcloud beta billing accounts list

## Link billing account
gcloud beta billing projects link ${PROJECT_NAME} \
  --billing-account=YOUR_BILLING_ACCOUNT_ID
```

---

## Step 10: Enable Required APIs

```bash
gcloud services enable storage.googleapis.com
gcloud services enable bigquery.googleapis.com
gcloud services enable dataflow.googleapis.com
```

---

## Summary

✅ GCP account created  
✅ CLI installed and initialized  
✅ Project created (console + CLI)  
✅ APIs enabled and ready to go!

👉 Next: Dive into **Google Cloud Storage for Data Lakes**

---
