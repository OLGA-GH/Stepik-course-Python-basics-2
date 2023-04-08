import requests
import re

urlA = input()
urlB = input()

answer = "No"

def extract_urls_to_list(url):
    url_list = list()
    res = requests.get(url)
    if res.status_code != 200:
        return False

    url_list = re.findall(
        r'a href="(.*?)"', res.text)
    for found_url in url_list:
        res = requests.get(found_url)
        if res.status_code != 200:
            url_list.remove(found_url)

    return url_list

url_list_on_a = extract_urls_to_list(urlA)

if url_list_on_a:
    for url in url_list_on_a:
        if urlB in extract_urls_to_list(url):
            answer = "Yes"
            break

print(answer)
