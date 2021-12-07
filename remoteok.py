import requests
from bs4 import BeautifulSoup

def remote_jobs(term):
  url= "https://remoteok.io/remote-dev+{}-jobs?hide_sticky=&compact_mode=true".format(term)
  headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
  
  remote_db=[]
  r=requests.get(url,headers=headers)
  soup=BeautifulSoup(r.text,"html.parser")

  page=soup.find("div",{"class":"page"})
  container=page.find("div",{"class":"container"})
  table=container.find("table",{"id":"jobsboard"})
  jobs=table.find_all("tr")

  for job in jobs:
    try:
      title=job.find("h2",{"itemprop":"title"}).text
      company=job.find("h3",{"itemprop":"name"}).text
      link=job.find("a",{"class":"preventLink"})["href"]
      link="https://remoteok.io"+link
  
      detail={
        "title":title,
        "company":company,
        "link":link
      }
      remote_db.append(detail)
    except:
      pass

  return remote_db

