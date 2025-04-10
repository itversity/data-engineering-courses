def log_file_metadata(event, context):
    file_name = event.get('name')
    bucket = event.get('bucket')
    size = event.get('size', 'unknown')
    content_type = event.get('contentType', 'unknown')
    time_created = event.get('timeCreated', 'unknown')

    print("📄 File Uploaded:")
    print(f"📁 Name       : {file_name}")
    print(f"🪣 Bucket     : {bucket}")
    print(f"📦 Size       : {size} bytes")
    print(f"📄 Type       : {content_type}")
    print(f"⏱️ Created At : {time_created}")