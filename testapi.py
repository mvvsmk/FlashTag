import requests
import json

# {
#     "user": 3,
#     "toll": 1,
#     "vehicle_number" : "MH04AH1053",
#     "vehicle_distance" : 10,
#     "transaction_status" : 1 
# }

inputString = "<3,1,MH04AH1053,10,1>"
# <userid,tollid,vehicle_number,vehicle_distance,transaction_status>

def parseInputtojson(inputString):
    inputString = inputString.replace("<","")
    inputString = inputString.replace(">","")
    inputString = inputString.split(",")
    inputJson = {
        "user": inputString[0],
        "toll": inputString[1],
        "vehicle_number" : inputString[2],
        "vehicle_distance" : inputString[3],
        "transaction_status" : inputString[4] 
    }
    return inputJson

def sendRequest(inputJson):
    url = "https://flashtag.onrender.com/test/"
    headers = {'Content-type': 'application/json',
               'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'}
    print(inputJson)
    response = requests.post(url, json=inputJson, headers=headers)
    print(response.status_code)
    outputJson =response.json()
    if(outputJson['detail'] == "Transaction successfull"):
        print("Transaction created")
        return True
    else:
        print("Transaction failed")
        return False

if __name__ == "__main__":
    inputJson = parseInputtojson(inputString)
    sendRequest(inputJson)
