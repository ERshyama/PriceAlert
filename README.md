# PriceAlert
Sign up to receive updates on popular Crypto prices directly on your email

## Technologies Used

* This app is setup using the Flask microservice architecture
* SQLAlchemy is used to persist of registered users using sqllite database
* A minimal FE is setup using HTML and Flask WT Forms
* A BackgroudScheduler is set up using apscheduler to run the scraper and email service at regular intervals (as defined in config) 
* Python Selenium is used to scrape crypto prices from Coindesk using Chromedriver
* Emails are sent to all registered users using python SMTP protocol

## Setup & How to Run:

* Configure to sender email and alert frequency in config.py
* Configure your email for SMTP - steps in gmail are as follows:
  * Go to Manage your Google Account
  * Click 'Security' on the left side panel
  * Turn on Less secure app access  
* Install Requirements: pip install -r requirements.txt
* Run the Flask Server: python run.py
* Add & Remove users by visiting the localhost url
* For testing and running the selenium price scraper independently run: python price_scraper.py
