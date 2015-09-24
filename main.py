"""
Checks instagram's website for existing user names.
"""
import requests
import time
import random


def url(username):
    return 'https://instagram.com/{}/'.format(username.lower())


def load_dict():
    with open('dictionary_definitions.txt', 'r') as file:
        definitions = file.readlines()

    return definitions


def record_response(word, status):
    status_codes = {404: 'available.txt', 200: 'unavailable.txt'}
    filename = status_codes.get(status, 'error.txt')

    with open('tried.txt', 'a') as file:
        file.write('{}\n'.format(word))

    with open(filename, 'a') as file:
        file.write('{}\n'.format(word))


def main():
    definitions = [x.strip() for x in load_dict() if x.strip().isalpha()]
    three_letter_words = [x for x in definitions if len(x) == 3]

    for word in three_letter_words:
        user_page = url(word)
        headers = {'user-agent': 'instauser/0.0.1'}
        r = requests.get(user_page, headers=headers)

        print(word, r.status_code)
        record_response(word, r.status_code)

        time.sleep(random.random(0.5, 1))


if __name__ == '__main__':
    main()