"""
This file will generate a random password.
"""
import random


class PasswordGenerator:
    """
    This is the main class for the generator
    """

    def __init__(self) -> None:
        print("Welcome to the password generator.")

        self._password_length = 0
        self._password = ""
        self._allowed_classes = {
            "alpha": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "digits": "0123456789",
            "symbols": "!@#$%^&*()_+-=[]{}<>?|\\:;'\".,/"
        }

        self.ask_password_length()
        (self._alpha, self._numbers,
         self._symbols) = self._ask_allowed_characters()

    def _get_password_length(self):
        return self._password_length

    def _set_password_length(self, length):
        self._password_length = length

    def ask_password_length(self) -> None:
        """
This is a helper function that will be used to generate a random password.
ask the user for the password length
        """
        # ask the user for the password length
        while True:
            password_length = input(
                "Please enter the length of the password: ")
            # check if the user entered a good value
            if self._verify_password_length(password_length):
                # if the user entered a good value, then store it
                self._set_password_length(password_length)
                break

    def _verify_password_length(self, password_length):
        return_value = False
        if not password_length.isdigit():
            # if the user entered a non-numeric value, then ask again
            print("You must enter a number.")
        elif int(password_length) < 8:
            # if the user entered a number that is less than 8, then ask again
            print("The password must be at least 8 characters long.")
        else:
            # the user entered a good value
            return_value = True

        return return_value

    def generate_password(self) -> str:
        """This function will generate a random password."""
        allowed_characters = ''
        if self._alpha:
            allowed_characters += self._allowed_classes["alpha"]
        if self._numbers:
            allowed_characters += self._allowed_classes["digits"]
        if self._symbols:
            allowed_characters += self._allowed_classes["symbols"]

        password = ''.join(random.choice(allowed_characters)
                           for _ in range(int(self._get_password_length())))
        # save the password
        self._set_password(password)
        return password

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = password

    def _verify_yn(self, char):
        return char.lower() == "y" or char.lower() == "n"

    def _ask_allowed_characters(self):
        alpha = True

        # ask the user which characters are allowed in the password
        while True:
            char = input("Do you want to include numbers? (y/n): ")
            if self._verify_yn(char):
                numbers = char.lower() == "y"
                break

        while True:
            char = input("Do you want to include symbols? (y/n): ")
            if self._verify_yn(char):
                symbols = char.lower() == "y"
                break

        return alpha, numbers, symbols


if __name__ == '__main__':
    pwd_gen = PasswordGenerator()
    PASSWORD = pwd_gen.generate_password()
    print("Your password is: " + PASSWORD)
