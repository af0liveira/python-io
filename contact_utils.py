"""Module with tools for managing Contact objects."""

import csv
import json
import pickle

from contact import Contact


def csv_to_contacts(filepath, encoding='latin_1'):
    """Converts a contact list from CSV to a list of Contact objects."""
    contacts = []
    with open(filepath, mode='r', encoding=encoding) as fp:
        csv_reader = csv.reader(fp)
        for line in csv_reader:
            id, name, email = line
            contact = Contact(id=id, name=name, email=email)
            contacts.append(contact)
    return contacts

def contacts_to_pickle(contacts, filepath):
    """Serialize a list of Contact objects to a pickle file."""
    with open(filepath, 'wb') as fp:
        pickle.dump(contacts, fp)

def pickle_to_contacts(filepath):
    """Deserialize a contacts list from a pickle file."""
    with open(filepath, 'rb') as fp:
        contacts = pickle.load(fp)
    return contacts

def contacts_to_json(contacts, filepath):
    """Serialize a contacts lists to JSON format."""
    with open(filepath, 'w') as fp:
        json.dump(contacts, fp, default=lambda contact: contact.__dict__)

def json_to_contacts(filepath):
    """Deserialize a contacts list in JSON format."""
    contacts = []
    with open(filepath, 'r') as fp:
        contacts_json = json.load(fp)
        for contact in contacts_json:
            c = Contact(**contact)
            contacts.append(c)
    return contacts
