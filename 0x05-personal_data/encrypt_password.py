#!/usr/bin/env python3
""" Encrypting passwords """
import bcrypt


def hash_password(password: str) -> bytes:
    """ transform to hashed password """
    password = bytes(password, 'utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ validate that the provided password matches the hashed password """
    return bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password)
