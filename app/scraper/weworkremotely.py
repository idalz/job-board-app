import requests
from bs4 import BeautifulSoup
from app.scraper.utils import extract_tags

def fetch_weworkremotely_jobs():
    url = "https://weworkremotely.com/categories/remote-programming-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    print("Status Code:", response.status_code)
    print(response.text[:1000]) 

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for li in soup.select("li.new-listing-container"):
        title = li.select_one("h4.new-listing__header__title")
        company = li.select_one("p.new-listing__company-name")
        location = li.select_one("div.new-listing__company-headquarters")
        anchor = li.select_one("a[href^='/remote-jobs/']")
        raw_tags = extract_tags(title.text.strip())
        tags = [tag.strip().lower() for tag in raw_tags if tag and tag.strip()]

        if anchor and title and company:
            job_url = f"https://weworkremotely.com{anchor['href']}"
            jobs.append({
                "title": title.text.strip(),
                "company": company.text.strip(),
                "location": location.text.strip() if location else "Remote",
                "url": job_url,
                "description": "Imported from We Work Remotely",
                "tags": tags
            })

    return jobs
