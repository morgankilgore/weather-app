import requests


def get_request(url, params=None, to_dict=False):
    """
    Sends a GET request to specified URL

    Param(s):
        url (str): Required. URL to send GET request to.
        params (dict): Optional. Parameters to be sent in the query string for the request.
        to_dict (bool): Optional. True to return response as a dictionary, else False. Default False.

    Returns: dict or request object. If 'to_dict' is True a dictionary is returned, else a Request object is returned.
    """
    resp = requests.get(url=url, params=params)
    if to_dict:
        return resp.json()
    return resp


def post_request(url, params=None, json_data=None, to_dict=False):
    """
    Sends a POST request to specified URL

    Param(s):
        url (str): Required. URL to send POST request to.
        params (dict): Optional. Parameters to be send in the query string for the request.
        json_data (dict): Optional. JSON data to send in the body of the request.
        to_dict (bool). True to return response as a dictionary, else False. Default False.

    Returns: dict or request object. If 'to_dict' is True a dictionary is returned, else a Request obejct is returned.
    """
    resp = requests.post(url=url, params=params, json=json_data)
    if to_dict:
        return resp.json()
    return resp
