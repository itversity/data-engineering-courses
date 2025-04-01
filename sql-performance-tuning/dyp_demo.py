import os
import glob
import pandas as pd
import psycopg2
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def load_file(file, conn_string):
    try:
        df = pd.read_csv(file)
        df.to_sql('toyota_sales', conn_string, if_exists='append', index=False)
        return f"Successfully loaded {file}"
    except Exception as e:
        return f"Error loading {file}: {str(e)}"

def main(num_files=12, max_workers=4):
    base_dir = 'data/toyota_sales_10years'
    files = sorted(glob.glob(os.path.join(base_dir, '*.csv')))[:num_files]
    print(f"Found {len(files)} files to load")
    conn_string = "postgresql://postgres:perfdemo123@34.58.132.114:5432/performance_tuning"
    
    start_time = time.time()
    
    # Using ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Create future tasks
        future_to_file = {
            executor.submit(load_file, file, conn_string): file 
            for file in files
        }
        
        # Process completed tasks
        for future in as_completed(future_to_file):
            file = future_to_file[future]
            try:
                result = future.result()
                print(result)
            except Exception as e:
                print(f"Error processing {file}: {str(e)}")
    
    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()