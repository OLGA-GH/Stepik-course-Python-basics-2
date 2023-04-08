import requests
import re
from urllib.parse import urlparse

url = input()

res = requests.get(url)
url_list = re.findall(r'<a.+href=[\'"]([^./][^\'"]*)[\'"]', res.text)

domains_list = []
domains_formatted = []

for _ in url_list:
    parsed_url = urlparse(_)
    if parsed_url.netloc:
        domains_list.append(parsed_url.netloc)
    elif parsed_url.path:
        domains_list.append(parsed_url.path)

for _ in domains_list:
    domain = _.split(":")[0]
    if domain not in domains_formatted:
        domains_formatted.append(domain)

domains_formatted.sort()

for _ in domains_formatted:
    print(_)
