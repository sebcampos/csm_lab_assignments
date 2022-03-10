# CIS-117 Lab3
# Description
# Group 1, Project 3
# Dillon Anawalt and Sebastian Campos

options = None


def verify_input(user_input: str) -> bool:
    """

    :param user_input:
    :return:
    """
    if user_input in options:
        return True
    return False
