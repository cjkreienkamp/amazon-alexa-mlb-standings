import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def func():
    url1 = 'https://howmanydaysuntil.center/mlb-opening-day/'
    html1 = urllib.request.urlopen(url1).read()
    soup1 = BeautifulSoup(html1, 'html.parser')

    dayhour = soup1.find('span', class_='dhcountdown').text
    dayhour = dayhour.split()
    days = int(dayhour[0])
    hours = int(dayhour[2])
    if hours > 0:
        days = days + 1
    return days
