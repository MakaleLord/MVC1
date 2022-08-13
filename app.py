#!/usr/bin/python3

from flask import Flask, render_template, requests, redirect, url_for
import random
app = Flask(__name__)

day = ["2", "7", "4"]

month = ["5", "1" "8"]

year = ["0", "9", "3"]

flux = "http://archive.org/wayback/available?"

site = "youtube.com"

@app.route("/<month>/<day>/<year>")
def time_machine(year, month, day):
    url = f"{flux}url={site}&timestamp={year}{month}{day}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        url = data['archived_snapshots']['closest']['url']
    return render_template('page.html', site_url=url)

@app.route("/")
def home_page():
    return redirect("time_machine")
    random.randint(0, 9)
