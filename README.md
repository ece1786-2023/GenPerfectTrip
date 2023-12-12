# GenPerfectTrip

GenPerfectTrip is designed to revolutionize the way we plan for our trip.
This product is based on `GPT-4` which aims to help you construct a trip plan based on your input and requirements, making it easier and more efficient than ever before. During the plan-making process, the product will use the data online like the information about the hotels and attractions to generate the plan, so it will implement some web scraping to fetch the up-to-date data to generate the output.

## Prerequisites
Before you begin, ensure you have the following packages

- beautifulsoup4
- lxml
- requests 
- Django
- django-bootstrap-v5
- OpenAI 

## Installation

Use the following command to install the required packages:

```bash
pip install requests beautifulsoup4
pip install lxml
python -m pip install Django
pip install django-bootstrap-v5
pip install --upgrade openai
```

You also need to set up your APIKey. For more details, please visit: [OpenAI Official Documentation](https://platform.openai.com/docs/quickstart?context=python)
## Run the program

to run the program, you need to direct to the second GenPerfectTrip directory, where you can see `manage.py`, and then run the following command:
```bash
python manage.py runserver
```
## Instructions

After running the program and clicking the link displayed in the terminal, a webpage will appear:
![interface](/images/interface.png)
On the left-hand side, you'll find a textarea where you can enter your trip preferences. Upon clicking the **generate plan** button, a preliminary plan will be presented on the right-hand side.
![result1](/images/result1.png)
The hotels provided in the plan are real and atcually avaliable on BOOKING.com:
![hotels](/images/hotels1.png)
Once you have the preliminary plan, the **improve plan** button will become available. You can modify your preferences, add more details, and then click the button to obtain an improved version of the plan.
![result2](/images/result2.png)