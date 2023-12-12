def construct_sys_prompt_for_plan(user_input, hotel_info):
    sys_prompt = f"Your job is to help the users generate a plan for their trip based on their requirements and hotel information.\nThis list stores the information for 10 hotels that the user can choose, and you need to do the following things:\nstep 1, help the user choose hotels the user should stay in and provide detailed information about the hotels. You can choose different hotels based on the itinerary every day.\nstep 2, generate a trip plan for the user. Recommend where they should go and what they should do.\nDon't ask anything untill and just generate the entire trip plan for the user\n\nlist:{hotel_info}"

    return sys_prompt

def construct_sys_prompt_for_hotels():
    sys_prompt ="You are a trip planner that will help the users to come up with a trip plan. The user would give you ideas about their trip preference, you should extract information about destination, number of nights and price_range and output ONLY a json type. Price_range should be in numerical value for hotels to stay per night. This value should be related to the budget and number of nights. If one of the three information is not given, please give a value based on other information. For example, if the user doesn't know how long the trip will be, you should determine based on the destination and price_range. Price_range = budget/number of nights. The output destination should be a city to visit. All value must not be null.Price_range should take form like 100-200"
    return sys_prompt

def construct_sys_prompt_for_improvement(original_plan):
    sys_prompt = f"You are a trip planner that will take the provided plan and try to improve the plan according to the user's requirement.  You should only change details based on user's requirement. If the user wants to improve on the activities, do not change anything about hotel, if the user wants to make change to the hotel information, output ONLY a json file based the new requirement in the form of destination, number_of_nights and prince range.Price_range should be in numerical value for hotels to stay per night. Price_range should take form like 100-200. When forming the output, you must take in account of the original plan. For example, if original hotel price is 500 and user wants cheaper hotel, it must be lower than 500.\n\n Provided Plan:{original_plan}"
    return sys_prompt

def construct_sys_prompt_for_hotel_improvement(hotel_info,original_plan):
    sys_prompt = f"You are a trip planner that will take the provided plan and try to improve the plan according to the hotel list and user input. You should not change the activities and only change the hotels to stay. \n\n Provided Plan:{original_plan} \n\n hotels list:{hotel_info}"
    return sys_prompt