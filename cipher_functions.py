# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28
BASE_ASCII_VALUE = ord('A')
LETTERS_IN_ALPHA = 26


def clean_message(message):
    '''(str) -> str
    Return the input str (message) all capitalized and all non-alphabetical
    letters are deleted.
    >>> clean_message("Josh is 45 years old")
    'JOSHISYEARSOLD'
    >>> clean_message("Hello World")
    'HELLOWORLD'
    >>> clean_message("Kevin's apple")
    'KEVINSAPPLE'
    '''
    # Go through all the letters in the message and deletes any spaces or
    # anyting that is non- alphabetical
    for each_char in message:
        if(each_char.isalpha() is False):
            message = message.replace(each_char, '')

    # Delete all spaces found in message
    message = message.replace(' ', '')

    # Capitalize all letters in the message
    message = message.upper()
    return message


def encrypt_letter(single_character, keystream_value):
    '''(str, int) -> str
    Encrypts a single letter with a given keystream value. If the keystream
    value is greater than 26, it will loop back to the beginning of the
    alphabet and continue.
    >>> encrypt_letter('d', 11)
    'O'
    >>> encrypt_letter('h', 20)
    'B'
    >>> encrypt_letter('f', 47)
    'A'
    '''
    # Makes the character uppercase if not already
    single_character = single_character.upper()

    # Find the index of the character by getting the ASCII value of the
    # character and subtracting from the base value (letter A which is 65)
    index_schar = ord(single_character) - BASE_ASCII_VALUE

    # Performs the computation in order to encrypt the letter with the
    # given keystream value
    final_index = index_schar + keystream_value

    # If the final_index is greater than 25, it will be subtracted by 26
    # in order to not go out of the alphabet
    final_index %= LETTERS_IN_ALPHA

    # Find the letter to be encrypted to the single_character and returns the
    # encrypted letter
    return chr(final_index + BASE_ASCII_VALUE)


def decrypt_letter(upper_single_char, keystream_value):
    '''(str, int) -> str
    Decrypts a single letter with a given keystream value. If the keystream
    value is greater than 26, it will loop back to the beginning of the
    alphabet and continue.
    REQ: upper_single_char must be uppercase
    >>> decrypt_letter('D', 11)
    'S'
    >>> decrypt_letter('E', 43)
    'N'
    '''
    # Find the index of the character (upper_single_char) in order to perform
    # the decryption
    index_us_char = ord(upper_single_char) - BASE_ASCII_VALUE

    # Perform the decryption of the single letter
    final_index = index_us_char - keystream_value

    # Check if the final index is below 0 in order to not go out of the
    # alphabet
    final_index %= LETTERS_IN_ALPHA

    # Return the decrypted letter
    return chr(final_index + BASE_ASCII_VALUE)


def swap_cards(deck_of_cards, index_into_deck):
    '''(list of int, int) -> NoneType
    Swap the card and index (index_into_deck) with the card after it; Mutates
    deck_of_cards *IN PLACE*.
    >>> test_list = [1, 2, 3, 4]
    >>> swap_cards(test_list, 3)
    >>> test_list == [4, 2, 3, 1]
    True
    >>> test_list = [1, 2, 3, 4, 5]
    >>> swap_cards(test_list, 3)
    >>> test_list == [1, 2, 3, 5, 4]
    True
    >>> test_list = [1, 2, 3, 4, 5, 6]
    >>> swap_cards(test_list, 10)
    >>> test_list == [1, 2, 3, 4, 6, 5]
    True
    '''
    # Treat deck as circular
    if(index_into_deck > len(deck_of_cards)):
        index_into_deck %= deck_of_cards[len(deck_of_cards)-1]

    # If the card at index_into_deck is the last card, the first card will be
    # swapped with the last one. Treat the deck as circular.
    if(deck_of_cards[index_into_deck] == deck_of_cards[len(deck_of_cards)-1]):
        (deck_of_cards[index_into_deck],
         deck_of_cards[0]) = (deck_of_cards[0], deck_of_cards[index_into_deck])

    # Swap the card after the index_into_deck card, this will work anywhere in
    # the deck except for the last card
    else:
        (deck_of_cards[index_into_deck],
         deck_of_cards[index_into_deck+1]) = (deck_of_cards[index_into_deck+1],
                                              deck_of_cards[index_into_deck],)


