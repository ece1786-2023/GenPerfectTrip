from .hotel_data_processing import scrap_hotels_by_requirment
import json

def send_prompt(client, system_prompt, prompt, t, max_tokens):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=t,
        max_tokens=max_tokens,
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