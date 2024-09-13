# Stock News App

This Python application retrieves stock price data and news related to a specified company (e.g., Tesla Inc.) using the Alpha Vantage API and the News API. If the stock price change exceeds a defined threshold, the app sends relevant news headlines to the user via Twilio's WhatsApp messaging service.

## Features

- Fetch daily stock price data
- Retrieve the latest news articles related to the company
- Compare stock prices over two consecutive days
- Send a WhatsApp message via Twilio when significant stock price changes occur

## Prerequisites

To run this project locally, you will need to have:

- Python 3.x installed
- A Twilio account
- API keys from Alpha Vantage and NewsAPI.org
- The necessary Python libraries installed (listed below)

### Libraries Required:
- requests
- python-dotenv
- twilio

Install them via pip:

```bash
pip install requests python-dotenv twilio
```

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/stock-news-app.git
   cd stock-news-app
   ```

2. **Create and Set Up the .env File:**

   Create a `.env` file in the root directory of your project. This file will store sensitive information like API keys. It should look like this:

   ```
   ACCOUNT_SID=your_twilio_account_sid
   TWILIO_TOKEN=your_twilio_auth_token
   STOCK_API_KEY=your_alpha_vantage_api_key
   NEWS_API_KEY=your_news_api_key
   ```

   Note: Be sure to replace the placeholder values with your actual keys and phone numbers.

3. **Run the App:**

   To run the stock news app, simply execute the following command in the terminal:

   ```bash
   python main.py
   ```

   The script will:
   - Fetch the stock data for the specified company
   - Retrieve the most recent news headlines if the stock price change exceeds a threshold (e.g., 5%)
   - Send a WhatsApp message with the stock price change, headlines, and a brief summary
