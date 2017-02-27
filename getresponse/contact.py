class Contact(object):
    def __init__(self, *args, **kwargs):
        self.id = args[0]
        self.href = args[1]
        self.name = args[2]
        self.email = args[3]
        self.note = args[4]
        self.day_of_cycle = args[5]
        self.origin = args[6]
        self.created_on = args[7]
        self.changed_on = args[8]
        self.campaign = args[9]
        self.timezone = args[10]
        self.ip_address = args[11]
        self.activities = args[12]
        self.scoring = args[13]


class ContactManager(object):
    def __init__(self):
        self.contacts = {}

    def create(self, obj):
        if isinstance(obj, list):
            _list = []
            for item in obj:
                campaign = self._create(**item)
                self.contacts[campaign.id] = campaign
                _list.append(campaign)
            return _list

        campaign = self._create(**obj)
        self.contacts[campaign.id] = campaign
        return campaign

    def get(self, contact_id):
        return self.contacts.get(contact_id, None)

    def _create(self, *args, **kwargs):
        contact = Contact(
            kwargs['contactId'], kwargs['href'], kwargs['name'], kwargs['email'], kwargs['note'], kwargs['dayOfCycle'],
            kwargs['origin'], kwargs['createdOn'], kwargs['changedOn'], kwargs['campaign'], kwargs['timeZone'],
            kwargs['ipAddress'], kwargs['activities'], kwargs['scoring'])
        return contact
