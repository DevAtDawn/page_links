from bs4 import BeautifulSoup, SoupStrainer
import requests
import sys
# pip install beautifulsoup4
def main()
    url = sys.argv[1]
    find = sys.argv[2] # 'body' 'source'
    get = sys.argv[3] # 'class' 'src'
    # for x in url:
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data)

    for link in soup.find_all(find):
        # print(link)
        print("\n", link.get(get), "\n")
        #print(link.get('source'))
if __name__ == "__main__":
    main()
