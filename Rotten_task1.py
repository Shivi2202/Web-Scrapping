import requests
import json 
from bs4 import BeautifulSoup
import pprint
def rotten_data():
    url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    page=requests.get(url)
    HTMLContent=BeautifulSoup(page.content,"html.parser")
    # print(HTMLContent)
    Tabledata= HTMLContent.find("table",class_="table")
    # pprint.pprint(Tabledata)
    rank=Tabledata.find_all('td',class_='bold')
    rating=Tabledata.find_all("span",class_="tMeterScore")
    title=Tabledata.find_all("a",class_="unstyled articleLink")
    # pprint.pprint(title)
    reviews=Tabledata.find_all("td",class_="right hidden-xs")
    main_list=[]
    for i in range(len(rank)):
        ranking=rank[i].get_text()
        Rating=rating[i].get_text().strip()
        Title=title[i].get_text().strip()
        a = Title.split()
        urls="https://www.rottentomatoes.com"+title[i]["href"]
        years=int(a[-1][1:5])
        Reviews=reviews[i].get_text()
        main_dict={"rank":ranking,"title":Title,"Ratings":Rating,"Reviews":Reviews,"url":urls,"year":years}
        main_list.append(main_dict)
    with open("rotten_file1.json","w") as file_1:
        json.dump(main_list,file_1,indent=3)
        return main_list
first_data=rotten_data()