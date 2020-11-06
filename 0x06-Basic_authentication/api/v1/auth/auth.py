#!/usr/bin/env python3
""" class to manage the API authentication """

from flask import request
from typing import TypeVar, List


class Auth:
    """ class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method """
        if path not in excluded_paths or path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """ public method """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method """
        return None
