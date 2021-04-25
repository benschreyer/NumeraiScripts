#Bensch 4/20/21
#Script to check validation correlation of a list of Numer.ai models and print whether or not they changed from the previous round to the current
import requests



def getAccountValidations(name):
    req = requests.get("https://api-tournament.numer.ai/?query={userActivities(username:\""+name+"\",tournament:8){submission {validationCorrelation } } } ").json()
    return (req["data"]["userActivities"][1]["submission"]["validationCorrelation"],req["data"]["userActivities"][0]["submission"]["validationCorrelation"])

accounts = ["bensch","bensch_a"]

for account in accounts:
    get = getAccountValidations(account)
    #print(get)
    prev = get[0]
    curr = get[1]
    if(curr == prev):
        print(account+ " UNCHANGED " + str(prev))
    else:
        print(account+ " CHANGED PREV:" + str(prev) + " NEW:" + str(curr))

input()
