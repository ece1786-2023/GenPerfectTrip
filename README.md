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
## Run the program

to run the program, you need to direct to the third GenPerfectTrip directory, where you can see `manage.py`, and then run the following command:

```bash
python manage.py runserver
```