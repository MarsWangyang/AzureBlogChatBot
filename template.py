import copy
import os
import azure
import json

PATH = "./Template"
bubblePath = os.path.join(PATH, "bubbleTemplate.json")
carouselPath = os.path.join(PATH, "CarouselTemplate.json")
flexMessagePath = os.path.join(PATH, "FlexMessage.json")

with open(bubblePath, "r") as bubble_json:
    bubbleTemplate = json.load(bubble_json)
with open(carouselPath, "r") as carousel_json:
    carouselTemplate = json.load(carousel_json)
with open(flexMessagePath, "r") as flex_json:
    flexMessageTemplate = json.load(flex_json)


def process_articles_template():
    all_articles_attribtes = azure.get_azure_blog_json()
    for page in all_articles_attribtes:
        for article in page:
            print(article['tags'])
            bubbleTemplate['body']['contents'][0]['text'] = copy.deepcopy(article['title'])
            bubbleTemplate['body']['contents'][1]['contents'][0]['text'] = copy.deepcopy(article['description'])
            bubbleTemplate['body']['contents'][1]['contents'][2]['contents'][1]['text'] = copy.deepcopy(article['time'])
            bubbleTemplate['body']['contents'][1]['contents'][3]['contents'][1]['text']  = copy.deepcopy(", ".join(article['tags']))
            bubbleTemplate['footer']['contents'][0]['action']['uri'] = copy.deepcopy(article['link'])
            
            carouselTemplate['contents'].append(copy.deepcopy(bubbleTemplate))
    flexMessageTemplate['contents'] = carouselTemplate
 
    return flexMessageTemplate

