# Python I/O: Conversion of a contacts list in CSV with pickle and JSON

This code was developed as an exercise within the online course
[_Python: trabalhando com I/O_](https://cursos.alura.com.br/course/python-3-trabalhando-com-io)
\[Python: working with I/O\] at [Alura](https://www.alura.com.br/).

The code implements methods for:

1. Reading a contacts list from a CSV file (`.data/contacts.csv`)

    - Each line of the CSV file represents one contact in the format `id,name,email`

2. Converting the CSV line into a Python object of the class `Contact`

    - The class is implemented in `contact.py` a an object with attributes `id`, `name`, and `email`

3. Serializing and deserializing the contacts list using `pickle`

4. Serializing and deserializing the contacts list using JSON

## Repository organization

The repository is organized as follows

```txt
./
|-- README.md       : this file
|-- main.py         : main program; run with `python3 main.py`
|-- contact.py      : implements the `Contact` class
|-- contact_utils.py    : implements the methods for handling `Contact` objects
`-- data/           : input and output files
    |-- contacts.csv    : contacts list in CSV format
    `-- contacts.json   : contacts list in JSON format
```

---
