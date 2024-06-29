import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://results.eci.gov.in/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Print the title of the webpage
print(soup.title.text)

# Extract other data as needed using BeautifulSoup's methods
# Example: Find all <a> tags
for link in soup.find_all('a'):
    print(link.get('href'))


url="https://results.eci.gov.in/PcResultGenJune2024/index.htm"

page = requests.get(url)
s = BeautifulSoup(page.text,"html.parser")

table = s.find('table', class_='table')

head = s.find('thead')
headr = head.find_all('th')
header = [th.text.strip() for th in headr]

foot = table.find('tfoot')
footr = foot.find_all('th')
footer = [th.text.strip() for th in footr]

table = s.find("tbody")
rows = table.find_all("tr")

party_name = []
won_seats = []
leading_seats = []
total_seats = []

row = rows[0]
tds = row.find_all("td")
print("-",tds[0].text.strip(),"-")
print("-",tds[1].text.strip(),"-")
print("-",tds[2].text.strip(),"-")
print("-",tds[3].text.strip(),"-")

row.find("a")['href']

for row in rows:
    cols = row.find_all('td')
    party_name.append(cols[0].text.strip())
    won_seats.append(cols[1].text.strip())
    leading_seats.append(cols[2].text.strip())
    total_seats.append(cols[3].text.strip())   

party_abb=[party.split()[-1] for party in party_name]

party_results = pd.DataFrame({
    'Party': party_name,
    'Party Abbreviation': party_abb,
    'Won': won_seats,
    'Leading': leading_seats,
    'Total': total_seats
})

party_results.to_csv('./data/data.csv', index = False)