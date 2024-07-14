from bs4 import BeautifulSoup
import requests
import pandas

url = "https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html')

table = soup.find('table',class_="sortable plainrowheaders wikitable")

headers = table.find_all('th')

headers_name = [data.text.strip() for data in headers][:7]

data_frame = pandas.DataFrame(columns=headers_name)

data_in_rows = table.find_all('tr')

for row in data_in_rows[1:-1]:
    th_data = row.find_all('th')[0].find('a').contents[0]
    data = row.find_all('td')[:-1]
    individual_data = [item.text.strip() for item in data]
    individual_data.insert(0,th_data)

    length = len(data_frame)
    data_frame.loc[length] = individual_data

print(data_frame)

data_frame.to_csv(r"Path for saving file",index=False)
