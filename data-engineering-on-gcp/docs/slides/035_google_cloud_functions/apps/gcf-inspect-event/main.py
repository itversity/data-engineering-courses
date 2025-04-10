import json

def inspect_event(event, context):
    print("🎯 Full GCS Event Payload:")
    print(json.dumps(event, indent=2))

    print(f"📁 File uploaded: {event.get('name')}")
    print(f"🪣 Bucket: {event.get('bucket')}")
    print(f"📦 Size: {event.get('size')} bytes")
    print(f"📄 Content type: {event.get('contentType')}")
    print(f"📅 Time created: {event.get('timeCreated')}")