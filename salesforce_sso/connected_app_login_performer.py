from salesforce_sso.utils.requester import Requester
from salesforce_sso.utils.functions import multi_compose, extract_url, parse_form, set_credentials, allow_app_access, get_token_and_instance_url, validate_login_succeeded
from salesforce_sso.base_login_performer import LoginPerformerBase


class ConnectedAppLoginPerformer(LoginPerformerBase):
    url_template = 'https://veeam.my.salesforce.com/services/oauth2/authorize?response_type=token' \
                   '&client_id={}' \
                   '&redirect_uri=https://login.salesforce.com/services/oauth2/token'

    def __init__(self, consumer_key: str):
        self._url = self.url_template.format(consumer_key)

    def _compose(self, build_authenticate_func):
        requester = Requester()
        authenticate = build_authenticate_func(requester)

        login_procedure = multi_compose(
            self._compose_login_proc(requester, authenticate),

            # https://veeam--c.na62.content.force.com/secur/contentDoor?*
            extract_url(regex=r'window\.location\.replace\(\"(.*?)\"\)'),
            requester.get,

            # Verify app access form; Allowing access
            parse_form(xpath_get_form='//form'),
            allow_app_access,
            requester.post,

            # parsing token and instance url
            extract_url(regex=r'window\.location\.replace\(\'(.*?)\'\)'),
            get_token_and_instance_url
        )

        return login_procedure

    def login(self, build_authenticate_func):
        login_proc = self._compose(build_authenticate_func)

        session_id, instance_url = login_proc(self._url)
        return {'session_id': session_id, 'instance_url': instance_url}
