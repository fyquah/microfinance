# Send a hypothetical email to quah.fy95@gmail.com

import main
import time
import requests

CAPITAL_ONE_API_KEY="bla"
CAPITAL_ONE_URL="https://api.reimaginebanking.com"

def send_money(from_id, to_id, amount):
    requests.post(CAPITAL_ONE_URL + "/accounts/" +
            from_id + "/transfers",
            json={
                "id": to_id,
                "body": {
                      "medium": "balance",
                      "payee_id": to_id,
                      "amount": amount,
                      "transaction_date": "2016-01-31",
                      "status": "pending",
                      "description": "This is a pooled payment for CB2"
                    }
                })


i = 0
while i < 10000:
    print '.',
    i += 1

print ''
print "Sending email to People with good financial situation ..."
main.send_rich_email("quah.fy95@gmail.com")
print "Sending email to People with bad financial situation ..."
main.send_medium_email("quah.fy95@gmail.com")
print "Sending email to People with bad financial situation ..."
main.send_poor_email("quah.fy95@gmail.com")

print 'Done!'

time.sleep(30)

main.send_email("quah.fy95@gmail.com", "MicroFinance : Thank You", "Thank you for helping out a Cambridge, CB2! We have creditted your CapitalOne Bank Account. Your microlending of $5 will help one of your neighbours to get out of debt really really soon!")

print 'Done!'
time.sleep(30)

main.send_email("quah.fy95@gmail.com", "MicroFinance : Thank You", "Thank you for reply! We have debitted your CapitalOne Bank Account. We hope this, along with some education, will help you get our of debt really soon!")
