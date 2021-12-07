import requests
import csv
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, send_file
from stackoverflow import stack_jobs
from weworkremotely import we_jobs
from remoteok import remote_jobs

app=Flask("Skan job remote")
fakeDB={}

@app.route("/")
def home_page():
  return render_template("home.html")

@app.route("/search")
def search_page():
  term=request.args.get('term')
  term=term.lower()
  total_job=[]
  check=fakeDB.get(term)

  if check:
    total_job=fakeDB[term]
    number_job=len(total_job)
  else:
    stack_jobs(term)
    we_jobs(term)
    remote_jobs(term)
    total_job.extend(stack_jobs(term))
    total_job.extend(we_jobs(term))
    total_job.extend(remote_jobs(term))
    number_job=len(total_job)
    fakeDB[term]=total_job

  return render_template("search.html",term=term,total_job=total_job,  number_job=number_job)

@app.route("/send")
def send_csv():
  term=request.args.get('term')
  term=term.lower()
  total_job=fakeDB[term]

  def save_csv(term):
    f=open("{}.csv".format(term),mode="w")
    w=csv.writer(f)
    w.writerow(["Title","Company","Link"])
    for x in total_job:
      w.writerow(list(x.values()))
    f.close()
    return 
  save_csv(term)

  return send_file("{}.csv".format(term), mimetype='csv', as_attachment=True, attachment_filename="{}.csv".format(term))

app.run(host="127.0.0.1",port="8080")
# URL= "http://127.0.0.1:8080/"