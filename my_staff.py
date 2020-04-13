from simple_salesforce import Salesforce
from salesforce_sso import login
from collections import namedtuple


def init_sf_credentials():
    """
    When kerberos is not an option or you'd like to use another account, form based auth can be used.
    login should be in format amust\\username
    Password is domain password for account
    """
    credentials = {'login': 'amust\\dmoiseenko', 'password': ''}
    login_result = login(creds=credentials)
    return login_result


def my_query():
    sf = Salesforce(**login_result)
    user_name = sf.restful('chatter/users/me')
    result = sf.query(
        f"Select CaseNumber, Status, Log_Locations__c from Case where Owner.Id='{user_name['id']}' and IsClosed=False ORDER BY CaseNumber Limit 2")

    Sf=namedtuple('Sf', 'l, c')
    Sf.__new__.__defaults__=([],[])
    s=Sf()


    l = []
    #########
    c = []
    #########
    for r in result['records']:
        if r['Log_locations__c'] is not None:
            s.l.append(r['Log_locations__c'].split('\n')[3])
            # l.append(r['Log_locations__c'].split('\n')[3])
        ##########
        if r['CaseNumber'] is not None:
            s.c.append(r['CaseNumber'])
            # c.append(r['CaseNumber'])
        ##########

    return Sf(l, c)


login_result = init_sf_credentials()

x, c = my_query()
for i in x:
    print(i)
#
for j in c:
    print(j)
#
# print(len(x))
# my_query()
