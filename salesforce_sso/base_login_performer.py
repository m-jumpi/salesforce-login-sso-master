from salesforce_sso.utils.functions import multi_compose, parse_form, extract_url


class LoginPerformerBase:
    def _compose_login_proc(self, requester, authenticate):
        return multi_compose(
            # input url
            requester.get,

            # https://veeam.my.salesforce.com/saml/authn-request.jsp*
            extract_url(regex=r'\'(/saml/.*?)\''),
            requester.get,

            # redirect form from SF to https://adfs.veeam.com/adfs/ls
            parse_form(xpath_get_form='//form'),

            authenticate,

            # back to SF
            requester.post
        )

    def login(self, build_authenticate_func):
        """
        Abstract method
        """
        raise NotImplementedError("Abstract method called")
