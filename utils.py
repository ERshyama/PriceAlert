import os
import sys
from selenium import webdriver
from app import db
from app.user_handler.models import User
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config


def scrape_and_email():
    email_to_name = {}
    for row in db.session.query(User):
        name = row.name
        email = row.email
        email_to_name[email] = name

    if len(email_to_name) > 0:
        prices = selenium_scraper()

        message = ''
        all_emails = [email for email in email_to_name]
        for crypto, price in prices.items():
            message = message + 'Price of ' + crypto + ' is ' + price + '\n'
        send_email(all_emails, config.EMAIL_SUBJECT, message)


def selenium_scraper():
    path1 = os.path.dirname(os.path.abspath(__file__))

    sys.path.append(path1)

    driver = webdriver.Chrome(config.webdriver_path)
    driver.maximize_window()
    driver.get(config.base_url)

    try:
        cryptos = WebDriverWait(driver, config.timeout_delay).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[class^=price-liststyles__ListCardWrapper-]')))
    except TimeoutException:
        print("Base URL not Loading")

    prices = {}
    for crypto in cryptos:
        info = crypto.text.split('\n')
        prices[info[0]] = info[3]

    driver.quit()
    return prices


def send_email(to_addresses, subject, message_text):
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()
    s.login(config.BOT_EMAIL, config.BOT_PASSWORD)
    if isinstance(to_addresses, str):
        to_addresses = [to_addresses]
    msg = MIMEMultipart()
    message = message_text
    msg['From'] = config.BOT_EMAIL
    msg['To'] = ', '.join(to_addresses)
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg
    s.close()
