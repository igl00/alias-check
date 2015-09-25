""" Checks a dictionary against instagram users looking for free user names based on 404 response.
    If a 404 is returned the username is not necessarily free as they seem to have an extensive forbidden word list.
"""

import requests
import time
import random
import sys
import os


def url(username):
    return 'https://instagram.com/{}/'.format(username.lower())


def load_dict():
    with open('dictionary_definitions.txt', 'r') as file:
        definitions = file.readlines()

    return definitions


def record_response(word, status, word_len):
    """ Writes the word to different files depending on server response.
    """
    status_codes = {404: 'available.txt', 200: 'unavailable.txt'}

    filename = os.path.join(str(word_len), status_codes.get(status, 'error.txt'))
    catch_all = os.path.join(str(word_len), 'tried.txt')

    with open(catch_all, 'a') as file:
        if status not in status_codes:
            file.write('{} - {}\n'.format(word, status))
        else:
            file.write('{}\n'.format(word))

    with open(filename, 'a') as file:
        file.write('{}\n'.format(word))


def main(word_len=None):
    definitions = [x.strip() for x in load_dict() if x.strip().isalpha()]
    if word_len:
        n_letter_words = [x for x in definitions if len(x) == word_len]
        definitions = n_letter_words

    if not word_len:
        word_len = 'all'
    if not os.path.exists(str(word_len)):
        os.makedirs(str(word_len))

    for word in definitions:
        user_page = url(word)
        headers = {'user-agent': 'instauser/0.0.1'}
        r = requests.get(user_page, headers=headers)

        if r.status_code == 404:
            print(word)

        record_response(word, r.status_code, word_len)

        time.sleep((random.random() * 0.5) + 0.5)  # Rate Limit


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word_length = int(sys.argv[1])
        main(word_length)
    else:
        main()
