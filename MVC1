#!/usr/bin/python3

from flask import Flask, render_template, requests, redirect, url_for
import random
app = Flask(__name__)

day = ["2", "7", "4"]

month = ["5", "1" "8"]

year = ["0", "9", "3"]
####### E X E R C I S E S #########
#
#  Exercise 1: Let's start with our first route
#  Exercise 2: Set the day in past you want to go
#  Exercise 3: Brace yourself for a trip to past
#  Exercise 4: Show the past webpage in the flask app.
#  Bonus: Show the futuristic loader while the iframe is loading. 
# 
#  Homework 1: Go to random date when its not mentioned in url.
#              - Import the random module
#              - Create a new function named home_page.
#              - Run this function on route /
#              - Get three random numbers for day, month and year using random.randint
#              - Import the redirect, url_for from flask
#              - Inside home_page()
#                  Redirect the route to time_machine using redirect
#                  Send the random day, month and year as data while calling url_for function
#
#  Homework 2: Get the site to visit from the route as well. 
#              - Add another variable for website in route for time_machine
#              - Add a parameter in time_machine function for website
#              - Use website parameter instead of site variable while generating api url.
#              - Set the website route variable to site variable where you saved the website.
###################################

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
