from django.shortcuts import render
from openai import OpenAI
from .static.test import OUTPUT
from .functions.prompt_constructor import construct_sys_prompt_for_plan, construct_sys_prompt_for_hotels
from .functions.send import get_hotels_by_req, send_prompt
from django.http import JsonResponse


def chat(request):
    context = {
        "raw_user_input": "",
    }
    if request.method == 'GET':
        user_input = request.GET.get("user_input")
        context = {
            "raw_user_input": user_input,
        }
    return render(request, template_name='chat.html', context=context)

def generate(request):
    client = OpenAI()
    user_input = request.GET.get("user_input")

    sys_prompt_1 = construct_sys_prompt_for_hotels()
    req = send_prompt(client, sys_prompt_1, user_input, t=1, max_tokens=200)
    hotels = get_hotels_by_req(req)
    sys_prompt_2 = construct_sys_prompt_for_plan(user_input, hotels)
    output = send_prompt(client, sys_prompt_2, user_input, t=0.5, max_tokens=1500)
    return JsonResponse({'data': output})

def improve(request):
    client = OpenAI()
    user_input = request.GET.get("user_input")
    hotel_info = ""
    sys_prompt = ""
    output = send_prompt(client, sys_prompt, user_input, t=0.5, max_tokens=10)
    return JsonResponse({'data': output})


def test(request):
    context = {
        "raw_user_input": "",
    }
    if request.method == 'GET':
        user_input = request.GET.get("user_input")
        context = {
            "raw_user_input": user_input,
        }
    return render(request, template_name='test.html', context=context)


def test_generate(request):
    user_input = request.GET.get("user_input")
    output = user_input+OUTPUT
    print(output)
    return JsonResponse({'data': output})


def test_improve(request):
    user_input = request.GET.get("user_input")
    output = "improve"+user_input+OUTPUT
    print(output)
    return JsonResponse({'data': output})


def hotels(request):
    context = {
        "raw_user_input": "",
    }
    if request.method == 'GET':
        user_input = request.GET.get("user_input")
        context = {
            "raw_user_input": user_input,
        }
    return render(request, template_name='hotels.html', context=context)


def hotels_generate(request):
    user_input = request.GET.get("user_input")
    output = get_hotels_by_req(user_input)
    print(output)
    return JsonResponse({'data': output})


def hotels_improve(request):
    user_input = request.GET.get("user_input")
    output = "improve"+user_input+OUTPUT
    print(output)
    return JsonResponse({'data': output})



