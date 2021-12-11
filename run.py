from app import app
from utils import scrape_and_email
from apscheduler.schedulers.background import BackgroundScheduler
from config import ALERT_FREQUENCY

sched = BackgroundScheduler(daemon=True)
sched.add_job(scrape_and_email, 'interval', minutes=ALERT_FREQUENCY)
sched.start()

app.run(host='0.0.0.0', port=8080, debug=True)
