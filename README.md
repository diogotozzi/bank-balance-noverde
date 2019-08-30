# Bank Balance

This is a simple bank balance AWS Lambda code.

It receives a small batch of accounts(with their funds) in CSV format. Then a second batch
with transactions is run. The result of all transactions are shown at terminal
as a CSV format.

I decided to use the **Strategy Design Pattern** at the *Transfer Class*, so we can change
the algorithn for transfers at runtime depending on the client's account type: normal, premium, black...

#### Attention
You must have Python 3 installed on your machine!

## Run it locally

`python3 main.py accounts.csv transfers.csv`

## Run Deployment script

`python3 deploy.py`

## Run unit tests

`python3 -m unittest discover`
