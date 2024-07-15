import cv2
import requests
import os

TELEGRAM_BOT_TOKEN = "6675736979:AAF9tiLMyI-cRCSnJ-iK-qi1TeTUihAN12A"
TELEGRAM_CHAT_ID = "6386971205"

def send_telegram_message(message, photo=None):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

    if photo:
        photo_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
        photo_data = {"chat_id": TELEGRAM_CHAT_ID}
        files = {'photo': open(photo, 'rb')}
        requests.post(photo_url, data=photo_data, files=files)

def send_alert_with_snapshot(image):
    # Save the image
    snapshot_path = 'snapshot.jpg'
    cv2.imwrite(snapshot_path, image)

    # Send Telegram alert
    message = "Unknown person detected! Please check the snapshot."
    send_telegram_message(message, snapshot_path)

    # Delete the snapshot after sending
    os.remove(snapshot_path)
