import os
import mysql.connector
import json
import string
from bottle import route, run

@route('/')
def index():
    return 'Hello World'

@route('/postcode/<postcode>')
def postcode(postcode):
    returnData = "INVALID input"
    #Validate input - can only be 4 numerics
    if len(postcode) == 4 and postcode.isdigit():
        #MYSQL Connection
        cnx = mysql.connector.connect(user=os.environ["dunnydbuser"], password=os.environ["dunnydbsecret"],
                            host=os.environ["dunnydbhost"],
                            database=os.environ["dunnydbname"])
        #Query
        cursor = cnx.cursor()
        query = ("SELECT name, address1, town FROM toilets "
         "WHERE postcode=" + postcode)
        cursor.execute(query)
        resultRow = ""
        for (name, address1, town) in cursor:
              resultRow = resultRow + json.dumps({'name' : name, 'address1': address1, 'town': town}) + ","

        resultRow = resultRow.rstrip(",")
        cursor.close()
        cnx.close()
        returnData = "[" + resultRow + "]"
    return returnData

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)