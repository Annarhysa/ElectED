# ElectED

This project implements a web-based dashboard using Dash and Plotly for visualizing election results data scraped from the Election Commission of India website.

## Features

- **Total Seats Won by Each Party:** Bar chart displaying the total number of seats won by each political party in the election.
- **Distribution of Total Seats Won:** Histogram showing the distribution of total seats won across all parties.
- **Total Seats Won by Top 5 Parties:** Bar chart highlighting the total seats won by the top 5 political parties.
- **Seats Distribution Among Top 20 Parties:** Pie chart depicting the distribution of seats among the top 20 political parties.

## Data Source

The election results data is scraped from the [Election Commission of India website](https://results.eci.gov.in/). The scraping process involves:

1. **Fetching Data:** Using the `requests` library to send HTTP GET requests to the website and retrieve the HTML content.
   
2. **Parsing HTML:** Utilizing `BeautifulSoup` for parsing the HTML content and navigating through the DOM structure to locate and extract relevant data tables.

3. **Data Extraction:** Extracting specific data fields such as party names, abbreviations, number of seats won, leading seats, and total seats from the HTML tables.

4. **Data Cleaning:** Cleaning and formatting the extracted data to ensure consistency and prepare it for further analysis and visualization.

## Dashboard Setup

The dashboard is built using Dash, a Python framework for building analytical web applications. Plotly Express is used for creating interactive and visually appealing plots and charts.

### Requirements

Ensure you have the following Python libraries installed:

```bash
pip install dash dash-bootstrap-components pandas plotly requests beautifulsoup4
```

## Running the Dashboard

To run the dashboard locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repository.git
   cd your-repository
   ```

2. To run the dashboard locally:

    ```bash
    python app.py
    ```

## Output

https://github.com/Annarhysa/ElectED/assets/91026126/48ddef68-ed02-431b-a0eb-29d3a8081edd


## Key Insights from the scrapped data

1. **Dominance of BJP:** BJP has 240 seats, more than double of INC's 99 seats.
2. **Regional Party Performance:** SP and AITC have strong regional influence with 37 and 29 seats respectively.
3. **Southern Influence:** DMK and TDP show political significance with 22 and 16 seats each.
4. **Emergence of New Alliances:** Shiv Sena split: SHSUBT has 9 seats, SHS has 7 seats.
5. **Smaller Parties Making Impact:** LJPRV and NCPSP have 5 and 8 seats, influencing outcomes despite limited reach.
6. **Communist Parties Holding Ground:** CPI(M) and CPI have 4 and 2 seats, maintaining left-wing presence.
7. **Independent Candidates:** Independent candidates secured 7 seats, indicating voter discontent with traditional parties.
8. **Variety of Political Ideologies:** Diverse landscape with regional, left-wing, right-wing, and caste-based parties.
9. **Single Seat Parties:** SKM and BHRTADVSIP each won one seat, showing localized political movements.
10. **Significance of Caste and Regional Parties:** RJD and RLD won 4 and 2 seats, highlighting the importance of caste dynamics.

PDF File of Report: 

