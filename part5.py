#wikiscrap/parse
import pandas as pd
import urllib.request
import bs4 as bs
# import lxml
url = 'https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015'
table = pd.read_html(url)
table = table[0]
# table[0].to_csv("testParse3.csv")
# f=pd.read_csv('testParse3.csv')
# below code defines the columns
col = ['Rank', 'Player', 'Team', 'Points', 'Games', 'Avg']
file = table[col]
file.to_csv('testParse3.csv', index=False)
#Version2
link = 'https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015'
source = urllib.request.urlopen(link).read()
soup = bs.BeautifulSoup(source, 'lxml')
# print(soup.title.text)
table = soup.find('table')
table_rows = table.find_all('tr')
x = (len(table.findAll('tr')))
count = 0
with open('fantasypros_parse2015.csv', 'a') as f:
    while count<x:
        for tr in table_rows[1:x]:
            td = tr.find_all('td')
            row = [i.text for i in td]
            print(row)
            count = count +1
            row = str(row)
            f.write('\n')
            f.write(row)