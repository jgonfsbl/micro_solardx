import urllib3
import json
from datetime import datetime, timezone
from bs4 import BeautifulSoup


HTTP = urllib3.PoolManager()
URL = 'http://dk0wcy.de/magnetogram/'

RESPONSE = HTTP.request('GET', URL)
SOUP = BeautifulSoup(RESPONSE.data, features="html.parser")
TAG = SOUP.find_all("b")

exitformat = {
    'timestamp':
        datetime.now(timezone.utc).strftime("%Y%m%dT%H:%M:%SUTC"),
    'dx-data': {
        'sfi': TAG[8].text.strip(),
        'ssn': TAG[6].text.strip(),
        'aurora': TAG[7].text.strip(),
        'a-index': TAG[3].text.strip(),
        'k-index': TAG[4].text.strip(),
        'solar_activity': TAG[2].text.strip(),
        'magnetic_field': TAG[5].text.strip()
    }
}

print()
print(json.dumps(exitformat))
