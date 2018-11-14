import requests


def get_request(url, params=None):
    """
    Sends a GET request to specified URL

    Param(s):
        url (str): Required. URL to send GET request to.
        params (dict): Optional. Parameters to be sent in the query string for the request.

    Returns: tuple (bool, dict or str). (True, dict) if successful else (False, str).
    """
    try:
        resp = requests.get(url=url, params=params)
    except requests.exceptions.ConnectionError:
        return False, 'Error in connecting to {}'.format(url)
    else:
        return True, resp.json()


def post_request(url, params=None, json_data=None):
    """
    Sends a POST request to specified URL

    Param(s):
        url (str): Required. URL to send POST request to.
        params (dict): Optional. Parameters to be send in the query string for the request.
        json_data (dict): Optional. JSON data to send in the body of the request.

    Returns: tuple (bool, dict or str). (True, dict) if successful else (False, str).
    """
    try:
        resp = requests.post(url=url, params=params, json=json_data)
    except requests.exceptions.ConnectionError:
        return False, 'Error in connecting to {}'.format(url)
    else:
        return True, resp.json()
