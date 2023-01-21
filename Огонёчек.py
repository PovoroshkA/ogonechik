import requests
from requests.structures import CaseInsensitiveDict
import time
syt = str(input("Начала ссылки: "))
b = str(input("Количество огоньков: "))
url = "https://events.webinar.ru/api/light/reactions/eventsessions/" + syt + "/likes"
token = str(input("Вставте токин: "))

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = token
headers["Content-Type"] = "application/json"
headers["Content-Length"] = "0"
a = 1
while a != b:
    try:
        resp = requests.post(url, headers=headers)
    except ArithmeticError:
        print("Ошибочка")
    a = a + 1
    time.sleep(0.1)
    print("Отправка")
    

print(resp.status_code)

