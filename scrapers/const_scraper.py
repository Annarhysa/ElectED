import requests
from bs4 import BeautifulSoup
import csv
import os

base_url = "https://results.eci.gov.in/PcResultGenJune2024/Constituencywise"

states = ["U0" + str(u) for u in range(1, 15)] + ["S0" + str(s) if s < 10 else "S" + str(s) for s in range(1, 35)]

results = []

for state in states:
    for constituency_code in range(1, 85):
        constituency_str = str(constituency_code)
        url = f"{base_url}{state}{constituency_str}.htm"
        response = requests.get(url)
        if response.status_code == 404:
            break
        
        response_text = response.text
        soup = BeautifulSoup(response_text, 'html.parser')

        table = soup.find('table')  # Find the table element

        # scrape table head
        headers = [th.text.strip() for th in table.find_all('th')]

        # table data
        data = []
        for tr in table.find_all('tr'):
            row = [td.text.strip() for td in tr.find_all('td')]
            if row:
                data.append(row)

        # data to CSV file
        with open('data/constituency.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data)

        # finding state name and constituency/district name
        spans = soup.find_all('span')
        constituency_names = []
        for span in spans:
            constituency_name = span.get_text(strip=True).split('(')[0].strip()
            constituency_names.append(constituency_name) 

        def extract_constituency(constituency_names):
            for item in constituency_names:
                if item:  # check if the string is not empty
                    # split by ' - ' and take the second part, then remove whitespace
                    constituency = item.split(' - ')[1].strip() if ' - ' in item else item
                    return constituency 
        
        # cleaning state names and constituency names
        constituency_n = extract_constituency(constituency_names)
        state_name = soup.find('strong').get_text(strip=True).strip('()')
        print("State:", state_name)
        print("Constituency:", constituency_n)

        # folder for each state if it doesn't exist
        state_folder = f"data/{state_name}"
        if not os.path.exists(state_folder):
            os.makedirs(state_folder)

        # unique filename for each state
        filename = f"{state_name}_{constituency_n}_{constituency_code}.csv"

        # data to CSV file in the state folder
        with open(os.path.join(state_folder, filename), 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data)
