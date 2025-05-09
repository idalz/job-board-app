import requests
from bs4 import BeautifulSoup
from app.scraper.utils import extract_tags

def fetch_remoteok_jobs():
    url = "https://remoteok.com/remote-dev-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for row in soup.find_all("tr", class_="job"):
        title = row.find("h2", itemprop="title")
        company = row.find("h3", itemprop="name")
        location = row.find("div", class_="location")
        link = row.get("data-href")
        
        if title and company and link:
            raw_tags = extract_tags(title.text.strip())
            tags = [tag.strip().lower() for tag in raw_tags if tag and tag.strip()]

            jobs.append({
                "title": title.text.strip(),
                "company": company.text.strip(),
                "location": location.text.strip() if location else "Remote",
                "url": f"https://remoteok.com{link}",
                "description": "Imported from RemoteOK",
                "tags": tags
            })

    return jobs
