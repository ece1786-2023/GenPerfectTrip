from django.shortcuts import render
from openai import OpenAI
from.functions.prompt_constructor import construct_sys_prompt_for_plan
from .functions.send import send_prompt_for_hotels, send_prompt


def hotels(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        hotels = send_prompt_for_hotels(user_input)
        return render(request, template_name="home.html", context={"outputs": hotels, "raw_user_input": user_input})
    return render(request, template_name="home.html")

def index(request):
    if request.method == 'POST':
        client = OpenAI()
        user_input = request.POST.get('user_input')
        print("user_input:", user_input)

        hotel_info = "[{'name': 'Samesun Toronto', 'location': 'Downtown Toronto, Toronto', 'price': 'CAD\xa053', 'rating': '7.4', 'diatance to the destination': '1.8 km from centre'}, {'name': 'Residence Inn by Soho', 'location': 'Downtown Toronto, Toronto', 'price': 'CAD\xa089', 'rating': '8.0', 'diatance to the destination': '1.1 km from centre'}, {'name': 'Three BR Condo step to CN tower Rogers Center with Free parking', 'location': 'Downtown Toronto, Toronto', 'price': 'CAD\xa099', 'rating': '6.8', 'diatance to the destination': '1.9 km from centre'}, {'name': 'Kensington Market House', 'location': 'Chinatown, Toronto', 'price': 'CAD\xa0100', 'rating': '7.0', 'diatance to the destination': '1.9 km from centre'}, {'name': 'Royal Oak Inn', 'location': 'Downtown Toronto, Toronto', 'price': 'CAD\xa097', 'rating': '4.9', 'diatance to the destination': '1.3 km from centre'}, {'name': 'Large private room close to Finch', 'location': 'North York, Toronto', 'price': 'CAD\xa083', 'rating': '9.5', 'diatance to the destination': '15.4 km from centre'}, {'name': 'Spacious private room near Finch station', 'location': 'North York, Toronto', 'price': 'CAD\xa097', 'rating': '9.1', 'diatance to the destination': '15.4 km from centre'}, {'name': 'Time Capsule - Value Inn', 'location': 'Toronto', 'price': 'CAD\xa073', 'rating': '5.0', 'diatance to the destination': '5.1 km from centre'}]"
        sys_prompt = construct_sys_prompt_for_plan(user_input, hotel_info)
        completion = send_prompt(client, sys_prompt, user_input, t=0.5, max_tokens=1500)
        
        return render(request, template_name="chat.html", context={"outputs": completion, "raw_user_input": user_input})
    return render(request, template_name="chat.html")
