import re
from google.cloud import storage

def validate_file(event, context):
    bucket_name = event['bucket']
    file_name = event['name']

    if file_name.startswith("invalid/"):
        print(f"Skipping already moved file: {file_name}")
        return

    if not file_name.endswith('.csv'):
        reason = "Invalid extension"
    elif not re.match(r'^sales_\d{8}\.csv$', file_name.split('/')[-1]):
        reason = "Invalid filename format"
    else:
        print(f"✅ File is valid: {file_name}")
        return

    print(f"🚫 File is invalid: {file_name}. Reason: {reason}")

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    source_blob = bucket.blob(file_name)
    destination_blob = bucket.blob(f"invalid/{file_name.split('/')[-1]}")

    bucket.copy_blob(source_blob, bucket, destination_blob.name)
    source_blob.delete()

    print(f"Moved to: invalid/{file_name.split('/')[-1]}")