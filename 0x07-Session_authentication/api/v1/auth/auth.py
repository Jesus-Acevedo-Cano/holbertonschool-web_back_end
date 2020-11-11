#!/usr/bin/env python3
""" class to manage the API authentication """

from flask import request
from typing import TypeVar, List
import os


class Auth:
    """ class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method """
        if path is not None and path[len(path) - 1] != '/':
            path += '/'
        if excluded_paths is None or excluded_paths == []:
            return True
        if path not in excluded_paths or path is None:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """ public method """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method """
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
