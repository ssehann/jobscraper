# conda activate webscraper
# make sure interpreter is set to webscraper

import requests
from bs4 import BeautifulSoup

r = requests.get("https://remoteok.com/remote-python-jobs")
# print(r.status_code)
# print(r.content)
# this returns 429 Too Many Requests and we're not able to access content

# solution: inspect -> network -> select page with status_code 200 -> get User_Agent
# we trick them into thinking that we are a browser
response = requests.get("https://remoteok.com/remote-python-jobs",
                   headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"})
# print(response.status_code)
# print(url.content)
# now this returns 200 and we see all the html content we want!

def get_remoteok_jobs(keyword):
    all_jobs = []
    response = requests.get(f"https://remoteok.com/remote-{keyword}-jobs",
                   headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("table", id="jobsboard").find_all("tr", attrs={"data-offset":True})

    for job in jobs:
        title = job.select("h2")[0].text.strip()
        company = job.select("h3")[0].text.strip()
        data = job.find_all("div", class_="location")
        if (len(data) <2):
            location = "Not specified"
            reward = data[0].text
        else:
            location = data[0].text
            reward = data[1].text

        link = job.find("a")["href"]

        job_data = {
            "title": title,
            "company": company,
            "location": location,
            "reward": reward,
            "url": f"https://remoteok.com{link}"
        }
        all_jobs.append(job_data)
    return all_jobs

# example usage
# langs = ["golang", "python", "flutter"]
# for lang in langs:
#     print(lang, get_remoteok_jobs(lang))