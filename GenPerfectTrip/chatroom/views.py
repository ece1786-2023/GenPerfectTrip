from django.shortcuts import render
from .functions.send import send_prompt
# Create your views here.




def index(request):
    hotels = send_prompt()
    return render(request, template_name="index.html", context={"hotels": hotels})

