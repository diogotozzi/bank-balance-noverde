import csv
import sys

def main(accounts_file, transfers_file):

    with open(accounts_file) as f:
        reader = csv.reader(f, delimiter = ',')
        accounts_list = list(reader)

    with open(transfers_file) as f:
        reader = csv.reader(f, delimiter = ',')
        transfers_list = list(reader)

    print(accounts_list)
    print(transfers_list)

main(sys.argv[1], sys.argv[2])
