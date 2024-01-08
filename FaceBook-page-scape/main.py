#import Facebook_scraper class from facebook_page_scraper
from facebook_page_scraper import Facebook_scraper
import json
#instantiate the Facebook_scraper class

page_name = "100083716701774"
posts_count = 3000
browser = "chrome"
proxy = "IP:PORT" #if proxy requires authentication then user:password@IP:PORT
timeout = 3600 #30 seconds
headless = False
meta_ai = Facebook_scraper(page_name, posts_count, browser, timeout=timeout, headless=headless)

#call the scrap_to_json() method

json_data = meta_ai.scrap_to_json()
print(json_data)

with open("./test1.json", "w") as outfile:
    json.dump(json_data, outfile, indent=4)

