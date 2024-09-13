import requests
import time
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Function to upload de api credentials
load_dotenv()

# Send the news to the phone
def send_news(i):
    account_sid = os.getenv('ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'''
        TSLA: 🔺5% \n
        {data_news_list[i]["title"]+ "\n"}
        {data_news_list[i]["description"]+ "\n"}
        ''',
        from_="whatsapp:+14155238886",
        to="whatsapp:+573115839595",
    )

    print(message.body)

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY_STOCK = os.getenv('API_KEY_STOCK')
API_KEY_NEWS = os.getenv('API_KEY_NEWS')

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Get the current date for the news api
date_now = time.strftime("%Y-%m-%d")

# URL APIS
url = f'{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&interval=5min&apikey={API_KEY_STOCK}'
url_news = f'https://newsapi.org/v2/everything?q=tesla&from={date_now}&sortBy=popularity&apiKey={API_KEY_NEWS}'

# Parsing news data
rq_news = requests.get(url_news)
data_news = rq_news.json()

# Parsing stock data
rq = requests.get(url)
data = rq.json()

# Get the first 3 news pieces for the COMPANY_NAME
data_news_list = data_news['articles'][0:3]
data_list = [value for (key, value) in data['Time Series (Daily)'].items()]

# Get the last two days data
yesterday_data = data_list[0]["4. close"]
day_before_yesterday_data = data_list[1]["4. close"]

# Calculate the difference between the two days
difference = abs((float(yesterday_data) - float(day_before_yesterday_data))/float(yesterday_data)*100)

# Printing the first three news after the difference is greater than 5%
if difference > 5:
    for i in range(3):
        send_news(i)
else:
    print("No news to send")