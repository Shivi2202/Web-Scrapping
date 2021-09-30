import requests
import json 
from bs4 import BeautifulSoup
import pprint
def movie_data():
    url="https://www.rottentomatoes.com/m/black_panther_2018"
    page=requests.get(url)
    HTMLContent=BeautifulSoup(page.content,"html.parser")
    Trs=HTMLContent.find_all("li",class_="meta-row clearfix")
    key_data=HTMLContent.find_all("div",class_="meta-label subtle")
    value_data=HTMLContent.find_all("div",class_="meta-value") 
    main_list=[]
    main_dict={}
    for i  in range(0,len(Trs)):
        key=key_data[i].get_text()
        value=value_data[i].get_text().split()
        main_list.append(value)
    # pprint.pprint(main_list)
        if key=="Genre" or key=="Director" or key=="Producer" or key=="Runtime":
            main_dict.update({key:main_list})
        else:
            main_dict.update({key:value})
    main_list.append(main_dict)
    pprint.pprint(main_dict)

        # main_dict.update({key:value})
    # pprint.pprint(main_list)
    with open("rotten_file4.json","w") as file:
        json.dump(main_dict,file,indent=3)
data1=movie_data()


    
    




