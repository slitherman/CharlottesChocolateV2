import socket
from time import sleep
import random
import json
import requests
PORT = 14014
PRODUCT_NO = 8013
URL = "https://charlottesstockapiv2.azurewebsites.net/api/EasterEggs"
IP = ""
ADDR = (IP,PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ADDR)

while True:
    data, addr = sock.recvfrom(1024)
    received_data = data.decode("utf-8")
    sales_json = json.loads(received_data)
    print("after loading json")
    print(sales_json)
    update_easteregg = requests.put(f"{URL}/{PRODUCT_NO}", json=sales_json)
    print("statuscode")
    print(update_easteregg.status_code)
    print("result after sending json")
    print(update_easteregg.text)
    sleep(5)



