import requests
import truststore
from bs4 import BeautifulSoup
import csv 

truststore.inject_into_ssl()

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

print(response.status_code)

class Job:
    def __init__(self, title, company, location, date_posted , link):
        self.title = title
        self.company = company
        self.location = location
        self.date_posted = date_posted
        self.link = link


soup = BeautifulSoup(response.content, "html.parser")
contents = soup.select("div.card-content")

jobs = []

for content in contents:
    job = Job(
        title=content.find("h2", class_="title").text.strip(),
        company=content.find("h3", class_="company").text.strip(),
        location=content.find("p", class_="location").text.strip(),
        date_posted=content.find("time")["datetime"],
        link=content.find_all("a")[1]["href"]
    )
    jobs.append(job)


dataFile = "jobs.csv"
with open(dataFile , 'w' , newline= "") as f :
    csvwriter = csv.writer(f)
    csvwriter.writerow(["Title", "Company", "Location", "Date Posted" , "Link"])
    for job in jobs:
        csvwriter.writerow([job.title, job.company, job.location, job.date_posted , job.link    ])
