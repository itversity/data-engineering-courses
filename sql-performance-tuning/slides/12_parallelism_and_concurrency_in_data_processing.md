---
theme: black
transition: slide
---

# Parallelism and Concurrency in Data Processing
### SQL Performance Tuning Scenario #10

---

### Native vs Application Processing

#### Native Database Processing
```sql
-- Example: Aggregating Data Using SQL
SELECT 
    DATE_TRUNC('month', sale_date) AS "Sale Month",
    car_model AS "Car Model",
    SUM(sale_amount) AS "Revenue"
FROM toyota_sales
GROUP BY DATE_TRUNC('month', sale_date), car_model
ORDER BY "Sale Month", "Car Model";
```

### Advantages
- Optimized execution plans with indexes
- Database engine manages memory and parallelism
- Minimized data transfer overhead

---

### Application Processing (Avoid)

```python
### The Wrong Way: Fetching Raw Data and Processing in Python
import pandas as pd
from sqlalchemy import create_engine

### Read the entire table into DataFrame
query = "SELECT * FROM toyota_sales"
df = pd.read_sql(query, engine)

### Process in Python
monthly_revenue = df.groupby([
    df['sale_date'].dt.to_period('M'),
    'car_model'
])['sale_amount'].sum().reset_index()
```

### Disadvantages
- Increases network overhead
- Slows down performance
- Consumes more memory and CPU

---

### DYP (Do Yourself Parallelism)

#### What is DYP?
- Manual implementation of parallel execution
- Optimizes large dataset operations
- Uses multi-threading/multiprocessing

### Use Cases
- Parallel data loading from multiple files
- Executing batch SQL queries
- Writing large query results to CSV

---

### Parallel Data Loading

#### Sequential Processing (Slow)
```python
### Loads files one by one
for file in files:
    df = pd.read_csv(file)
    table_name = file.replace(".csv", "")
    df.to_sql(table_name, engine, if_exists="replace", index=False)
```

#### Parallel Processing (Fast)
```python
from concurrent.futures import ThreadPoolExecutor

def load_file(file):
    df = pd.read_csv(file)
    table_name = file.replace(".csv", "")    
    df.to_sql(table_name, engine, if_exists="replace", index=False)

with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(load_file, files)
```

---

### Parallel Query Execution

```python
def get_table_count(table):
    query = f"SELECT COUNT(*) as count FROM {table}"
    result = pd.read_sql(query, engine)
    return table, result.iloc[0, 0]

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(get_table_count, tables))
```

### Benefits
- Executes multiple queries in parallel
- Optimized for large-scale data validation
- Reduces total runtime

---

### Parallel File Loading with Schema

```python
def db_loader(src_base_dir, db_conn_uri, ds_name):
    schemas = json.load(open(f'{src_base_dir}/schemas.json'))
    files = glob.glob(f'{src_base_dir}/{ds_name}/part-*')
    
    for file in files:
        df_reader = read_csv(file, schemas)
        for df in df_reader:
            to_sql(df, db_conn_uri, ds_name)

with ThreadPoolExecutor() as executor:
    future_to_ds_name = {
        executor.submit(db_loader, src_base_dir, db_conn_uri, ds_name): ds_name 
        for ds_name in ds_names
    }
```

---

### Best Practices

#### SQL Processing is Best For
- Large-scale aggregations
- Filtering and joins
- Optimized query execution
- Reducing data transfer

#### Application Processing is Best For
- Handling large files
- Parallel execution
- Complex transformations

---

### DYP Implementation Tips

#### ThreadPoolExecutor Usage
- Choose appropriate max_workers
- Handle exceptions properly
- Monitor resource usage
- Clean up resources

#### Performance Considerations
- Balance CPU vs I/O operations
- Monitor memory usage
- Handle database connections properly

---

### Common Pitfalls

#### Resource Management
- Too many concurrent connections
- Memory leaks
- Unclosed file handles

#### Error Handling
- Failed parallel operations
- Partial data loading
- Connection timeouts

---

### Monitoring and Optimization

```python
### Monitor parallel operations
def monitor_execution(future):
    try:
        result = future.result()
        print(f"Successfully completed: {result}")
    except Exception as e:
        print(f"Error occurred: {e}")

### Track progress
for future in as_completed(future_to_ds_name):
    monitor_execution(future)
```

---

### Summary

#### Key Requirements
1. Choose right processing approach
2. Implement proper parallelism
3. Handle resources efficiently
4. Monitor performance
5. Handle errors gracefully

---

### Key Takeaways

- Use native SQL when possible
- Implement DYP for file operations
- Monitor resource usage
- Handle errors properly
- Clean up resources

---

### Thank You!

#### Next Up: Scenario #11
### Advanced Database Optimization Techniques

Stay tuned for more SQL performance tuning insights! 🚀 