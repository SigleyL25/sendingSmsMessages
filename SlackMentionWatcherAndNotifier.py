# By: Larry Sigley

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




#---------------- Functions ---------------
#------------------------------------------





#       Create carrier gatewary.
# https://dev.to/mraza007/sending-sms-using-python-jkd
def create_carrier_specific_gateway_address(contactNumber, carrierName):
    carrierGatewayIs = ""


    if carrierName == "AT&T":
        carrierGatewayIs = contactNumber + "@txt.att.net"
    elif carrierName == "Sprint":
        carrierGatewayIs = contactNumber + "@messaging.sprintpcs.com"
    elif carrierName == "T-Mobile":
        carrierGatewayIs = contactNumber + "@tmomail.net"
    elif carrierName == "Verizon":
        carrierGatewayIs = contactNumber + "@vtext.com"
    elif carrierName == "Boost Mobile":
        carrierGatewayIs = contactNumber + "@myboostmobile.com"
    elif carrierName == "Cricket":
        carrierGatewayIs = contactNumber + "@sms.mycricket.com"
    elif carrierName == "Metro PCS":
        carrierGatewayIs = contactNumber + "@mymetropcs.com"
    elif carrierName == "Tracfone":
        carrierGatewayIs = contactNumber + "@mmst5.tracfone.com"
    elif carrierName == "U.S. Cellular":
        carrierGatewayIs = contactNumber + "@email.uscc.net"
    elif carrierName == "Virgin Mobile":
        carrierGatewayIs = contactNumber + "@vmobl.com"
    

    return carrierGatewayIs





#       Create SMS message.
# https://dev.to/mraza007/sending-sms-using-python-jkd
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





#       Sending SMS Message
# https://dev.to/mraza007/sending-sms-using-python-jkd
def sending_sms_message (email, emailPassword, smsCarrierGateway, emailSmtpServer, emailPort, message):
    # Starting email server
    theServer = smtplib.SMTP(emailSmtpServer,emailPort)

    # Starting the server
    theServer.starttls()

    # Login to server with password
    theServer.login(email, emailPassword)

    theServer.sendmail(email, smsCarrierGateway, message)
    theServer.quit()









#-------------------- MAIN ----------------
#------------------------------------------

# Get Slack Credentials
# Get Users cell phone number
# Store cedentials and cell number (user app data directory)
# Check Slack application for messages or mentions




# Send SMS message to cell phone if messaged or mentioned
carrierToUse = (create_carrier_specific_gateway_address("9167124601", "T-Mobile"))
print("Carrier gatewary is: " + carrierToUse)
sendersEmailAddress = ""
sendersEmailPassword = ""

messageToSend = sms_message("Slack watcher notification.", "You've got a message on Slack!", sendersEmailAddress, carrierToUse)
print(messageToSend)

sending_sms_message(sendersEmailAddress, sendersEmailPassword, carrierToUse, "smtp.gmail.com", 587, messageToSend)
print("SMS message sent.")