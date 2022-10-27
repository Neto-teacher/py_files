import requests
from pprint import pprint

# response = requests.get('https://www.nozhikov.ru/')
# print(response)
#
# print(type(response))

# https://restapitutorial.ru/httpstatuscodes.html
# https://trinixy.ru/65585-oshibki-servera-po-koshachi-15-foto.html

from requests import HTTPError

# for url in ['https://www.nozhikov.ru/', 'https://www.nozhikovs.ru/']:
#     try:
#         response = requests.get(url)
#     except HTTPError as http_err:
#         print(f'Ошибка: {http_err}')
#     except Exception as err:
#         print(f'Непонятная ошибка: {err}')
#     else:
#         print("Соединение установлено!")

# json_response = requests.get('https://jsonplaceholder.typicode.com/comments', params=b'postId=1')
# pprint(json_response.text)
# pprint(json_response.json())
