from scraper.remoteok import fetch_remoteok_jobs
from scraper.weworkremotely import fetch_weworkremotely_jobs

for job in fetch_weworkremotely_jobs():
    print(job)