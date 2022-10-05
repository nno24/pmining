import requests
from bs4 import BeautifulSoup

# Get the page
URL = "https://www.nordpoolgroup.com/en/Market-data1/Dayahead/Area-Prices/ALL1/Hourly/?view=table"
page = requests.get(URL)

# Save to a text file
with open("page.txt", "w") as f:
    f.write(page.text)

with open("page.txt") as f:
    soup = BeautifulSoup(f,"html.parser")
    print(soup.prettify())


