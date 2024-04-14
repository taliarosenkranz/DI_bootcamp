import requests
from bs4 import BeautifulSoup
# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
# Make a GET request to fetch the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Find the table with the complete class name
table = soup.find('table', {'class': 'wikitable sortable sticky-header sort-under mw-datatable col2left col6left'})
if table:
    # Initialize lists to store extracted data
    countries = []
    populations = []
    # Iterate over each row in the table except the header
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        if len(cells) > 1:
            # Extract country name, typically found in the second cell (adjust index as needed)
            country_name = cells[1].text.strip()
            # Extract population, typically found in the third cell (adjust index as needed)
            population = cells[2].text.strip()
            countries.append(country_name)
            populations.append(population)
    # Print the first 5 entries to check the data
    print("Countries:", countries[:5])
    print("Populations:", populations[:5])
else:
    print("Failed to find the specified table. Please check the class name or table structure.")