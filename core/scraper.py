import cloudscraper
import re
import json
from bs4 import BeautifulSoup

class scraperw:
    def __init__(self):
        self.id = ''

    def scrapers(self, base_url):
        url = base_url
        flag = False
        
        while not flag:
            try:
                sc = cloudscraper.create_scraper()
                html_text = sc.get(url).text
                flag = True
            except:
                continue
        
        p = re.compile('var stats = .*')
        soup = BeautifulSoup(html_text, 'lxml')
        name = soup.find('div', id='player-name')
        scripts = soup.find_all('script')
        data = ''
        
        for script in scripts:
            try:
                m = p.match(script.string.strip())

                if m:
                    data = m.group()
                    break
            except:
                continue
            
        data_json = json.loads(data[12:-1])
        return data_json
    
    def PlayerName(self, base_url):
        url = base_url
        flag = False
        
        while not flag:
            try:
                sc = cloudscraper.create_scraper()
                html_text = sc.get(url).text
                flag = True
            except:
                continue
        
        p = re.compile('var stats = .*')
        soup = BeautifulSoup(html_text, 'lxml')
        name = soup.find('div', id='player-name').text

        return str(name)