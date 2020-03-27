# By: Larry Sigley

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#---------------- Functions ---------------
#------------------------------------------

def create_carrier_specific_gateway_address(contactNumber, carrierName):




def sms_message(subjectOfMessage, bodyOfMessage, fromEmailAddress, smsCarrierGateway):
    # Using the MIME module to create the message
    theMessage = MIMEMultipart()
    theMessage['From'] = fromEmailAddress
    theMessage['To'] = smsCarrierGateway
    theMessage['Subject'] = (subjectOfMessage + "\n")

    # Adding the body to the message
    theMessage.attach(MIMEText((bodyOfMessage + "\n"), 'plain'))

    # Convert message to string
    theMessageConvertedToString = theMessage.as_string()

    return theMessageConvertedToString




#       SMS Messaging
# https://dev.to/mraza007/sending-sms-using-python-jkd
def sending_sms_message (email, emailPassword, smsCarrierGateway, emailSmtpServer, emailPort, message):
    # Starting email server
    theServer = smtplib.SMTP(emailSmtpServer,emailPort)

    # Starting the server
    theServer.starttls()

    # Login to server with password
    theServer.login(email, emailPassword)

    theServer.sendmail(email, smsCarrierGateway)
    theServer.quit()




#-------------------- MAIN ----------------
#------------------------------------------

# Get Slack Credentials
# Get Users cell phone number
# Store cedentials and cell number (user app data directory)
# Check Slack application for messages or mentions
# Send SMS message to cell phone if messaged or mentioned
checkingMessage = sms_message("The Test", "You've got a message", "testingEmail@gmail.com", "5555555555@tmobile.com")
print(checkingMessage)