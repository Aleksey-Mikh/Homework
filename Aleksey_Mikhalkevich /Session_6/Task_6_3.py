"""
Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters
in the alphabet. Add the provided keyword at the begining
of the alphabet. A keyword is used as the key, and it determines
the letter matchings of the cipher alphabet to the plain alphabet.
Repeats of letters in the word are removed, then the cipher alphabet
is generated with the keyword matching to A, B, C etc.
until the keyword is used up, whereupon the rest of the
ciphertext letters are used in alphabetical order,
excluding those already used in the key.

Example:
```
cipher = Cipher("crypto")
cipher.encode("Hello world")
output: "Btggj vjmgp"

cipher.decode("Fjedhc dn atidsn")
output: "Kojima is genius"
```
"""


import string


class Cipher:
    """class which implements encoding and decoding for latin alphabet"""
    encryption_core = string.ascii_lowercase

    def __init__(self, keyword):
        self.keyword = keyword
        self.decryption_core = self._get_decryption_core()
        self._get_cryptographic_dictionaries()

    @staticmethod
    def _get_str_with_only_unique_letters(non_unique_str):
        """
        function which gets non unique string and return string
        with only unique symbols with save the order of follow
        """
        list_with_duplicates = list(non_unique_str.lower())
        unique_list = list(dict.fromkeys(list_with_duplicates))

        return "".join(unique_list)

    def _get_decryption_core(self):
        """
        function which gets the keyword and together with
        the `encryption core` forms the `decryption core` -
        the character sequence will be used in the formation
        of the crypto dictionary.
        """
        unique_keyword = self._get_str_with_only_unique_letters(self.keyword)
        decryption_core_non_unique = unique_keyword + self.encryption_core
        decryption_core = self._get_str_with_only_unique_letters(decryption_core_non_unique)

        return decryption_core

    def _get_cryptographic_dictionaries(self):
        """
        function which make dictionaries to be used
        in encode and decode process
        """
        self.encryption_dictionary = self.decryption_dictionary = {}

        for number, letter in enumerate(self.encryption_core):
            self.encryption_dictionary[letter] = self.decryption_core[number]

        self.decryption_dictionary = {value: key for key, value in self.encryption_dictionary.items()}

    @staticmethod
    def _en_and_de_coding_string(string_for_cipher, cipher_dictionary):
        """function which realizes the encode and decode process"""
        list_of_words = string_for_cipher.split()
        for number, word in enumerate(list_of_words):
            result_word = ''

            for letter in word:
                if letter.isupper():
                    result_word += cipher_dictionary[letter.lower()].upper()
                else:
                    result_word += cipher_dictionary[letter]

            list_of_words[number] = result_word

        return " ".join(list_of_words)

    def encode(self, string_for_cipher):
        """encode string"""
        return self._en_and_de_coding_string(string_for_cipher, self.encryption_dictionary)

    def decode(self, string_for_cipher):
        """decode string"""
        return self._en_and_de_coding_string(string_for_cipher, self.decryption_dictionary)


def main():
    cipher = Cipher('crypto')
    print(cipher.encode("Hello world"))
    print(cipher.decode("Fjedhc dn atidsn"))


if __name__ == '__main__':
    main()