def move_joker_1(deck_of_cards):
    '''(list of int) -> NoneType
    Finds JOKER1 in the deck and swap it with the card that follows it. If
    the card is at the end of the deck, it will be swapped with the first
    card. Mutates deck_of_cards *IN PLACE*.
    >>> test_list = [1, 2, 3, 4, 5, 27, 9, 8]
    >>> move_joker_1(test_list)
    >>> test_list == [1, 2, 3, 4, 5, 9, 27, 8]
    True
    >>> test_list = [1, 4, 6, 8, 3, 27]
    >>> move_joker_1(test_list)
    >>> test_list == [27, 4, 6, 8, 3, 1]
    True
    '''
    # Find JOKER1 in the deck of cards and get index
    for each_card in deck_of_cards:
        if(each_card == JOKER1):
            card_index = deck_of_cards.index(each_card)

    # Use previous swap_cards function to swap the card
    swap_cards(deck_of_cards, card_index)


def move_joker_2(deck_of_cards):
    '''(list of int) -> NoneType
    Move the JOKER2 two places down the deck; mutates the deck *IN PLACE*.
    >>> test_list = [1, 5, 7, 8, 4, 28, 6, 7, 11, 3]
    >>> move_joker_2(test_list)
    >>> test_list == [1, 5, 7, 8, 4, 6, 7, 28, 11, 3]
    True
    >>> test_list = [1, 5, 7, 8, 4, 14, 6, 7, 28, 3]
    >>> move_joker_2(test_list)
    >>> test_list == [28, 5, 7, 8, 4, 14, 6, 7, 3, 1]
    True
    >>> test_list = [1, 5, 7, 8, 4, 14, 6, 7, 18, 28]
    >>> move_joker_2(test_list)
    >>> test_list == [5, 28, 7, 8, 4, 14, 6, 7, 18, 1]
    True
    '''
    # Find JOKER2 in the deck in order to get its index
    for each_card in deck_of_cards:
        if(each_card == JOKER2):
            card_index = deck_of_cards.index(each_card)

    # Swap the card once after the first time finding JOKER2's index in the
    # deck
    swap_cards(deck_of_cards, card_index)

    # Finds the index of JOKER2 after one swap to do the second swap
    for each_card in deck_of_cards:
        if(each_card == JOKER2):
            card_index = deck_of_cards.index(each_card)
    swap_cards(deck_of_cards, card_index)


def triple_cut(deck_of_cards):
    '''(list of int) -> NoneType
    Everyting before the first joker that appears will be moved to the bottom
    of the deck, everything after the second joker that appears will be moved
    to the top of the deck. Mutates the deck in place *IN PLACE*.
    >>> test_list = [27, 4, 8, 28]
    >>> triple_cut(test_list)
    >>> test_list == [27, 4, 8, 28]
    True
    >>> test_list = [1, 3, 28, 7, 10, 27, 14, 12, 11]
    >>> triple_cut(test_list)
    >>> test_list ==[14, 12, 11, 28, 7, 10, 27, 1, 3]
    True
    >>> test_list = [1, 3, 5, 28, 7, 15, 27, 1]
    >>> triple_cut(test_list)
    >>> test_list ==[1, 28, 7, 15, 27, 1, 3, 5]
    True
    '''
    # Store the index of the jokers found
    index_of_jokers = []

    # Find the joker and store the index in the list index_of_jokers so
    # that the triple cut could be performed
    for each_element in deck_of_cards:

        # Get the index of whichever joker comes first in the deck, it will
        # eventually get the index of both jokers in the deck
        if(each_element == JOKER1 or each_element == JOKER2):

            # Store the index of both jokers (in order) in the list
            # (index_of_jokers)
            index_of_jokers.append(deck_of_cards.index(each_element))

    # Create 2 sub-list for the sections of the list to be swapped
    temp_one = deck_of_cards[:index_of_jokers[0]]
    temp_two = deck_of_cards[index_of_jokers[1]+1:]

    # Delete the everything after the last joker in order to replace it with
    # the new element
    del deck_of_cards[index_of_jokers[1]+1:]

    # Swap the 2 section of the deck; before the first joker and after the
    # second joker
    deck_of_cards[:index_of_jokers[0]] = temp_two
    deck_of_cards[len(deck_of_cards):len(deck_of_cards)] = temp_one


