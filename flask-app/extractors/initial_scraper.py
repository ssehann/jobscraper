# conda activate webscraper
# make sure interpreter is set to webscraper

import requests
from bs4 import BeautifulSoup

# 1. initialization
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
response = requests.get(url)
print(response.content)
soup = BeautifulSoup(response.content, "html.parser")
# params: content data, type of data we're giving

# run code -> go back to website -> inspect mode -> identify parts of page you want to scrape

# 2. inspection & get data
jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
# since class is a reserved word in python, use class_ for html class
# find() only finds the first instance, so use find_all to get all listings
# exclude first and last <li> since they're not jobs
print(jobs)

all_jobs = []
for job in jobs:
    title = job.find("span", class_="title").text
    if (job.find("span", class_="region")):
        company, position, region = job.find_all("span", class_="company")
        company = company.text
        position = position.text
        region = region.text
    else:
        company, position = job.find_all("span", class_="company")
        company = company.text
        position = position.text

    url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
    # in each job listing, there are two <a> tags with href (url link)
    # so find the first one we want to skip (tooltip) and get the next href

    job_data = {
        "title": title,
        "company": company,
        "position": position,
        "region": region,
        "url": f"https://weworkremotely.com{url}"
    }
    all_jobs.append(job_data)
