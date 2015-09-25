""" Checks a file of words against a websites users looking for free user names based on 404 response.
    If a 404 is returned the username is not necessarily free as most websites seem to have an extensive
    forbidden word list.
"""

import interfaces
import time
import sys
import os


def load_words(file_name):
    """ Opens the supplied file and returns a list of the line separated words.
    """
    with open(file_name, 'r') as file:
        file_contents = file.readlines()

    words = [word.strip() for word in file_contents]

    return words


def make_directory(file_name, word_length):
    """ Builds a directory based on the input file name and the word length specified. If no word length is specified
        it will just store the output in the folder based on the filename. If a word length is specified and the length
        is between one and twenty, it will replace the number with the word for that number, otherwise, it will use the
        number as a sub-folder to store the results.
    """
    sub_folder_names = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                        9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'}

    folder = file_name.split('.')[0]
    if word_length:
        sub_folder = sub_folder_names.get(word_length, str(word_length))
        path = os.path.join(folder, sub_folder)
    else:
        path = folder

    if not os.path.exists(path):
        os.makedirs(path)

    return path


def record_response(word, responses, path):
    """ Writes the word and response codes in csv form with one item per line in a candidates file.
        There is currently nothing to show which response came from which website but they are in alphabetical
        order from the websites that you used.
    """
    filename = os.path.join(path, 'candidates.txt')

    with open(filename, 'a') as log:
        log.write('{0}, {1}'.format(word, ', '.join([str(n) for n in responses])))


def main(file_name, word_length=None, rate_limit=None):
    words = load_words(file_name)

    if word_length:
        words = [word for word in words if len(word) == int(word_length)]

    path = make_directory(file_name, word_length)

    websites = [interfaces.Instagram(), interfaces.Twitter()]  # In alphabetical order

    for word in words:
        responses = []

        for website in websites:
            website.set_username(word)
            responses.append(website.fetch_profile())

        if 404 in responses:
            record_response(word, responses, path)

        if rate_limit:
            time.sleep(rate_limit)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Please specify a file with line separated words to be checked.')
    else:
        args = sys.argv[1:]
        main(*args)