def insert_top_to_bottom(deck_of_cards):
    '''(list of int) -> NoneType
    According to last card in the deck, move that many cards from the top of
    the deck to the bottom, inserting before the last card of the deck.
    If the last card is JOKER2, use JOKER1. Mutates the deck *IN PLACE*.
    >>> test_list = [1, 2, 27, 3, 28, 4, 5]
    >>> insert_top_to_bottom(test_list)
    >>> test_list == [4, 1, 2, 27, 3, 28, 5]
    True
    >>> test_list = read_deck(open('deck1.txt', 'r'))
    >>> insert_top_to_bottom(test_list)
    >>> test_list == [23, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,
    ... 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26]
    True
    '''
    # Get the number of cards to be moved from the top of the deck
    number_of_cards_to_move = deck_of_cards[len(deck_of_cards)-1]

    # Test if the card is JOKER2, if it is, change it to JOKER1
    if(number_of_cards_to_move == JOKER2):
        number_of_cards_to_move = JOKER1

    # Insert the cards to be moved from the top of the deck to right before the
    # last card of the deck
    if(deck_of_cards[len(deck_of_cards)-1] > len(deck_of_cards)):
        number_of_cards_to_move %= len(deck_of_cards)
    for each_element in range(0, number_of_cards_to_move):
        deck_of_cards.insert(len(deck_of_cards)-1,
                             deck_of_cards[each_element])

    # Delete the card moved from the top of the deck
    del deck_of_cards[:number_of_cards_to_move]


def get_card_at_top_index(deck_of_cards):
    '''(list of int) -> int
    Read the first card of the deck and use it as an index. Return the value of
    the card at that index. If the first card is JOKER2, it uses JOKER1 as the
    index. Mutates the deck
    >>> get_card_at_top_index([2, 1, 5, 4, 3])
    5
    >>> get_card_at_top_index([28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    ... 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])
    27
    '''
    # Get the index value to find the keystream value
    index_to_look = deck_of_cards[0]

    # Check if card is a JOKER2, if it is, uses JOKER1 as the index
    if(index_to_look == JOKER2):
        index_to_look = JOKER1

    # Return the value of the card at the index (index_to_look)
    return deck_of_cards[index_to_look]


def get_next_value(deck_of_cards):
    '''(list of int) -> int
    Returns the potential keystream value; no restrictions set on the keystream
    value in this function.
    >>> get_next_value(read_deck(open('deck1.txt', 'r')))
    11
    >>> deck = read_deck(open('deck1.txt', 'r'))
    >>> for number in range(0, 10):
    ...     ksv = get_next_value(deck)
    ...
    >>> print(ksv)
    27
    '''
    # Call of 5 steps of the algorithm and gets a potential keystream value
    move_joker_1(deck_of_cards)
    move_joker_2(deck_of_cards)
    triple_cut(deck_of_cards)
    insert_top_to_bottom(deck_of_cards)
    pot_keystream_value = get_card_at_top_index(deck_of_cards)

    # Return the potential keystream value; no restrictions on keystream value
    return pot_keystream_value


def get_next_keystream_value(deck_of_cards):
    '''(list of int) -> int
    Returns a valid keystream value, anything greater than 26 returned will be
    re-evaluated and returns a new keystream value.
    >>> deck = read_deck(open('deck1.txt', 'r'))
    >>> for number in range(0, 10):
    ...     ksv = get_next_value(deck)
    ...
    >>> ksv == 27
    True
    >>> deck = read_deck(open('deck1.txt', 'r'))
    >>> for number in range(0, 10):
    ...     real_ksv = get_next_keystream_value(deck)
    ...
    >>> real_ksv == 8
    True
    '''
    # Try to get a valid keystream value under or equal to 26
    keystream_value = get_next_value(deck_of_cards)

    # Re-evaluate the keystream value if the keystream value is greater than
    # 26
    while(keystream_value > LETTERS_IN_ALPHA):
        keystream_value = get_next_value(deck_of_cards)
    return keystream_value


