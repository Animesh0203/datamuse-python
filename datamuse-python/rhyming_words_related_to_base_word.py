import requests
from bs4 import BeautifulSoup
import json

def rhyming_words_related_to_base_word(base_word, rhyming_word):
    url = f"https://api.datamuse.com/words?ml={base_word}&rel_rhy={rhyming_word}"
    r = requests.get(url)
    print(url)

    soup = BeautifulSoup(r.content, 'html5lib')
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()

    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


