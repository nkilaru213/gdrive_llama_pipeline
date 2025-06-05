from io import BytesIO
from googleapiclient.http import MediaIoBaseDownload
import textract

def download_and_extract_text(file_id, drive_service):
    request = drive_service.files().get_media(fileId=file_id)
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        _, done = downloader.next_chunk()
    fh.seek(0)
    text = textract.process(fh).decode('utf-8')
    return text