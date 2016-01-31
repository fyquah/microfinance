# Send a hypothetical email to quah.fy95@gmail.com

import main
import time

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
