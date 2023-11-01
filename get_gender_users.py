from get_data import get_data as get
def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    s={}
    l=[]
    for i in data['results']:
        if i['gender']=='male':
           s['Male']=1
           l.append(s)
        elif i['gender']=='female':
           s['Female']=0
           l.append(s)
    return l
print(get_gender_users(get('randomuser_data.json')))