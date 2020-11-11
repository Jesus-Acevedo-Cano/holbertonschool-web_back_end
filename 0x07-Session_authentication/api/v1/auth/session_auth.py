#!/usr/bin/env python3
""" Module of session auth
"""
from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ session auth class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create session id """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
