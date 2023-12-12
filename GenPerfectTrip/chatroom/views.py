from django.shortcuts import render
from openai import OpenAI
from .functions.prompt_constructor import construct_sys_prompt_for_plan, construct_sys_prompt_for_hotels,construct_sys_prompt_for_improvement,construct_sys_prompt_for_hotel_improvement
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
    try:
        client = OpenAI()
        user_input = request.GET.get("user_input")
        sys_prompt_1 = construct_sys_prompt_for_hotels()
        req = send_prompt(client, sys_prompt_1, user_input, t=1, max_tokens=200)
        hotels = get_hotels_by_req(req)
        sys_prompt_2 = construct_sys_prompt_for_plan(user_input, hotels)
        output = send_prompt(client, sys_prompt_2, user_input, t=0.5, max_tokens=1500)
        return JsonResponse({'data': output})
    except:
        output = "We are not able to generate the plan based on your input, please be more specific."
        return JsonResponse({'data': output})



def improve(request):
    try:
        client = OpenAI()
        user_input = request.POST.get("user_input")
        original_plan = request.POST.get("original_plan")
        print("original_plan---->", original_plan)
        sys_prompt_1 = construct_sys_prompt_for_improvement(original_plan)
        # two cases here for hotel or activity improvement
        # hotel improvement needs to go through web-scraping and plan generation
        # activity improvement can directly output improved plan
        check = send_prompt(client, sys_prompt_1, user_input, t=1, max_tokens=1500)
        print(check)
        if len(check) < 200:
            hotels = get_hotels_by_req(check)
            sys_prompt_2 = construct_sys_prompt_for_hotel_improvement(hotels, original_plan)
            print(sys_prompt_2)
            output = send_prompt(client, sys_prompt_2, user_input, t=0.5, max_tokens=1500)
            return JsonResponse({'data': output})
        else:
            output = check
            return JsonResponse({'data': output})
    except:
        output = "We are not able to improve the plan based on your input, please be more specific."
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
    output = user_input
    print(output)
    return JsonResponse({'data': output})


def test_improve(request):
    user_input = request.GET.get("user_input")
    original_plan = request.GET.get("original_plan")
    output = "improve"+user_input+original_plan
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



