import requests
import json 
from bs4 import BeautifulSoup
url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
div1=soup.find("div",class_="_3RA-")
pickle_name=div1.find_all("div",class_="UGUy")
pickle_price=div1.find_all("div",class_="_1kMS")
pickle_link=div1.find_all("div",class_="_3WhJ")
my_list=[]
position=0
i=0
while i<len(pickle_name):
    position+=1
    a=pickle_name[i].get_text()
    b=int(pickle_price[i].span.get_text())
    c=pickle_link[i].a["href"]
    i+=1
    my_dict={"Position":position,"Name":a,"Price":b,"Link":c}
    my_list.append(my_dict)
with open("pickle_file.json","w") as file_1:
    json.dump(my_list,file_1,indent=3)






























# first_div=s
# a=first_div.find("span",class_="_3-is").get_text().split()
# 
