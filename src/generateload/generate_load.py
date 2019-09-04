from azure.storage.queue import QueueService, QueueMessageFormat
import base64
queue_service = QueueService(connection_string="")
queue_service.encode_function = QueueMessageFormat.text_base64encode

for y in range(0, 4):
    for x in range(0, 1000):
        queue_service.put_message('images', f"https://BLOB_LOCATION.blob.core.windows.net/images/Cat/{x}.jpg")
        queue_service.put_message('images', f"https://BLOB_LOCATION.blob.core.windows.net/images/Dog/{x}.jpg")
    