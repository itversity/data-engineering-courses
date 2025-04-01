---
theme: black
transition: slide
---

# Setting Up PostgreSQL on GCP Cloud SQL
### A Comprehensive Guide

---

### What is GCP?

- Google's Public Cloud Platform
- Managed Services including Cloud SQL
- Focus on Innovation
- $300 free credits for new users

---

### Why PostgreSQL?

- Standards Compliance
- Complex Query Support
- Extensibility
- Performance
- Vibrant Community

---

### Setting Up PostgreSQL

#### Project Setup
1. Navigate to GCP Console
2. Create/select project
3. Enable Cloud SQL Admin API

```bash
gcloud services enable sqladmin.googleapis.com
```

---

### Instance Creation

```bash
gcloud sql instances create perf-demo-instance \
    --database-version=POSTGRES_15 \
    --cpu=1 \
    --memory=3840MB \
    --region=us-central1
```

---

### Network Configuration

#### Security Best Practices
- Enable SSL connections
- Use strong passwords
- Restrict IP ranges
- Keep up with security patches

---

### Performance Tuning

#### Basic Configuration
```sql
ALTER SYSTEM SET shared_buffers = '1GB';
ALTER SYSTEM SET work_mem = '16MB';
```

#### Monitoring
```sql
CREATE EXTENSION pg_stat_statements;
```

---

### Database Operations

#### Creating Database & Tables
```sql
CREATE DATABASE performance_tuning;

CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE,
    amount DECIMAL(10,2)
);
```

---

### Maintenance Tasks

- Regular VACUUM ANALYZE
- Index Management
- Backup Strategy
- Performance Monitoring

---

### Troubleshooting Tips

- Connection Problems
- Performance Issues
- Storage Concerns
- Query Optimization

---

### Summary

- GCP Project Setup
- PostgreSQL Configuration
- Security Best Practices
- Performance Tuning
- Maintenance Strategy

---

### Thank You!

#### Questions?

Visit [cloud.google.com](https://cloud.google.com) to get started 