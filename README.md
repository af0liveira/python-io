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

## Running the code

To run the code, simply execute the file `main.py` with a Python 3 interpreter.

```sh
python3 main.py
```

The code was written for study purposes.
All it should do is read the `data/contacts.csv` file and save its contents back in pickle and JSON formats as `data/contacts.p` and `data/contacts.json`.
It then proceeds to read the pickle and JSON files and print their contents on the screen.

> **Warning**
>
> Make sure you trust the content of pickle files before opening them.
> Since they'll restore Python objects, it's fairly easy to insert malicious code into them.

---
