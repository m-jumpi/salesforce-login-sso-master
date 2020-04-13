from salesforce_sso.simple_login_performer import SimpleLoginPerformer
from salesforce_sso.connected_app_login_performer import ConnectedAppLoginPerformer
from salesforce_sso.auth import setup_form_based_auth


def login(creds: dict = None, consumer_key: str = None):
    """
    :param creds:
    For kerberos auth leave argument None

    For explicit authentication provide dictionary with
    login = amust login, Example amust\vpupkin
    password = amust password

    :param consumer_key:
    To use Salesforce connected app, provide consumer key
    To skip connected app usage, leave None value

    :return:
    returns login result dictionary with session_id and instance_url values.
    To use it with simple salesforce: sf = Salesforce(**login_result)
    """
    auth = build_auth(creds)
    login_performer = build_login_performer(consumer_key)

    return login_performer.login(auth)


def build_auth(creds: dict):
    if creds:
        return setup_form_based_auth(**creds)
    #return setup_kerberos_auth()


def build_login_performer(consumer_key: str = None):
    if consumer_key:
        return ConnectedAppLoginPerformer(consumer_key)
    return SimpleLoginPerformer()
