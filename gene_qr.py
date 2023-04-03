from coreqr import encod_data, decode_data
import cv2
from pyzbar.pyzbar import decode

# Define your geolocation data as a Python dictionary
location = {
    "latitude": 50.3183202730564860,
    "longitude": 3.5105228796591064,
    "orientation": 1,
}
encod_data = encod_data(location["latitude"], location["longitude"])

img = cv2.imread("test.png")
qrcodes = decode(img)
lat, lon = decode_data(qrcodes)
print(lat, lon, location["orientation"])
