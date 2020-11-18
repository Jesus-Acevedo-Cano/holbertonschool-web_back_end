#!/usr/bin/env python3
""" Auth module """
import bcrypt


def _hash_password(password: str) -> str:
    """ takes a pwd string and encrypt it """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
