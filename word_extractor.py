import requests
from bs4 import BeautifulSoup
import re

page_url = str(input("URL: "))

def get_html_of(url):
    resp = requests.get(page_url)

    if resp.status_code != 200:
        print(f"Status code: {resp.status_code}.\nStatus code expected: 200. Exiting ...")
        exit(1)

    return resp.content.decode()

html = get_html_of(page_url)
soup = BeautifulSoup(html, 'html.parser')
raw_text = soup.get_text()
all_words = re.findall(r'\w+', raw_text)
word_count = {}

for word in all_words:
    if word not in word_count:
        word_count[word] =  1
    else:
        current_count = word_count.get(word)
        word_count[word] = current_count + 1

print(word_count)