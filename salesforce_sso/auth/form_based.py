from salesforce_sso.utils.functions import multi_compose, parse_form, set_credentials, validate_login_succeeded


def setup_form_based_auth(login: str, password: str):
    def setup(requester):
        return multi_compose(
            requester.post,

            # parse login form and insert credentials
            parse_form(xpath_get_form='//form[@action]'),
            set_credentials(login=login, password=password),
            requester.post,
            validate_login_succeeded,

            # redirect back to Salesforce: https://veeam.my.salesforce.com/?so=00D300000000RWR
            parse_form(xpath_get_form='//form')
        )

    return setup
