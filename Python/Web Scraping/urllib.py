import urllib.request

url = 'https://docs.python.org/3/library/concurrent.futures.html'

def load_url(url, timeout):
     with urllib.request.urlopen(url, timeout=timeout) as connection:
         return connection.read()

load_url(url, timeout=5)
