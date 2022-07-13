import requests
from bs4 import BeautifulSoup 
import re

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser");
    pagination = soup.find("div", {"class" : "pagination"})

    links = pagination.find_all("a")
    pages = []
    for link in links[0:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_job(html):
    job_title = html.find("span")["title"]
    com_name = html.find("span", {"class":"companyName"}).string
    com_loc = html.find("div", {"class":"companyLocation"}).string
    job_id = html.find("a")["data-jk"]
    return {'title' : job_title,
             'company' : com_name,
             'location' : com_loc,
             'apply_link' : f"https://kr.indeed.com/viewjob?jk={job_id}"
            }
    

def extract_jobs(last_pages):
    jobs = []
    for page in range(last_pages):
        print(f"Scrapping Indeed: page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser");
        job_contents = soup.find_all("td",{"class" : "resultContent"})
        for result in job_contents:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_pages = get_last_page()
    jobs = extract_jobs(last_pages)
    return jobs

#companyName