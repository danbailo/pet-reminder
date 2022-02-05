import json


def load_json(path: str) -> dict:
    with open(path, 'r') as file:
        return json.load(file)


def get_recipients_from_txt():
    with open('recipients_emails.txt', 'r') as file:
        return file.readlines()
