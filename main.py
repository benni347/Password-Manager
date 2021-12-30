#!/usr/bin/env python
# This is my portable password manager.
# It is a simple program that stores passwords in a file.
# It is meant to be used with a terminal.

import pwd_gen

pwd_gen = pwd_gen.PasswordGenerator()
password = pwd_gen.generate_password()
