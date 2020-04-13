from functional import partial
import functools
import re
from urllib.parse import urlparse, unquote
from lxml import html


def compose(func1, func2):
    def composition(*args, **kwargs):
        inner_result = func2(*args, **kwargs)
        if isinstance(inner_result, tuple):
            return func1(*inner_result)
        return func1(inner_result)

    return composition


def multi_compose(*functions):
    args_reversed = functions[::-1]
    return partial(functools.reduce, compose)(args_reversed)


def set_credentials(login: str, password: str):
    def do_set_credentials(url: str, data: dict):
        data['UserName'] = login
        data['Password'] = password
        data['AuthMethod'] = 'FormsAuthentication'
        return url, data

    return do_set_credentials


def extract_url(regex):
    def do_extract_url(response):
        url = re.search(regex, response.text).group(1)
        return compose_abs_url(response.url, url)

    return do_extract_url


def compose_abs_url(request_url, url_to_compose):
    if url_to_compose[0] == '/':
        url_base = "{uri.scheme}://{uri.netloc}".format(uri=urlparse(request_url))
        return url_base + url_to_compose
    return url_to_compose


def parse_form(xpath_get_form='//form'):
    def do_parse_form(response):
        doc = html.fromstring(response.content)
        form = doc.xpath(xpath_get_form)[0]

        action_url = compose_abs_url(response.url, form.action)
        submit_data = {}

        to_post_fields = form.xpath('//input[@name][@value]')
        for field in to_post_fields:
            submit_data[field.name] = field.value

        return action_url, submit_data

    return do_parse_form


def allow_app_access(url: str, data: dict):
    updated_data = dict(data)
    updated_data['save'] = ' Allow '

    return url, updated_data


def get_token_and_instance_url(url: str):
    url = unquote(url)
    token = re.search('access_token=(.*?)&', url).group(1)
    instance_url = re.search('instance_url=(.*?)&', url).group(1)

    return token, instance_url


def validate_login_succeeded(response):
    doc = html.fromstring(response.content)
    form = doc.xpath('//form')[0]

    login_successful = "salesforce.com" in form.action
    if not login_successful:
        raise InvalidCredentialsError("Incorrect user ID or password")

    return response


class InvalidCredentialsError(Exception):
    pass
