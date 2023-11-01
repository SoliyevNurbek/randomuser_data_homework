from get_data import get_data as get
def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    l=[]
    for i in data['results']:
        l.append(i.get('email'))
    return l
print(get_email(get('randomuser_data.json')))