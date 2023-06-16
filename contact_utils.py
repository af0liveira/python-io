"""Module with tools for managing Contact objects."""
import csv
from contact import Contact

def csv_to_contacts(csv_path, encoding='latin_1'):
    """Converts a contact list from CSV to a list of Contact objects."""

    contacts = []

    with open(csv_path, mode='r', encoding=encoding) as fp:
        csv_reader = csv.reader(fp)
        for line in csv_reader:
            id, name, email = line
            contact = Contact(id=id, name=name, email=email)
            contacts.append(contact)

    return contacts

def contacts_to_pickle():
    raise NotImplementedError(f"Function {__name__} hasn't been implemented yet.")

def pickle_to_contacts():
    raise NotImplementedError(f"Function {__name__} hasn't been implemented yet.")

def contacts_to_json():
    raise NotImplementedError(f"Function {__name__} hasn't been implemented yet.")

def json_to_contacts():
    raise NotImplementedError(f"Function {__name__} hasn't been implemented yet.")
