import requests
from bs4 import BeautifulSoup

def stack_jobs(term):
  url= "https://stackoverflow.com/jobs?r=true&q={}".format(term)
  headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
  r=requests.get(url,headers=headers)
  soup=BeautifulSoup(r.text,"html.parser")
  table=soup.find("div",{"class":"js-search-results d-flex fd-row flush-left"})
  table2=table.find("div",{"class":"previewable-results js-previewable-results"})
  pagination=table2.find("div",{"class":"d-flex gs16 fd-column"})
  page=pagination.find("div",{"class":"s-pagination"}).find_all('span')[-2].text
  page=int(page)
  db=[]

  for x in range(1,page+1):
    stack_url="https://stackoverflow.com/jobs?r=true&q={}&pg={}".format(term,x)
    stack_r=requests.get(stack_url,headers=headers)
    stack_soup=BeautifulSoup(stack_r.text,"html.parser")
    stack_table=stack_soup.find("div",{"class":"js-search-results d-flex fd-row flush-left"})
    stack_jobs=stack_table.find("div",{"class":"listResults"})
    stack_job=stack_jobs.find_all("div")
    for i in stack_job:
      try:
        title= i.find("h2",{"class":"mb4 fc-black-800 fs-body3"}).text.strip()
        link= i.find("h2",{"class":"mb4 fc-black-800 fs-body3"}).find('a')["href"]
        company= i.find("h3",{"class":"fc-black-700 fs-body1 mb4"}).find('span').text.strip()
        if "via" in company:
          n=company.find("via")
          company=company[n+3:]
          company=company.strip()
        link="https://stackoverflow.com"+link
        detail={
          "title":title,
          "company":company,
          "link":link
        }
        db.append(detail)
      except:
        pass
  stack_db=[]
  # 3중복 정렬
  for x in range(len(db)//3):
      y=0+3*x
      stack_db.append(db[y])
  
  return stack_db