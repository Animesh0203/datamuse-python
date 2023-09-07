import requests
from bs4 import BeautifulSoup
import json

def rwords_that_describe_adjectives(word1):
    url = f"https://api.datamuse.com/words?rel_jib={word1}"
    r = requests.get(url)
    print(url)

    soup = BeautifulSoup(r.content, 'html5lib')
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()

    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


