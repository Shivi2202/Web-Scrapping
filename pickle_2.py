import requests
import json 
from bs4 import BeautifulSoup
def pickle_data():
    url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    div=soup.find("div",class_="_1gX7")
    div_span=div.span.get_text()
    div_int=int(div_span.split()[1])
    div_float=div_int//32+1
    my_list=[]
    position=0
    incmt=1
    while incmt<=div_float:
        url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(incmt)
        page=requests.get(url)
        soup=BeautifulSoup(page.text,"html.parser")
        div1=soup.find("div",class_="_3RA-")
        pickle_name=div1.find_all("div",class_="UGUy")
        pickle_price=div1.find_all("div",class_="_1kMS")
        pickle_link=div1.find_all("div",class_="_3WhJ")
        index=0
        while index<len(pickle_name):
            position+=1
            name=pickle_name[index].get_text()
            price=(pickle_price[index].span.get_text())
            link=(pickle_link[index].a["href"])
            dict={"Position":position,"Name":name,"Price":price,"Link":link}
            my_list.append(dict)
            index=index+1
        incmt+=1
    with open("pickle2_file.json","w") as file:
        json.dump(my_list,file,indent=3)
    return my_list
pickle_data()