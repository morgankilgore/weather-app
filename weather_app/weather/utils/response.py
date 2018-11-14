from django.http import JsonResponse


def create_json_response(content, status_code=200):
    """
    Creates a JSON response

    Param(s):
        content (dict): Content of the response
        status_code (int): HTTP status code

    Returns: django.http.JsonResponse object
    """
    if status_code in range(200, 300):
        content['status'] = 'success'
    else:
        content['status'] = 'error'

    return JsonResponse(content, status=status_code)
