"""
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """

from json import loads
def get_data(filename:str) -> dict:
    f=loads(open(filename, 'r', encoding='UTF8').read())
    return f