def process_message(deck_of_cards, message, enc_or_dec):
    '''(list of int, str, str) -> str
    Returns either the encrypted or decrypted message according to the mode
    (enc_or_dec; "e" for encryption, "d" for decryption).
    REQ: enc_or_dec have to either "d" or "e"
    >>> process_message(read_deck(open('deck1.txt', 'r')), 'Kevin Chen', 'e')
    'VNSPXBSPU'
    >>> process_message(read_deck(open('deck1.txt', 'r')), 'VNSPXBSPU', 'd')
    'KEVINCHEN'
    >>> process_message(read_deck(open('deck1.txt', 'r')), 'I won the lottery!'
    ... , 'e')
    'TFLUDGPWVBCPCY'
    '''
    # Declare a empty string in order to concat single letters (encrypted or
    # decrypted)
    return_str = ''

    # Code to be ran if the mode (enc_or_dec) is "e" for encrypt
    if(enc_or_dec == 'e'):

        # Clean up the message and capitalizes all the alphabetical characters,
        # non-alphabetical characters are all removed
        message = clean_message(message)

        # Get the number of characters in the message in order to know how many
        # keystream values need to be generated
        num_of_ksv = len(message)

        # Control the amount of keystream values generated. This will encrypt
        # one letter at a time in a message
        for letter in range(0, num_of_ksv):

            # Generate one keystream value for the letter to be encrypted
            keystream_value = get_next_keystream_value(deck_of_cards)

            # Encrypt the letter using the keystream value generated
            enc_letter = encrypt_letter(message[letter], keystream_value)

            # Concat or adds all of the encrypted characters to a string that
            # will result in the final encrypted string
            return_str += enc_letter

    # Block of code that runs if the mode (enc_or_dec) is "d" for decrypt
    elif(enc_or_dec == 'd'):

        # Get the number of characters in a encrypted message in order to know
        # how many keystream values need to be generated
        num_of_ksv = len(message)

        # Control the number of keystream values
        for letter in range(0, num_of_ksv):

            # Generate one keystream value for the letter to be decrypted
            keystream_value = get_next_keystream_value(deck_of_cards)

            # Decrypt one letter using the keystream value generated
            dec_letter = decrypt_letter(message[letter], keystream_value)

            # Concat decrypted letters to a string that will result in the
            # decrypted message
            return_str += dec_letter
    return return_str


def process_messages(deck_of_cards, list_of_msg, enc_or_dec):
    '''(list of int, list of str, str) -> list of str
    Returns a list of either encrypted or decrypted messages depending on the
    mode (enc_or_dec).
    REQ: list_of_msg have to be a list
    >>> process_messages(read_deck(open('deck1.txt', 'r')), read_messages(open
    ... ('secret1.txt', 'r')), 'd')
    ['THISISITTHEMASTERSWORD', 'NOTHISCANTBEITTOOBAD']
    '''
    # Final list of the lines that have been encrypted or decrypted
    end_list = []

    # Decrypts or encrypts the lines in the list depending on the mode
    # (enc_or_dec)
    for each_message in list_of_msg:

        # Encrypts or decrpyts the message depending on the mode (enc_or_dec)
        end_list.append(process_message(deck_of_cards, each_message,
                                        enc_or_dec))
    return end_list


def read_messages(file_opened):
    '''(io.TextIOWrapper) -> list of str
    Returns a list of the lines in the file and any leading or trailing
    whitespace.
    >>> read_messages(open('message1.txt', 'r'))
    ['This is it! The master sword!', "No, this can't be it. Too bad."]
    '''
    # Appends the stripped lines in the new list to be returned
    message_final = []

    # Read the file for the encrypted or decrypted message
    raw_message = file_opened.readlines()

    # Strips any newlines and/or whitespaces
    for each_element in raw_message:
        parts = each_element.strip()
        message_final.append(parts)
    return message_final


def read_deck(file_opened):
    '''(io.TextIOWrapper) -> list of int
    Returns a list of int by reading off a file the card order. This returns
    the deck.
    '''
    # Empty list for storing the new deck
    deck = []

    # This is the original deck (list) after reading from file
    raw_deck = file_opened.readlines()

    # Split all elements of the list by whitespaces in order to get it
    # separate. This will return a list of str.
    for each_element in raw_deck:
        parts = each_element.strip().split()
        deck += parts

    # Cast all elements in deck to a int, it was a string originally
    deck = [int(each_element) for each_element in deck]
    return deck
