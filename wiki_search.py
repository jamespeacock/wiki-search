import wikipedia
import sys
from wikipedia.exceptions import DisambiguationError

WIKI_HOST = "https://en.wikipedia.org"

def search_results(q_term):
    try:
        page = wikipedia.page(q_term)
        return [page.url]
    except DisambiguationError as e:
        page_list = [WIKI_HOST + p.get('href') for p in e.options]
        return page_list

if __name__ == '__main__':
    print(search_results(sys.argv[1]))

