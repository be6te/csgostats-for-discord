from cloudscraper import create_scraper
from core.scraper import scraperw
scrape = scraperw()
requests = create_scraper()

class RequestAPI:
    def __init__(self):
        self.steam_key = 'your steam key'

    def GetSteamID(self, url):
        data = requests.post('https://faceitfinder.com/', data={'name': url})
        final = data.text.split('<script type="text/javascript">window.location.replace("/profile/')[1].split('");</script>')[0]
        return str(final)

    def AvatarURL(self, user):
        avatar = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.steam_key}&steamids={user}").json()['response']['players'][0]['avatar']
        return avatar

    def CSGOStats(self, final_url):
        data = scrape.scrapers(base_url=f'https://csgostats.gg/player/{self.GetSteamID(url=final_url)}')
        return data
