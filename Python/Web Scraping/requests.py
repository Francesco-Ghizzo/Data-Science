import requests

import time

def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

url = "https://www.python.org/"

with requests.Session() as session:
    download_site(url, session)

# Read 49837 from https://www.python.org/

 with requests.Session() as session:
     start_time = time.time()
     download_site(url, session)
     duration = time.time() - start_time
     print(f"Downloaded in {duration} seconds")

# Read 49837 from https://www.python.org/
# Downloaded in 0.3716869354248047 seconds