from bs4 import BeautifulSoup
import pandas as pd
import requests

link = "https://3083218.youcanlearnit.net/rainieststate.html"

page_read = requests.get(link)

soup = BeautifulSoup(page_read.content)

# Get the paragraph element
louisiana = soup.select('p:last-of-type').pop().string.strip() # <== get the html string content
# Change it to a list of 2 elements [column 1 value, column 2 value]
louisiana = louisiana.split(', ')
# Reverse order so the info comes fist in list
louisiana.reverse()

# Get the table element from page
table_df = pd.read_html(link, match = 'Capital')
table_df = table_df.pop() # <== return the actual df

# Append the paragraph content at the table end
table_df.loc[len(table_df)] = louisiana
# Rename column names
table_df = table_df.rename(columns={0: 'info', 1: 'stat'})

print(table_df)