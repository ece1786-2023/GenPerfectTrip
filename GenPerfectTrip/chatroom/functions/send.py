from .hotel_data_processing import scrap_hotels_by_requirment


def send_prompt(client, prompt):
    response = client.chat.completions.create(
      model="gpt-4",
      messages=[
        {
          "role": "user",
          "content": prompt
        }
      ],
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    output = response.choices[0].message.content.strip('"')
    print(output)
    return output

def send_prompt_for_hotels(requirement):
    requirement = {
        "destination": "University of Toronto",
        "no_adults": "1",
        "no_children": "0",
        "no_rooms": "1",
        "checkin": "2023-12-10",
        "checkout": "2023-12-11",
        #price: sort by price (low to high)
        #class: sort by rating(high to low)
        #class-acs: sort by rating(low to high)
        "order": "price",
        "price_range": "100-200",
        #3000: less than 3km
        "dis": "3000"
    }
    hotels = scrap_hotels_by_requirment(requirement)
    return hotels