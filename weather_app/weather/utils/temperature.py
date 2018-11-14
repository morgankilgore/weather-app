from weather.utils.validation import is_valid_temperature_value


def get_average_temp(temps):
    """
    Calculates an average temperature from a list of temperatures

    Param(s):
        temps (list): List of temperatures

    Returns: tuple(bool, float or str).  (True, average_temperature) else (False, error)
    """
    total_temp = 0

    for temp in temps:
        if not is_valid_temperature_value(temp):
            return False, 'Invalid temperature value'
        total_temp += float(temp)
    return True, total_temp / len(temps)
