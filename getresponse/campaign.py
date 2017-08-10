import datetime


class Campaign(object):
    def __init__(self, *args, **kwargs):
        self.id = args[0]
        self.href = None
        self.name = None
        self.language_code = None
        self.is_default = None
        self.created_on = None
        self.description = None
        self.confirmation = None
        self.profile = None
        self.postal = None
        self.opting_types = None
        self.subscription_notifications = None

    def __repr__(self):
        return "<Campaign(id='{}', name='{}', is_default='{}'>".format(self.id, self.name, self.is_default)


class CampaignManager(object):
    def create(self, obj):
        if isinstance(obj, list):
            _list = []
            for item in obj:
                campaign = self._create(**item)
                _list.append(campaign)
            return _list

        campaign = self._create(**obj)
        return campaign

    def _create(self, *args, **kwargs):
        campaign = Campaign(kwargs['campaignId'])
        if 'href' in kwargs:
            campaign.href = kwargs['href']
        if 'name' in kwargs:
            campaign.name = kwargs['name']
        if 'languageCode' in kwargs:
            campaign.language_code = kwargs['languageCode']
        if 'isDefault' in kwargs:
            campaign.is_default = kwargs['isDefault']
        if 'createdOn' in kwargs:
            created_on = kwargs['createdOn']
            if created_on:
                campaign.created_on = datetime.datetime.strptime(created_on, '%Y-%m-%dT%H:%M:%S%z')
        if 'description' in kwargs:
            campaign.description = kwargs['description']
        if 'confirmation' in kwargs:
            campaign.confirmation = kwargs['confirmation']
        if 'profile' in kwargs:
            campaign.profile = kwargs['profile']
        if 'postal' in kwargs:
            campaign.postal = kwargs['postal']
        if 'optinTypes' in kwargs:
            campaign.opting_types = kwargs['optinTypes']
        if 'subscriptionNotifications' in kwargs:
            campaign.subscription_notifications = kwargs['subscriptionNotifications']
        return campaign
