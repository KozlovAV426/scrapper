from datetime import datetime

import requests
from bs4 import BeautifulSoup

from entities.Flight import Flight
from repository import Repository

FLIGHT_TIME_POSTFIX = 'в пути'
URL = "https://www.aviasales.ru/search/MOW1001AUH1"
page = requests.get(URL)

def extract_airport(elems):
    airports = []
    for item in elems:
        if item.text.strip().isalpha() and item.text.strip().isupper():
            airports.append(item.text.strip())
        if len(airports) == 2:
            break
    return airports

def create_time(str_time):
    return datetime.strptime(datetime.now().strftime('%Y:%m:%d') + ' ' + str_time, '%Y:%m:%d %H:%M')

def extract_times(elems):
    times = []
    for item in elems:
        if ':' in item.text.strip():
            times.append(item.text.strip())
        if len(times) == 2:
            break
    return times


def extract_flight_time(elems):
    for item in elems:
        if FLIGHT_TIME_POSTFIX in item.text.strip():
            return item.text.strip().split(" ")[0][:-1]

def extract_price(s):
    return int(''.join(s.split(' ')))


def main():
    repository = Repository("postgresql+psycopg2://root:root@localhost/db")
    with open('1.html', 'r') as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        tickets = soup.find_all('div', {'class': 'product-list__item fade-enter-done'})
        for element in tickets:
            price = extract_price(element.find_next('span', {'data-test-id': 'price'}).text[:-1])
            elems = element.find_all_next('div', {'data-test-id': 'text'})
            from_airport, to_airport = extract_airport(elems)
            depart_time, arrival_time = extract_times(elems)
            flight_time = int(extract_flight_time(elems).split(',')[0])

            repository.insert(
                Flight(departure_airport=from_airport, arrival_airport=to_airport,
                                     departure_time=create_time(depart_time), arrival_time=create_time(arrival_time),
                                     price=price, flight_time=flight_time)
                              )


if __name__ == '__main__':
    main()
