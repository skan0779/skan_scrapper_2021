import requests
from bs4 import BeautifulSoup

def we_jobs(term):
  url= "https://weworkremotely.com/remote-jobs/search?term={}".format(term)
  headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
  
  we_db=[]
  r=requests.get(url,headers=headers)
  soup=BeautifulSoup(r.text,"html.parser")

  table=soup.find("div",{"class":"jobs-container"})
  section=table.find_all("section",{"class":"jobs"})
  for x in section:
    jobs=x.find('ul').find_all('li')[:-1]
    for y in jobs:
      title=y.find("span",{"class":"title"}).text
      company=y.find("span",{"class":"company"}).text
      link=y.find_all('a')[1]["href"]
      link="https://weworkremotely.com"+link
      detail={
        "title":title,
        "company":company,
        "link":link
      }
      we_db.append(detail)
 
  return we_db