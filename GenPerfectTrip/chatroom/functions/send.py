from .hotel_data_processing import scrap_hotels_by_requirment
import json

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
    print(requirement)
    requirement = json.loads(requirement)
    hotels = scrap_hotels_by_requirment(requirement)
    return hotels