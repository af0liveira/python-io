#!/usr/bin/env python3

csv_path = './data/contacts.csv'

try:
    fp = open(csv_path, 'r', encoding='latin_1')

    for contact in fp:
        print(contact, end='')

finally:
    fp.close()