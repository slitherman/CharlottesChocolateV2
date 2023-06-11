import socket
from time import sleep
import random
import json
PORT = 14014
PRODUCT_NO = 8013
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP,PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    amount_sold = random.randint(1, 100)
    stock = amount_sold - 1
    sale = {"ProductNo": PRODUCT_NO,"ChocolateType": "KitKat", "InStock": stock, "AmountSold": amount_sold, "Price": 15}
    sale_json = json.dumps(sale).encode("utf-8")
    sock.sendto(sale_json, ADDR)
    print(sale_json)
    sleep(3)


