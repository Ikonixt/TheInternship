# The Internship - 4
# Gorramuth Prasertkull
# Program to output logos sorted by company description length
# Simple Flask API to return full url of logo location

from bs4 import BeautifulSoup
import json
import requests
from flask import Flask, jsonify

url = "https://theinternship.io"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "html.parser")
logoList = soup.find_all('img', class_='center-logos')
descList = soup.find_all('span', class_='list-company')
mapper = {}

# Parse the html tags and maps each image's url to its respective startup
for logo in range(len(logoList)):
    mapper[logoList[logo]['src']] = descList[logo].get_text()

logoDict = dict()
for keys in sorted(mapper, key=lambda x: len(mapper[x])):
    logoDict[keys] = "https://theinternship.io/"+keys
    print(keys)


# API for calling GET
app = Flask(__name__)
@app.route('/companies', methods=['GET'])
def companyLogo():
    response = jsonify({
        'companies' : [ { 'logo' : logoDict[x] } for x in logoDict ]
    })
    return response

if __name__ == "__main__":
    app.run()