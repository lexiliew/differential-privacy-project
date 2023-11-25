import requests
from bs4 import BeautifulSoup
import csv

url = 'https://columbuspolice.org/Reports/Results?from=11/1/2023&to=11/3/2023&loc=all&types=9'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the data
    table = soup.find('table', {'id': 'MainContent_gvResults'})
    
    # Check if the table is found
    if table:
        # Extract data from the table
        rows = table.find_all('tr')[1:]  # Skip the header row
        data_list = []

        for row in rows:
            columns = row.find_all('td')
            if len(columns) == 5:
                cr_number, description, victim, reported, location = [col.get_text(strip=True) for col in columns]
                # print(cr_number, description, victim, reported, location)
                data_list.append([cr_number, description, victim, reported, location])
            else:
                print(f"Skipping row with unexpected number of columns: {len(columns)}")

        # Print the data
        for data in data_list:
            print(data)

        # Save the data to a CSV file
        with open('web_scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['CRNumber', 'Description', 'Victim', 'Reported', 'Location'])
            csv_writer.writerows(data_list)

        print('Data saved to web_scraped_data.csv')
    else:
        print('Table not found on the webpage.')
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
