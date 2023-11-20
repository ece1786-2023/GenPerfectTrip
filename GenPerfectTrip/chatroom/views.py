from django.shortcuts import render
from openai import OpenAI

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
        print(user_input)

        # completion = send_prompt(client, prompt=user_input)
        completion = "This is some placeholder content for the scrollspy page. Note that as you scroll down the page, the appropriate navigation link is highlighted. It's repeated throughout the component example. We keep adding some more example copy here to emphasize the scrolling and highlighting."
        
        return render(request, template_name="chat.html", context={"outputs": completion, "raw_user_input": user_input})
    return render(request, template_name="chat.html")
