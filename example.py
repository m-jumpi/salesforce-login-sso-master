# from simple_salesforce import Salesforce
# from salesforce_sso import login
#
#
# def test_query(login_result):
#     sf = Salesforce(**login_result)

    # result = sf.search("FIND {00532000004zYZSAA2}")
    # print(result)

    # result = sf.query("select Id, Name, FirstName, OwnerId from Contact where Name='Denis Moiseenko'")
    # print(result)

    # result = sf.query("select Id from User where Name='Denis Moiseenko'")
    # print(result)

    # result = sf.query("select Id, Alias, UserName from User where Name='Denis Moiseenko'")
    # print(result)

    # result = sf.query("Select Id, CaseNumber, OwnerId, IsClosed, Status, Owner.Name from Case where OwnerID='00532000004zYZSAA2' and IsClosed=False Limit 1")
    # for r in result['records']:
    #     print(r)

    # print(login_result)
    # result = sf.query(
    #     "Select Id, CaseNumber, OwnerId, IsClosed, Status, Log_Locations__c from Case where Owner.Name='Denis Moiseenko' and IsClosed=False Limit 1")
    # for r in result['records']:
    #     print(r)
    #     print('\n')
    #     print(((r['Log_locations__c']).split('\n'))[3])

    # print(login_result)

    # result = sf.query(
    #     "Select CaseNumber, Status, Log_Locations__c from Case where Owner.Id='00532000004zYZSAA2' and IsClosed=False")
    # l = []
    # for r in result['records']:
    #     # print(r)
    #     # print('\n')
    #     if r['Log_locations__c'] is not None:
    #         l.append(r['Log_locations__c'].split('\n')[3])
    # return l


# def init_sf_kerberos():
#     """
#     When started using amust domain account, kerberos auth can be used, no credentials required
#     """
#     login_result = login()
#     test_query(login_result)


# def init_sf_credentials():
#     """
#     When kerberos is not an option or you'd like to use another account, form based auth can be used.
#     login should be in format amust\\username
#     Password is domain password for account
#     """
#     credentials = {'login': 'amust\\dmoiseenko', 'password': 'mj_2327_AJ_#23'}
#     login_result = login(creds=credentials)
#     return login_result
#    test_query(login_result)


# init_sf_kerberos()
# init_sf_credentials()
