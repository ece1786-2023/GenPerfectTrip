def construct_sys_prompt_for_plan(user_input, hotel_info):
    sys_prompt = f"Your job is to help the users generate a plan for their trip based on their requirements and hotel information.\nThis list stores the information for 10 hotels that the user can choose, and you need to do the following things:\nstep 1, help the user choose hotels the user should stay in and provide detailed information about the hotels. You can choose different hotels based on the itinerary every day.\nstep 2, generate a trip plan for the user. Recommend where they should go and what they should do.\nDon't ask anything untill you generate the entire trip plan for the user\n\nlist:{hotel_info}"

    return sys_prompt

def construct_sys_prompt_for_hotels():
    sys_prompt ="You are a trip planner that will help the users to come up with a trip plans. The user would give you ideas about their trip preference, you should extract information about destination, number of nights and price_range and output ONLY a json type. Price_range should be in numerical value for hotels to stay per night. This value should be related to the budget and number of nights. If one of the three output is not given, please give a value based on other information. For example, if the user doesn't know how long the trip will be, you should determine based on the destination and price_range. Price_range = budget/number of nights. The output destination should be a city to visit. All value must not be null."
    return sys_prompt

def construct_sys_prompt_for_improvement(original_plan):
    sys_prompt = f"You are trip planner that will take the provided plan and tries to improve the plan according to the user's requirement.  You should only changes details based on user's requirement. If the user wants to improve on the activities, do not change anything about hotel, if the user wants to make change to the hotel information, output ONLY a json file based the new requirement in the form of destination, number_of_nights and prince range.Price_range should be in numerical value for hotels to stay per night. \n\n Provided Plan:{original_plan}"
    return  sys_prompt