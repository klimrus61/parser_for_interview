import requests
from bs4 import BeautifulSoup

def main():
    host = 'https://propertyhub.in.th'
    url = 'https://propertyhub.in.th/en/condo/bts-national-stadium'

    page = requests.get(url)
    announcements = []
    soup = BeautifulSoup(page.text, 'html.parser')
    announcements = soup.find_all('div', attrs={'class': 'sc-8har3e-0 kTvRSH'})
    for i, an in enumerate(announcements):
        links = an.find_all('a')
        print('-------------------------')
        title = an.find('p', attrs={'class': 'elaovb-3 izRiRZ'}).text
        description = an.find('p', attrs={'class': 'elaovb-4 izZFwi'}).text
        print(f"announcement numer - {i+1}")
        print('title: ' + title)
        print('description: ' + description)
        for num, link in enumerate(links):
            print(f'link number - {num+1}: '+host+link.get('href'))

if __name__ == "__main__":
    main()