# scraper for dynamic websites, using playwright

from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

def get_content(keyword):
    p = sync_playwright().start()

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.wanted.co.kr/")
    # time.sleep(5)

    # press search button
    page.click("button.Aside_searchButton__rajGo")
    # time.sleep(5)

    # input keyword (i.e. "flutter") into search bar and press enter
    page.get_by_placeholder("검색어를 입력해 주세요.").fill(keyword)
    # time.sleep(5)
    page.keyboard.down("Enter")
    # time.sleep(5)

    # press positions button
    page.click("a#search_tab_position")
    # time.sleep(5)

    # scroll down the page multiple times
    for i in range(5):
        page.keyboard.down("End")

    # get page content at the end of page
    content = page.content()
    p.stop()

    return content

def get_wanted_jobs(keyword):
    # read content and extract data
    all_jobs = []
    content = get_content(keyword)
    soup = BeautifulSoup(content, "html.parser")

    jobs = soup.find_all("div", class_="JobCard_container__REty8")
    for job in jobs:
        title = job.find("strong", class_="JobCard_title__HBpZf").text
        company = job.find("span", class_="JobCard_companyName__N1YrF").text
        reward = job.find("span", class_="JobCard_reward__cNlG5").text
        url = f"https://www.wanted.co.kr/{job.find('a')['href']}"

        job_data = {
            "title": title,
            "company": company,
            "location": "Seoul", # placeholder for consistency with other databases
            "reward": reward,
            "url": url
        }
        all_jobs.append(job_data)
    return all_jobs

# # export data into csv file
# file = open("dynamic_scraping_output.csv", mode="w")
# writer = csv.writer(file)
# writer.writerow(["Title", "Company", "Reward", "Link"])

# for job in all_jobs:
#     writer.writerow(job.values())

# file.close()