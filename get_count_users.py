
from get_data import get_data as get
def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    k=0
    for i in data['results']:
        if i["login"]['username']:
            k+=1
    return k
print(get_count_users(get('randomuser_data.json')))

    
