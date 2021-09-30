from typing import Container
import requests
import json 
from bs4 import BeautifulSoup
def first_data ():
    url="https://webscraper.io/test-sites"
    page=requests.get(url)
    HTMLContent=BeautifulSoup(page.content,"html.parser")
    # div_1=HTMLContent.find("div",class_="row test-site")
    header=HTMLContent.find_all("h2")
    # print(header)
    position=0
    main_list=[]
    for h2 in header:
        position+=1
        course_name=h2.get_text().strip()
        urls=h2.a["href"]

        my_dict={"position":position,"course_name":course_name,"urls":urls}

        main_list.append(my_dict)
    with open("e-commerce.json","w") as file_1:
        json.dump(main_list,file_1,indent=3)
    return main_list
       
first_data()