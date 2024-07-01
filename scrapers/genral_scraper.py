import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL
url = 'https://results.eci.gov.in/PcResultGenJune2024/index.htm'

# Send a GET request to the URL and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Print the title of the webpage
print(soup.title.text)

# Find the table containing the election results
table = soup.find('table', class_='table')

# Extract the table headers
header = [th.text.strip() for th in table.find('thead').find_all('th')]

# Extract the table footer (if needed)
footer = [th.text.strip() for th in table.find('tfoot').find_all('th')]

# Extract the table rows
rows = table.find('tbody').find_all('tr')

# Initialize lists to store the extracted data
party_name = []
won_seats = []
leading_seats = []
total_seats = []

# Loop through each row and extract the columns
for row in rows:
    cols = row.find_all('td')
    party_name.append(cols[0].text.strip())
    won_seats.append(cols[1].text.strip())
    leading_seats.append(cols[2].text.strip())
    total_seats.append(cols[3].text.strip())

# Create abbreviations for the party names
party_abb = [party.split()[-1] for party in party_name]

# Create a DataFrame with the extracted data
party_results = pd.DataFrame({
    'Party': party_name,
    'Party Abbreviation': party_abb,
    'Won': won_seats,
    'Leading': leading_seats,
    'Total': total_seats
})

# Save the DataFrame to a CSV file
party_results.to_csv('./data/data.csv', index=False)

print("Data has been saved to ./data/data.csv")
