"""
    Module for checking errors
"""


from .response import Response


def err(**kwargs):
    """
        Checks errors
    """
    message = 'Error message!'
    errors = {}

    meta = {'errors': len(errors)}
    if errors:
        return Response.failed(meta=meta, message=message, errors=errors)
    return False
