#!/usr/bin/env python3

from contact_utils import (csv_to_contacts, contacts_to_pickle,
                           pickle_to_contacts)

csv_path = './data/contacts.csv'
pickle_path = './data/contacts.p'

try:
    contacts = csv_to_contacts(csv_path)
    contacts_to_pickle(contacts, pickle_path)
except FileNotFoundError:
    print(f"File '{csv_path}' could not be found!")
except PermissionError:
    print(f"You don't have the required permissions to open `{csv_path}`!")

for contact in pickle_to_contacts(pickle_path):
    print(contact.__dict__)