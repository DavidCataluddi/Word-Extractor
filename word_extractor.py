import requests
from bs4 import BeautifulSoup
import re
import click

def get_html_of(url):
    r = requests.get(url)

    if r.status_code != 200:
        print(f"Error, status code does not match: {r.status_code}")
        exit(1)

    return r.content.decode()

def get_all_words_from(url):
    content = get_html_of(url)
    soup = BeautifulSoup(content, 'html.parser')
    raw_html = soup.get_text()
    return re.findall(r'\w+', raw_html)

def word_count_in(word_list, min_length):
    word_count = {}
    for word in word_list:
        if len(word) < min_length:
            continue
        if word not in word_count:
            word_count[word] = 1
        else:
            current_count = word_count.get(word)
            word_count[word] = current_count + 1
    return word_count

def get_top_words_from(all_words, min_length):
    occurences = word_count_in(all_words, min_length)
    return sorted(occurences.items(), key=lambda item: item[1], reverse=True)

@click.command()
@click.option('--url', '-u', prompt='Web URL', help='URL from webpage to extract on.')
@click.option('--length', '-l', default=0, help='Minimum word length (from 0 to no limit)')

def main(url, length):
    the_words = get_all_words_from(url)
    top_words = get_top_words_from(the_words, length)    

    for i in range(10):
        print(top_words[i][0])

if __name__ == '__main__':
    main()
