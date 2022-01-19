import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.w3schools.com/html/html_tables.asp"	
page = requests.get(url)					# get page from a given url

encoding = page.encoding
decode = page.content.decode(encoding)				# decode page content in non human readable form 

soup = BeautifulSoup(page.text, 'lxml')				# format page in a human readable form

table = pd.read_html(decode, attrs = {'id': 'customers'})	# read table from html using pandas. Select table using id
table = table[0]						# table is a list. Turn table into a pandas DataFrame

