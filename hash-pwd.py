# This file is going to hash and add salt to the password.
# It will then save the hash to a file.
import pwd_gen


class hash_password():
    pwd_gen = pwd_gen.PasswordGenerator()
    password = pwd_gen._get_password()
