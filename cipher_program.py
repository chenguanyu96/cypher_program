"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message1.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    # Decrypts or encrypts the message in MSG_FILENAME with the deck of cards
    # specified in DECK_FILENAME. The program will encrypt or decrypt depending
    # on the MODE.
    out_list = cipher_functions.process_messages(cipher_functions.read_deck
                                                 (open(DECK_FILENAME, 'r')),
                                                 cipher_functions.read_messages
                                                 (open(MSG_FILENAME, 'r')),
                                                 MODE)

    # Print each element in the result list from encryption or decryption
    for each_element in out_list:
        print(each_element)

main()
