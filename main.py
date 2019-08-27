from src.accounts import Accounts

import csv
import sys

def main(accounts_file, transfers_file):

    accounts_list = load_accounts(accounts_file)
    transfers_list = load_transfers(transfers_file)

    accounts = Accounts(accounts_list)
    accounts.batch_transfers(transfers_list)

    for account in accounts.all():
        print(str(account[0]) + ',' + str(account[1]), end='\n')

def load_accounts(accounts_file):
    with open(accounts_file) as f:
        reader = csv.reader(f, delimiter = ',')
        accounts_list = list(reader)

    return accounts_list

def load_transfers(transfers_file):
    with open(transfers_file) as f:
        reader = csv.reader(f, delimiter = ',')
        return list(reader)

main(sys.argv[1], sys.argv[2])
