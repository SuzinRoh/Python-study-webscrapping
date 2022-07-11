import requests
from bs4 import BeautifulSoup 
import re

LIMIT = 50
URL = f"https://search.incruit.com/list/search.asp?col=job&kw=python&psize={LIMIT}"

#P sqr_paging sqr_pg_mid

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("p", {"class" : "sqr_paging sqr_pg_mid"}).find_all("span")
    last_page = int(pages[-1].text)
    return last_page

def extract_job(html):
    com_name = html.find("a", {"class" : "cpname"}).string
    job_title = html.find("div", {"class" : "cell_mid"}).find("a").string
    job_id = html.find("div", {"class" : "cell_mid"}).find("button")["jobno"]
    com_loc = html.find("div", {"class" : "cl_md"}).find_all("span", recursive=False)[2].string
    return {'title' : job_title,
             'company' : com_name,
             'location' : com_loc,
             'link' : f"https://job.incruit.com/jobdb_info/jobpost.asp?job={job_id}&src=etc*search"
            }

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&startno={page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("li", {"class" : "c_col"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
        return jobs
          

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs

