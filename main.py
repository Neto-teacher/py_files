import csv
import sys

# with open("files/newsafr.csv", newline="", encoding="utf-8") as f:
#     reader = csv.reader(f)
# print(type(reader))
# for r in reader:
#     print(r[-2])
# Как вариант чтобы избавиться от title, можем преобразовать данные в список.
# news_list = list(reader)
# print(type(news_list))
# print(news_list)
# header = news_list.pop(0)
# print(header)
# for r in news_list:
#     print(r[-1])

# Выводим в словарь
# with open("files/newsafr.csv", newline="", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
# news_list = list(reader)
# print(news_list[30])
# for r in reader:
#     print(r["title"])

# Записываем данные в файл
# a = append, w = write, r = read
# with open("files/newsafr.csv", newline="", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     news_list = list(reader)
# header = news_list.pop(0)
# with open("files/newsafr2.csv", "w", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerows(news_list)

# with open("files/newsafr.csv", newline="", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     news_list = list(reader)
# header = news_list.pop(0)
#
# csv.register_dialect("customcsv", delimiter=";", quoting=csv.QUOTE_ALL)
# # csv.register_dialect("customcsv", delimiter=",", quoting=csv.QUOTE_NONE, escapechar="\\")
# # #
# with open("files/newsafr2.csv", "w", encoding="utf-8") as f:
#     writer = csv.writer(f, "customcsv")
#     writer.writerow(header)
#     writer.writerows(news_list)

# Формат JSON
# import json
#
# with open("files/newsafr.json", encoding="utf-8") as f:
#     json_data = json.load(f)

# print(type(json_data))
# news_list = json_data["rss"]["channel"]["items"]
# for news in news_list:
#     print(news["title"])
# #
# # # сохраняем в новый файл данные
# with open("files/newsafr2.json", "w", encoding="utf-8") as f:
#     json.dump(json_data, f, ensure_ascii=False, indent=4)

# sys.exit()

# import json
#
# with open("files/codebeautify.json", encoding="utf-8") as f:
#     json_data = json.load(f)
#
# news_list = json_data["rss"]["channel"]["item"] #!!!!
# for news in news_list:
#     if news["pubDate"][6] == '0':
#         print(news["pubDate"], news["title"])
#
# # # сохраняем в новый файл данные
# with open("files/codebeautify2.json", "w", encoding="utf-8") as f:
#     json.dumps(json_data, f, ensure_ascii=False, indent=4)
# #
# sys.exit()

import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
xml_data = ET.parse("files/codebeautify.xml", parser)
xml_root = xml_data.getroot()
# print(xml_root.attrib)
# print(xml_root.tag)
#
titles = xml_root.findall("channel/item/title")
print(len(titles))
for title in titles:
    print(title.text)
# #
# sys.exit()
