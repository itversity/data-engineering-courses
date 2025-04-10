from google.cloud import storage
from datetime import datetime

def rename_and_organize(event, context):
    bucket_name = event['bucket']
    original_file_name = event['name']

    if original_file_name.startswith('structured/'):
        print(f"Skipping already organized file: {original_file_name}")
        return

    filename = original_file_name.split('/')[-1]
    if '.' not in filename:
        print(f"Skipping file without extension: {filename}")
        return

    base_name, ext = filename.rsplit('.', 1)

    created_date = event.get('timeCreated') or datetime.utcnow().isoformat()
    date_obj = datetime.strptime(created_date[:10], "%Y-%m-%d")
    today_str = date_obj.strftime('%Y-%m-%d')
    date_suffix = date_obj.strftime('%Y%m%d')

    new_filename = f"{base_name}_{date_suffix}.{ext}"
    destination_path = f"structured/{today_str}/{new_filename}"

    client = storage.Client()
    bucket = client.bucket(bucket_name)

    source_blob = bucket.blob(original_file_name)
    destination_blob = bucket.blob(destination_path)

    bucket.copy_blob(source_blob, bucket, destination_blob.name)
    source_blob.delete()

    print(f"Moved file: {original_file_name} → {destination_path}")