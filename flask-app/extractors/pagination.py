# conda activate webscraper
# make sure interpreter is set to webscraper

import requests
from bs4 import BeautifulSoup

all_jobs = []
def scrape_page(url):
    print(f"Scraping {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

    for job in jobs:
        title = job.find("span", class_="title").text
        if (job.find("span", class_="region")):
            company, position, region = job.find_all("span", class_="company")
            company = company.text
            region = region.text
        else:
            company, position = job.find_all("span", class_="company")
            company = company.text

        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]

        job_data = {
            "title": title,
            "company": company,
            "region": region,
            "salary": "Not specified", # placeholder for consistency with other databases
            "url": f"https://weworkremotely.com{url}"
        }
        all_jobs.append(job_data)

def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    buttons = soup.find("div", class_="pagination").find_all("span", class_="page")
    return len(buttons)

def get_wwr_jobs():
    total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs#job-listings")

    for x in range(total_pages):
        page_num = x + 1
        url = f"https://weworkremotely.com/remote-full-time-jobs?page={page_num}"
        scrape_page(url)
    return all_jobs
