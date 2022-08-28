from bs4 import BeautifulSoup   
from urllib.request import Request, urlopen
from flask_restful import Resource

class Scraper(Resource):

    def get(self):

        results = []

        #TODO: Connect to RDS

        # URL to scrape

        req = Request(
            url="https://www.comparefirst.sg/wap/productsListEvent.action?prodGroup=invst&pageAction=prodlisting", 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        fp = urlopen(req)
        mybytes = fp.read()

        html_doc = mybytes.decode("utf8")
        fp.close()

        soup = BeautifulSoup(html_doc, 'html.parser')

        # Find all <li> tags with the specified class
        for policy in soup.find_all('li', class_=""):
            temp = {
                "Company": "",
                "Policy Name": "",
                "Premium Type": "",
                "Product Summary": "",
                "Features": [],
            }
            for div in policy.contents:
                if div["class"] == "result_details prodlist-results":
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
                    temp["Product Summary"] = div.a["href"]
            # #TODO: Check if policy in database, and add it if it isn't
            # results.append(temp)
       
        return results
        # return {"Message": f"Successfully inserted {num_articles} articles into the DB"}, 200