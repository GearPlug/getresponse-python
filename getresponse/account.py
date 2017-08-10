class Account(object):
    def __init__(self, *args, **kwargs):
        self.id = args[0]
        self.first_name = None
        self.last_name = None
        self.email = None
        self.phone = None
        self.company_name = None
        self.state = None
        self.city = None
        self.zip_code = None
        self.country_code = None
        self.industry_tag = None
        self.number_of_employees = None
        self.time_format = None
        self.href = None

    @property
    def name(self):
        return '{} {}'.format(self.first_name or '', self.last_name or '')

    def __repr__(self):
        return "<Account(id='{}', name='{}', email='{}'>".format(self.id, self.name, self.email)


class AccountManager(object):
    def create(self, obj):
        if isinstance(obj, list):
            _list = []
            for item in obj:
                account = self._create(**item)
                _list.append(account)
            return _list

        account = self._create(**obj)
        return account

    def _create(self, *args, **kwargs):
        account = Account(kwargs['accountId'])
        if 'firstName' in kwargs:
            account.first_name = kwargs['firstName']
        if 'lastName' in kwargs:
            account.last_name = kwargs['lastName']
        if 'email' in kwargs:
            account.email = kwargs['email']
        if 'phone' in kwargs:
            account.phone = kwargs['phone']
        if 'companyName' in kwargs:
            account.company_name = kwargs['companyName']
        if 'state' in kwargs:
            account.state = kwargs['state']
        if 'city' in kwargs:
            account.city = kwargs['city']
        if 'zipCode' in kwargs:
            account.zip_code = kwargs['zipCode']
        if 'countryCode' in kwargs:
            account.country_code = kwargs['countryCode']
        if 'industryTag' in kwargs:
            account.industry_tag = kwargs['industryTag']
        if 'numberOfEmployees' in kwargs:
            account.number_of_employees = kwargs['numberOfEmployees']
        if 'timeFormat' in kwargs:
            account.time_format = kwargs['timeFormat']
        if 'href' in kwargs:
            account.href = kwargs['href']
        return account
