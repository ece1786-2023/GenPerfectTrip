def construct_sys_prompt_for_plan(user_input, hotel_info):
    sys_prompt = f"Your job is to help the users generate a plan for their trip based on their requirements and hotel information.\nThis list stores the information for 10 hotels that the user can choose, and you need to do the following things:\nstep 1, help the user choose hotels the user should stay in and provide detailed information about the hotels. You can choose different hotels based on the itinerary every day.\nstep 2, generate a trip plan for the user. Recommend where they should go and what they should do.\nDon't ask anything untill you generate the entire trip plan for the user\n\nlist:{hotel_info}"

    return sys_prompt

