# Data Processing using Azure Functions
## Overview of Azure Functions 
Azure Functions are nothing but serverless functions provided as part of Azure Platform.
* Azure Functions is a serverless solution that allows you to maintain less infrastructure, write less code and save on costs.
* Azure Functions meets the demand with as many resources and function instances as necessary, but only while needed.
* You can follow this (page)[https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview] to get more details about Google Cloud Functions.

## Create First Azure Function using Python
Here are the instructions to create first Azure function using Python.
* Search for Azure Function
* Follow the steps as demonstrated to create first Azure Function
* Create a function app
* Name : `file_format_converter`
* Runtime stack : Python
* Review and create 

## Run and Validate Azure Function
Here are the instructions to run and validate Azure Function.
* Go to function app for Testing and click on test/run
## Review File Format Converter Logic using Pandas
* Source: `landing/retail_db/orders`
* Source File Format: `CSV`
* Schema: `landing/retail_db/schemas.json`
* Target: `bronze/retail_db/orders`
* Target File Format: `parquet`

Here is the design for the file format conversion.
* The application should take table name as argument.
* It has to read the schema from schemas.json and need to be applied on CSV data while creating Pandas Data Frame.
* The Data Frame should be written to target using target file format.
* Source location, Target location as well as base folders should be passed as environment variables.

```
import json
import os
import pandas as pd


def get_columns(input_base_dir, ds_name):
    schemas = json.load(open(f'{input_base_dir}/schemas.json'))
    columns = list(map(lambda td: td['column_name'], schemas[ds_name]))
    return columns


input_base_dir="<source location>"

output_base_dir = "<target location"
ds_name = 'orders'
columns = get_columns(input_base_dir, ds_name)
print(columns)
for file in os.listdir(f'{input_base_dir}/{ds_name}'):
    print(file)
    df = pd.read_csv(f'{input_base_dir}/{ds_name}/{file}', names=columns)
    os.makedirs(f'{output_base_dir}/{ds_name}', exist_ok=True)
    df.to_parquet(f'{output_base_dir}/{ds_name}/{file}.snappy.parquet')
```
## Deploy Inline Application as Azure Function
As we have reviewed the core logic, let us make sure to deploy file format converted as Azure Function.
* Create Function with relevant run time (Python 3.9).
* Update `requirements.txt` with all the required dependencies.
* Update the program file with the logic to convert the file format.
* Update Environment Variables for container names as well as base folder names.
## Run Inline Application as Azure Function
As File Format Converter as deployed as Azure Function, let us go through the details of running it. We will also validate to confirm if the Azure Function is working as expected or not.
* Run the Azure Function by passing Table Name as run time argument.
* Review the logs to confirm, the Azure Function is executed with out any errors.
* Review the files in ADLS in the target location.
* Use Pandas `read_parquet` to see if the data in the converted files can be read into Pandas Data Frame.





