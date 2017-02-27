import logging
import requests
from getresponse.enums import HttpMethod
from .account import Account
from .campaign import CampaignManager
from .contact import ContactManager
from .excs import UniquePropertyError, NotFoundError

logging.basicConfig(level=logging.INFO)

campaign_manager = CampaignManager()
contact_manager = ContactManager()


class GetResponse(object):
    API_BASE_URL = 'https://api.getresponse.com/v3'
    TIMEOUT = 8

    def __init__(self, *args, **kwargs):
        self.api_key = args[0]
        self.session = requests.Session()

        self.session.headers.update({
            'X-Auth-Token': 'api-key {}'.format(self.api_key),
            'Content-Type': 'application/json'
        })

    def accounts(self):
        return self._request('/accounts')

    def ping(self):
        return True if self.accounts() else False

    def get_campaigns(self):
        return self._request('/campaigns')

    def get_campaign(self, campaign_id):
        return self._request('/campaigns/{}'.format(campaign_id))

    def update_campaign(self, campaign_id):
        raise NotImplementedError

    def get_campaign_contacts(self, campaign_id):
        raise NotImplementedError

    def create_campaign(self, body):
        return self._request('/campaigns', HttpMethod.POST, body)

    def get_contacts(self):
        return self._request('/contacts')

    def get_contact(self, contact_id):
        return self._request('/contacts/{}'.format(contact_id))

    def create_contact(self, body):
        return self._request('/contacts', HttpMethod.POST, body)

    def update_contact(self, contact_id):
        raise NotImplementedError

    def delete_contact(self, contact_id):
        return self._request('/contacts/{}'.format(contact_id), HttpMethod.DELETE)

    def get_rss_newsletter(self, rss_newsletter_id):
        raise NotImplementedError

    def send_newsletter(self, body):
        return NotImplementedError

    def get_webforms(self, webform_id):
        return NotImplementedError

    def get_forms(self, form_id):
        return NotImplementedError

    def get_custom_fields(self):
        return NotImplementedError

    def set_custom_fields(self, body):
        return NotImplementedError

    def _request(self, api_method, http_method=HttpMethod.GET, body=None):
        if http_method == HttpMethod.GET:
            response = self.session.get(self.API_BASE_URL + api_method, timeout=self.TIMEOUT)
            if response.status_code != 200:
                return None
            if '/accounts' in api_method:
                obj = Account(**response.json())
            elif '/campaigns' in api_method:
                obj = campaign_manager.create(response.json())
            elif '/contacts' in api_method:
                obj = contact_manager.create(response.json())
            return obj

        if http_method == HttpMethod.POST:
            response = self.session.post(self.API_BASE_URL + api_method, json=body, timeout=self.TIMEOUT)
            if response.status_code == 400:
                error = response.json()
                if error['code'] == 1001:
                    raise NotFoundError(error['message'])
            if response.status_code == 409:
                # Error cuando el ID no es único.
                error = response.json()
                raise UniquePropertyError(error['message'])
            if response.status_code == 202:
                # Respuesta exitosa para un objeto que no se crea inmediatamente.
                return True
            if '/campaigns' in api_method:
                obj = campaign_manager.create(response.json())
            elif '/contacts' in api_method:
                obj = contact_manager.create(response.json())
            return obj

        if http_method == HttpMethod.DELETE:
            response = self.session.delete(self.API_BASE_URL + api_method, timeout=self.TIMEOUT)
            if response.status_code == 204:
                # Respuesta exitosa para un objeto que no se borra inmediatamente.
                return True
            return None
