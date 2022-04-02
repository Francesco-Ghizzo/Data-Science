# Retrieve .csv from the Web and assign its contents to a pandas dataframe

import urllib
import pandas as pd

url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

request = urllib.request.Request(url)
urlopen = urllib.request.urlopen(request)

iris = pd.read_csv(urlopen, sep=',', decimal='.')


# Using context managers:

import urllib
import pandas as pd

url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

try:
    request = urllib.request.Request(url)
    urlopen = urllib.request.urlopen(request)
except Exception as e:
    print(f"Error: {e}")    
finally:
    iris = pd.read_csv(urlopen, sep=',', decimal='.')