from selenium import webdriver
import pandas as pd
from bs4 import BeatifulSoup

## Download the chromedriver from link in description
## and give the location of executable here
driver = webdriver.Chrome(".chromedriver")

dataframe = pd.dataframe(columns=["Title","Location","Company","Salary","Sponsored","Description"])

##Step1 : Get the page
driver.get("https://id.indeed.com/jobs?q=data+science&l=Indonesia")
driver.implicity_wait(4)

all_jobs = driver.find_elements_by_class_name('result')

for job in all_jobs:

	result_html = job.get_attribute('innerHTML')
	soup = BeatifulSoup(result_html,'html.parser')
	
		title = soup.find("a",class_="jobtitle").text.replace('\n','')
	try:
	except:
		title = "None"

	try:
		location = soup.find(class_="location").text
	except:
		location = "None"

	try:
		company = soup.find(class_="company").text.replace('\n',"").strip()
	except:
		company = "None"

	try:
		salary = soup.find(class_="salary").text.replace('\n',"").strip()
	except:
		salary = "None"

	try:
		sponsored= soup.find(class_="sponsoredGray").text
		sponsored = "Sponsored"
	except:
		sponsored = "Organic"

	sum_div = job.find_elements_by_class_name("summary")[0]

	sum_div.click()

	job_desc = driver.find_elements_by_id('vjs-desc').text

	df = df.append({'Title':title,'Location':location,"Company":company,
					"Sponsored":sponsored,"Description":job_desc},
					ignore_index=True)


	


