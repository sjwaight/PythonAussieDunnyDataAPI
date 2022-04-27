# Python Aussie Dunny Data API

A simply Python-based REST API that is hosted using [bottle](https://bottlepy.org/docs/dev/).

This code is used as part of a demonstration on how you can move from running code on Virtual Machines or on-premises, to containers and finally [Azure Serverless](https://github.com/sjwaight/ServerlessDownunderDunnies).

In order to run the code you will need a MySQL database that is populated with the data contained in the [toiletdata_short.csv](/toiletdata_short.csv) file in this repository. This data is based on the Australian [National Public Toilet Map](https://data.gov.au/data/dataset/activity/national-public-toilet-map) dataset.

Set four environment variables to contain the connection details to your MySQL database and then run the dunnyapi.py file using Python 3. Make sure you've installed the requirements.txt contents!

Check out Microsoft Australia and New Zealand's cloud developer show [New Breakpoint](https://aka.ms/new-breakpoint/) on which this demo was used (Series 2, Show 9).