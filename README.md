# HACCwebsite

This is the initial Django framework for an Election Information website being created for HACC. CSS and page templates were taken from Bootstrap.

The project is "testSite".
Within this folder, "webapp" is currently an unused web application template.
Within the "testSite" folder, overall project changes can be made in the settings.py and urls.py files.

Within the "hcaaSite" folder, py files can be edited as needed.
"static" folder contains files needed for the web pages. These files are publically visible.
"templates/haccSite" folder contains the html pages. "header.html" is currently the main demo page. *this name will be changed later as needed.
* if adding more folders of html pages in templates, please add the appropriate info to "apps.py" and "views.py"

To access Hawaii Open Data Socrata database see this python example (change url as needed)
(requires "pip install requests" and "pip install sodapy")

# from api, using Python Requests
import requests

#url = "https://data.hawaii.gov/resource/u76e-fv4g.json"
url = "https://data.hawaii.gov/resource/u76e-fv4g.json?candidate_name=Bean, Tracy"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

for n, loop in enumerate(data):
    print ("Record ", n)
    print (data[n], '\n')
