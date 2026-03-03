import sys 
import requests
from bs4 import BeautifulSoup

class Crawler:

    def __init__ (self, url):

        self._title = ""
        self._links = []
        self._body = ""

        self._url = url
        self.crawl(url)


    def crawl(self,url):

        headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'} 
        try:
            webpage = requests.get(url,headers=headers)
            webpage.raise_for_status()

        except requests.exceptions.RequestException:
            print("Error: Unable to fetch the webpage")
            sys.exit(1)
            
        soup = BeautifulSoup(webpage.text,features="html.parser")
        
        if soup.title:
            self._title = soup.title.text
        
        if soup.body:
            self._body = soup.body.get_text(separator=" ",strip = True)

        links = soup.find_all('a')
        for l in links:
            link = l.get('href')
            if link:
                self._links.append(link)


    def getTitle(self):
        return self._title.strip()
    
    
    def getLinks(self):
        return self._links
    
    
    def getBody(self):
        return self._body
    

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Error: Provide the url!!!")
        sys.exit(1)
        
    url = sys.argv[1]

    if not url.startswith("http"):
        url = "https://" + url
    crawler = Crawler(url)

    print(crawler.getTitle())
    print(crawler.getBody())
    for link in crawler.getLinks():
        print(link)