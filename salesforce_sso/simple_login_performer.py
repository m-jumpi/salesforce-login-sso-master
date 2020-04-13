from salesforce_sso.utils.requester import Requester
from salesforce_sso.utils.functions import multi_compose, extract_url, parse_form
from salesforce_sso.base_login_performer import LoginPerformerBase


class SimpleLoginPerformer(LoginPerformerBase):
    url_default = 'https://veeam.my.salesforce.com/a6n'
    default_instance_url = 'https://veeam.my.salesforce.com'

    def __init__(self,
                 url: str = url_default,
                 instance_url: str = default_instance_url):
        self._url = url
        self._instance_url = instance_url

    def _compose(self, build_authenticate_func):
        requester = Requester()
        authenticate = build_authenticate_func(requester)

        login_procedure = multi_compose(
            self._compose_login_proc(requester, authenticate),

            # Session id is located in sid cookie for domain veeam.my.salesforce.com
            lambda r: requester.get_session_cookie(name="sid", domain="veeam.my.salesforce.com")
        )

        return login_procedure

    def login(self, build_authenticate_func):
        login_proc = self._compose(build_authenticate_func)

        session_id = login_proc(self._url)
        return {'session_id': session_id, 'instance_url': self._instance_url}
