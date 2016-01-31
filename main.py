from pymongo import MongoClient
import requests
import mailjet_rest


API_KEY="bla"
API_PASSWORD="bla"
SENDER_EMAIL="bla@bla"
PROJECT_NAME="bla"
FROM_EMAIL="bla"

def send_email(to_email, subject, contents):
    mj_client = mailjet_rest.Client(auth=(API_KEY, API_PASSWORD))
    data = {
        'FromEmail': FROM_EMAIL,
        'FromName': "MicroFinance",
        'Subject': subject,
        'Html-part': contents,
        'Recipients': [
            {"Email": to_email}
        ]
    }
    result = mj_client.send.create(data=data)
    print result

def send_medium_email(email):
    with open("medium.txt") as f:
        send_email(email, "MicroFinance : Education", f.read())

def send_rich_email(email):
    with open("rich.txt") as f:
        send_email(email, "MicroFinance : Help Your Neighbourhood", f.read())

def send_poor_email(email):
    with open("poor.txt") as f:
        send_email(email, "MicroFinance : URGENT", f.read())

def get_expenditure_income(account_id):
    def f(tx):
        if tx['type'] == 'DEBIT':
            return tx['value']
        else:
            return -tx['value']

    account_id = str(account_id)
    json = requests.get("http://localhost:3000/db/cards/list/" + account_id).json()
    all_balance = map(lambda x : x["currentBalance"], json["cards"])

    json = requests.get("http://localhost:3000/db/transactions/list/" + account_id).json()
    all_values = map(f, json["transactions"])
    debit_values = filter(lambda x : x > 0, all_values)
    credit_values = filter(lambda x : x < 0, all_values)

    return (sum(debit_values), -sum(credit_values),)

def main():
    client = MongoClient("mongodb://localhost:27017")
    db = client.MiniOASDB
    cursor = db.accounts.find()
    account_ids = list(map(lambda x: x["accountId"],cursor))
    samples = account_ids[0:10]

    print map(
        get_expenditure_income, samples
    )

if __name__ == "__main__":
    main()
