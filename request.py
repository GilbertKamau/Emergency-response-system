from flask import Flask, request

app = Flask(__name__)

# Sample USSD menu options
menu = {
    '1': 'Check Balance',
    '2': 'Top Up',
    '3': 'Transfer Funds',
    '4': 'Settings',
    '0': 'Exit'
}

@app.route('/ussd', methods=['GET', 'POST'])
def ussd_callback():
    session_id = request.values.get('sessionId')
    phone_number = request.values.get('phoneNumber')
    text = request.values.get('text')

    if text == '':
        # Initial request
        response = "Welcome to My USSD App\n"
        for key, value in menu.items():
            response += f"{key}. {value}\n"
    else:
        # Process user input
        if text == '0':
            response = "Thank you for using My USSD App."
        elif text in menu:
            response = f"Select an option:\n{menu[text]}"
        else:
            response = "Invalid input. Please try again."

    return response

if __name__ == '__main__':
    app.run(debug=True)
