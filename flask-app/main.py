from extractors.remoteok_scraper import get_remoteok_jobs
from extractors.dynamic_scraper import get_wanted_jobs
from flask import Flask, render_template, request, redirect, send_file
from file import save_to_file

app = Flask("JobScraper")
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = {} #cache

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")

    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = get_remoteok_jobs(keyword) + get_wanted_jobs(keyword)
        db[keyword] = jobs

    # flask allows you  to send variables to html
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None or keyword =="":
        return redirect("/")
    
    if keyword not in db:
        #user has to first go to search page for us to get database
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True) #trigger download
    
app.run()