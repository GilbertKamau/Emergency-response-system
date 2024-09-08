import africastalking

# Initialize Africa's Talking
username = "okmaisha"
api_key = "7eeba03a290f617010cfd381aed6b577edab78fe47dce52c80799a098f7f00ad"
africastalking.initialize(username, api_key)

# Create a USSD service
ussd = africastalking.USSD
def ussd_callback(args):
    session_id = args['sessionId', None]
    service_code = args['serviceCode','*789*60000#']
    phone_number = args['phoneNumber', '0715619945']
    text = args['text']

    response = ""

    if text == '':
        # Main Menu
        response = "CON Welcome to Okoa Maisha\n"
        response += "1. Report an Incident\n"
        response += "2. Request Assistance\n"
        response += "3. Get Information"
    elif text == '1':
        # Report an Incident
        response = "CON Please describe the incident:\n"
        # Implement logic to collect incident details
    elif text == '2':
        # Request Assistance
        response = "CON What type of assistance do you need?\n"
        # Implement logic to collect assistance details
    elif text == '3':
        # Get Information
        response = "CON Choose an option:\n"
        response += "1. Safety Tips\n"
        response += "2. Emergency Contacts\n"
        # Implement logic to provide information
    else:
        response = "END Invalid input."

    return response

# Start the USSD service
ussd.start(ussd_callback)
