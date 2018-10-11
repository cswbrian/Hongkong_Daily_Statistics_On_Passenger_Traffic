import scraperwiki

import requests
from bs4 import BeautifulSoup
import re

from datetime import datetime
from datetime import timedelta
import pytz


date = "20180929"
date1 = "2018-09-29"

# Get Date
twoDayAgo = datetime.now() + timedelta(hours=8)-timedelta(days=2)

# Scrape Page
r = requests.get("https://www.immd.gov.hk/eng/stat_{}.html".format(date))
soup = BeautifulSoup(r.text, "html.parser")
tr = soup.find_all("tr")
for row in tr:
    cp = row.find("td", class_ ="")
    if cp:
        td = row.find_all("td", class_ ="hRight")
        ctrlPt_data = {
            'date': date1,
            'control_point': cp.text,
            'arrival_Hong_Kong_Residents': int(td[0].text.replace(',','')),
            'arrival_Mainland_Visitors': int(td[1].text.replace(',','')),
            'arrival_Other_Visitors': int(td[2].text.replace(',','')),
            'arrival_Total': int(td[3].text.replace(',','')),
            'departure_Hong_Kong_Residents': int(td[4].text.replace(',','')),
            'departure_Mainland_Visitors': int(td[5].text.replace(',','')),
            'departure_Other_Visitors': int(td[6].text.replace(',','')),
            'departure_Total': int(td[7].text.replace(',',''))
        }
        scraperwiki.sqlite.save(unique_keys=['date', 'control_point'], data=ctrlPt_data)
        print(ctrlPt_data)

print(date1)
