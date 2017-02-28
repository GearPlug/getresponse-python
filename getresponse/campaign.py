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


class CampaignManager(object):
    def __init__(self):
        self.campaigns = {}

    def create(self, obj):
        if isinstance(obj, list):
            _list = []
            for item in obj:
                campaign = self._create(**item)
                self.campaigns[campaign.id] = campaign
                _list.append(campaign)
            return _list

        campaign = self._create(**obj)
        self.campaigns[campaign.id] = campaign
        return campaign

    def get(self, contact_id):
        return self.campaigns.get(contact_id, None)

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
            campaign.created_on = kwargs['createdOn']
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
