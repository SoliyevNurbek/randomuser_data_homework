from get_data import get_data as get
def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    l=[]
    for i in data['results']:
        s={}
        s["first_name"]=i['name']['first']
        s["last_name"]=i['name']['last']
        s["phone_number"]=i['phone']
        l.append(s)
    return l
print(get_users_data(get('randomuser_data.json')))