import datetime
import requests
from bs4 import BeautifulSoup

def scrap_hotels_by_requirment(requirements):
    url = form_url(requirements)
    hotels = get_hotel_info(url)
    return hotels

def form_url(requirement):
    BOOK_URL = "https://www.booking.com/searchresults.en-gb.html?"
    url = BOOK_URL
    number_of_night = int(requirement.get("number_of_nights"))
    destination = requirement.get("destination")
    group_adults = requirement.get("no_adults", 1)
    group_children = requirement.get("no_children", 0)
    no_rooms = requirement.get("no_rooms", 1)
    check_in = requirement.get("checkin", str(datetime.date.today()+ datetime.timedelta(days=1)))
    check_out = requirement.get("checkout", str(datetime.date.today() + datetime.timedelta(days=number_of_night+1)))
    order = requirement.get("order")
    price_range = requirement.get("price_range")
    distance = requirement.get("dis")

    if destination is not None:
        destination = destination.split()
        destination = "+".join(destination)
        url += f"ss={destination}"

    url += f"&group_adults={group_adults}" + f"&group_adults={group_children}" + f"&no_rooms={no_rooms}" + f"&checkin={check_in}" + f"&checkout={check_out}"

    if price_range is not None or distance is not None:
        url += "&nflt="
        if distance is not None:
            url += f"distance%3D{distance}%3B"
        if price_range is not None:
            url += f"price%3DCAD-{price_range}-1"

    if order is not None:
        url += f"&order={order}"

    print(url)
    return url

def get_hotel_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        "Accept": "*/*",
        "Accept-Encoding": "*",
        'Accept-Language': 'en-US, en;q=0.5',
        "Connection": "keep-alive"
    }
    response = requests.get(url, headers=headers)
    text = None
    if response.status_code == 200:
        text = response.text

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    # parse html
    soup = BeautifulSoup(text, "html.parser")
    # Find all the hotel elements in the HTML document
    hotel_list = soup.findAll("div", {'data-testid': 'property-card'})

    hotels_data = []
    count = 0
    for hotel in hotel_list:
        count += 1
        if count > 8:
            break
        # Extract the hotel name
        name_element = hotel.find('div', {'data-testid': 'title'})
        name = None
        if name_element is not None:
            name = name_element.text.strip()

        # Extract the hotel location
        location_element = hotel.find('span', {'data-testid': 'address'})
        location = None
        if location_element is not None:
            location = location_element.text.strip()

        # Extract the hotel price
        price_element = hotel.find('span', {'data-testid': 'price-and-discounted-price'})
        price = None
        if price_element is not None:
            price = price_element.text.strip()

        # Extract the hotel rating
        rating_element = hotel.find('div', {'class': 'a3b8729ab1 d86cee9b25'})
        rating = None
        if rating_element is not  None:
            rating = rating_element.text.strip()

        #Extract the distance to the destination
        distance_element = hotel.find("span", {"data-testid": 'distance'})
        distance = None
        if distance_element is not None:
            distance = distance_element.text.strip()

        #store hotels info
        hotels_data.append({
            'name': name,
            'location': location,
            'price': price,
            'rating': rating,
            'diatance to the destination': distance
        })
    return hotels_data

def main():
    requirement = {
        "destination": "University of Toronto",
        "no_adults": "1",
        "no_children": "0",
        "no_rooms": "1",
        # "checkin": "2023-12-10",
        # "checkout": "2023-12-11",
        #price: sort by price (low to high)
        #class: sort by rating(high to low)
        #class-acs: sort by rating(low to high)
        "order": "price",
        "price_range": "100-200",
        #3000: less than 3km
        "dis": "3000" 
    }
    hotel_list = scrap_hotels_by_requirment(requirement)
    for hotel in hotel_list:
        print(hotel)



if __name__ == "__main__":
    main()