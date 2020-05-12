import datetime


class Contact(object):
    def __init__(self, *args, **kwargs):
        self.id = args[0]
        self.href = None
        self.name = None
        self.email = None
        self.note = None
        self.day_of_cycle = None
        self.origin = None
        self.created_on = None
        self.changed_on = None
        self.campaign = None
        self.timezone = None
        self.ip_address = None
        self.activities = None
        self.scoring = None
        self.custom_field_values = None
        self.tags = None
        self.engagement_score = None

    def __repr__(self):
        return "<Contact(id='{}', name='{}', email='{}'>".format(self.id, self.name, self.email)


class ContactManager(object):
    def __init__(self, *args, **kwargs):
        self.campaign_manager = args[0]

    def create(self, obj):
        if isinstance(obj, list):
            _list = []
            for item in obj:
                contact = self._create(**item)
                _list.append(contact)
            return _list

        contact = self._create(**obj)
        return contact

    def _create(self, *args, **kwargs):
        contact = Contact(kwargs['contactId'])
        if 'href' in kwargs:
            contact.href = kwargs['href']
        if 'name' in kwargs:
            contact.name = kwargs['name']
        if 'email' in kwargs:
            contact.email = kwargs['email']
        if 'note' in kwargs:
            contact.note = kwargs['note']
        if 'dayOfCycle' in kwargs:
            contact.day_of_cycle = kwargs['dayOfCycle']
        if 'origin' in kwargs:
            contact.origin = kwargs['origin']
        if 'createdOn' in kwargs:
            created_on = kwargs['createdOn']
            if created_on:
                contact.created_on = datetime.datetime.strptime(
                    created_on, '%Y-%m-%dT%H:%M:%S%z')
        if 'changedOn' in kwargs:
            changed_on = kwargs['changedOn']
            if changed_on:
                contact.changed_on = datetime.datetime.strptime(
                    changed_on, '%Y-%m-%dT%H:%M:%S%z')
        if 'campaign' in kwargs:
            campaign = self.campaign_manager.create(kwargs['campaign'])
            contact.campaign = campaign
        if 'timeZone' in kwargs:
            contact.timezone = kwargs['timeZone']
        if 'ipAddress' in kwargs:
            contact.ip_address = kwargs['ipAddress']
        if 'activities' in kwargs:
            contact.activities = kwargs['activities']
        if 'scoring' in kwargs:
            contact.scoring = kwargs['scoring']
        if 'customFieldValues' in kwargs:
            contact.custom_field_values = kwargs['customFieldValues']
        if 'tags' in kwargs:
            contact.tags = kwargs['tags']
        if 'engagementScore' in kwargs:
            contact.engagement_score = kwargs['engagementScore']
        return contact
