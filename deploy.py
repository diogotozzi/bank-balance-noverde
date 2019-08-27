import os
import json
import sys
import http.client

class SlackClient:

    def __init__(self):
        self.client = http.client.HTTPSConnection("hooks.slack.com")
        self.headers = {'Content-Type': "application/json"}

    def send_with_body(self, body):
        self.client.request("POST", "/services/xxx/xxxxxx", json.dumps(body), self.headers)
        response = self.client.getresponse().read()
        print(response)

    def send_with_message(self, message):
        body = {
            "channel": "#ti",
            "username": "Bender",
            "icon_url": "https://images-na.ssl-images-amazon.com/images/I/81kq2U4Q4JL._SX569_.jpg",
            "attachments": [
                {
                    "color": "#e8db09",
                    "title": message
                }
            ]
        }
        self.client.request("POST", "/services/xxx/xxxxxx/xxxxxxxx", json.dumps(body), self.headers)
        response = self.client.getresponse().read()
        print(response)

print('''
  _   _   __      __          _
 | \ | |  \ \    / /         | |
 |  \| | __\ \  / /__ _ __ __| | ___
 | . ` |/ _ \ \/ / _ \ '__/ _` |/ _ \\
 | |\  | (_) \  /  __/ | | (_| |  __/
 |_| \_|\___/ \/ \___|_|  \__,_|\___|


NoVerde Lambda Deployment package

You can run as argument like this:
python3 deploy.py [lambda] [notify_slack]

Example:
python3 deploy.py bank-balance yes
''')

if 1 in sys.argv:
    lambda_function = sys.argv[1]
    notify_slack = sys.argv[0]
else:
    lambda_function = input("Type lambda function: ")
    notify_slack = input("Notify deploy? (yes/no) ")

lambdas = ('bank-balance');

if lambda_function in lambdas:

    if 'stag' not in lambda_function:
        production_deploy = input("Warning! Warning! Are you sure wanna deploy in PRODUCTION? (yes/no)")

        if 'no' in production_deploy:
            print("Safely aborting... :)")
            sys.exit()

    if notify_slack == 'yes':
        slack_client = SlackClient()
        slack_client.send_with_message("Deployment %s started" % (lambda_function))
    print('Starting deployment package...')

    print('''

###########################
Generating deploy package...
###########################

''')
    command = "zip -r lambda-function.zip ./ --exclude .git/**\* .gitignore"
    os.system(command.replace("lambda-function", lambda_function))
    print('Deploying %s function to AWS Lambda' % (lambda_function))
    command = "aws lambda update-function-code --function-name lambda-function --zip-file fileb://lambda-function.zip && rm lambda-function.zip"
    os.system(command.replace("lambda-function", lambda_function))
    print('''

Deployment %s lambda function

██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║  ██║██║   ██║██╔██╗ ██║█████╗
██║  ██║██║   ██║██║╚██╗██║██╔══╝
██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝


    ''' % (lambda_function))

    title = "Deployment %s lambda function done" % (lambda_function)
    if notify_slack == 'yes':
        body = {
            "channel": "#ti",
            "username": "Bender",
            "icon_url": "https://images-na.ssl-images-amazon.com/images/I/81kq2U4Q4JL._SX569_.jpg",
            "attachments": [
                {
                    "color": "#29a329",
                    "title": title
                }
            ]
        }
        slack_client.send_with_body(body)
else:
    print('Ops... the %s function does not exists' % (lambda_function))
