from bs4 import BeautifulSoup   
from urllib.request import Request, urlopen
from flask_restful import Resource
from selenium import webdriver
import chromedriver_binary
import boto3
from application import policies_db

class Scraper(Resource):

    def get(self):
        # URL to scrape
        url="https://www.comparefirst.sg/wap/productsListEvent.action?prodGroup=invst&pageAction=prodlisting"
        browser = webdriver.Chrome()
        browser.get(url)
        html_doc = browser.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')

        policies = soup.find_all('li', class_="result_content")

        # Find all <li> tags with the specified class
        for policy in policies:
            temp = {
                "Company": "",
                "Policy Name": "",
                "Premium Type": "",
                "Product Summary": "",
                "Features": [],
            }
            for div in policy.contents:
                if div["class"] == ['result_details', 'prodlist-results']:
                    tag = div.h3
                    temp["Company"] = tag.text
                    tag = tag.findNext('p')
                    temp["Policy Name"] = tag.text
                    tag = tag.findNext('p')
                    temp["Premium Type"] = tag.text
                    tag = tag.findNext('ul').contents
                    for feature in tag:
                        temp["Features"].append("active" in feature.img["src"])

                else:
                    if div.a is not None:
                        temp["Product Summary"] = "https://www.comparefirst.sg/wap/" + div.a["href"]

            policies_db.put_item(Item=temp)

        return {"Message": "Successfully inserted articles into the DB"}, 200