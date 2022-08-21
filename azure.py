import requests 
from bs4 import BeautifulSoup
from datetime import date
import copy

ROOT_URL = "https://azure.microsoft.com"
LOCATION = "/en-us"
PAGE = "/blog/?Page="
DATE = date.today().strftime("%A, %B %d, %Y")
print(DATE)


def process_azure_blog(num:str = "1"):
    rq = requests.get(ROOT_URL + LOCATION + PAGE + num)
    soup = BeautifulSoup(rq.text, "html.parser")
    all_articles = soup.find_all("article")
    articles_info = []
    for article in all_articles:
        today_date = f"{article.select_one('p', class_='text-body5').text}"
        if (today_date == DATE):
            link = f"{ROOT_URL}{article.select_one('a').get('href')}"
            title = f"{article.select_one('a').get('title')}"
            description = [i.text for i in article.select('p') if i.get('lang')][0]
            tags = []
    
            if article.find_all("li") != []:
                for tag in article.find_all("li"):
                    tags.append(tag.text.strip())
            else:
                tags.append("No Tag")

            # check for repeative article
            if not articles_info :
                articles_info.append({"link":copy.deepcopy(link), "title":copy.deepcopy(title), "time": copy.deepcopy(today_date), "description": copy.deepcopy(description), "tags": copy.deepcopy(tags)})
            else:
                for index, i in enumerate(articles_info):
                    if i['title'] == title:
                        articles_info[index] = {"link":copy.deepcopy(link), "title":copy.deepcopy(title), "time": copy.deepcopy(today_date), "description": copy.deepcopy(description), "tags": copy.deepcopy(tags)}
                        break 
                    else:
                        articles_info.append({"link":copy.deepcopy(link), "title":copy.deepcopy(title), "time": copy.deepcopy(today_date), "description": copy.deepcopy(description), "tags": copy.deepcopy(tags)})
    return articles_info

def get_azure_blog_json():
    today_articles_1 = process_azure_blog(num="1") 

    return [today_articles_1]

