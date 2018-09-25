import scraperwiki

import requests
from bs4 import BeautifulSoup
import re

from datetime import datetime
from datetime import timedelta
import pytz


# Get Date
hkt = pytz.timezone('Asia/Hong_Kong')
ytd = datetime.now().replace(tzinfo=hkt)-timedelta(days=2)
ytdYmd = ytd.strftime("%Y%m%d")


# Scrape Page
r = requests.get("https://www.immd.gov.hk/eng/stat_{}.html".format(ytdYmd))
soup = BeautifulSoup(r.text, "html.parser")
tr = soup.find_all("tr", class_="")
for row in tr[1:]:
    td = row.find_all("td")
    ctrlPt_data = {
        'date_control_point': "{}-{}".format(ytd.strftime("%Y-%m-%d"),td[0].text),
        'arrival_Hong_Kong_Residents': int(td[1].text.replace(',','')),
        'arrival_Mainland_Visitors': int(td[2].text.replace(',','')),
        'arrival_Other_Visitors': int(td[3].text.replace(',','')),
        'arrival_Total': int(td[4].text.replace(',','')),
        'departure_Hong_Kong_Residents': int(td[5].text.replace(',','')),
        'departure_Mainland_Visitors': int(td[6].text.replace(',','')),
        'departure_Other_Visitors': int(td[7].text.replace(',','')),
        'departure_Total': int(td[8].text.replace(',',''))
    }
    print(ctrlPt_data)
print(ytdYmd)
scraperwiki.sqlite.save(unique_keys=['date_control_point'], data=ctrlPt_data)