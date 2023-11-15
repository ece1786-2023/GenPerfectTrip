from django.http import JsonResponse
from django.shortcuts import render
from .functions.send import send_prompt
# Create your views here.




def index(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        print(user_input)
        hotels = send_prompt(user_input)
        return render(request, template_name="home.html", context={"hotels": hotels, "raw_user_input": user_input})
    return render(request, template_name="home.html")
