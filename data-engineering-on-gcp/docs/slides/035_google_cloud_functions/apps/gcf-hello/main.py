def hello_gcs(event, context):
    file = event
    print(f"📁 File uploaded: {file['name']}")
    print(f"🪣 Bucket: {file['bucket']}")