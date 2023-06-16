#!/usr/bin/env python3

csv_path = './data/contacts.csv'

try:
    with open(csv_path, 'r', encoding='latin_1') as fp:
        for contact in fp:
            print(contact, end='')
except FileNotFoundError:
    print(f"File '{csv_path}' could not be found!")
except PermissionError:
    print(f"You don't have the required permissions to open `{csv_path}`!")