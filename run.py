from app import app
from utils import scrape_and_email
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler(daemon=True)
sched.add_job(scrape_and_email, 'interval', minutes=1)
sched.start()

app.run(host='0.0.0.0', port=8080, debug=True)
