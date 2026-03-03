import sys 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Crawler:

    def __init__ (self, url):

        self._title = ""
        self._links = []
        self._body = ""

        self._url = url
        self.crawl(url)


    def crawl(self,url):

        options = Options()
        options.add_argument("--headless") 

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)

        try:
            driver.get(url)

        except Exception:
            print("Error: Unable to fetch the webpage")
            sys.exit(1)
            
        
        
        self._title = driver.title
        
        try:
            body = driver.find_element(By.TAG_NAME, "body")
            self._body = body.text
        except:
            self._body = ""

        links = driver.find_elements(By.TAG_NAME, "a")
        for l in links:
            link = l.get_attribute('href')
            if link:
                self._links.append(link)

        driver.quit()

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