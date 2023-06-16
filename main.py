#!/usr/bin/env python3

from contact_utils import csv_to_contacts

csv_path = './data/contacts.csv'

try:
    contacts = csv_to_contacts(csv_path)
except FileNotFoundError:
    print(f"File '{csv_path}' could not be found!")
except PermissionError:
    print(f"You don't have the required permissions to open `{csv_path}`!")

for contact in contacts:
    print(contact.__dict__)