class Account(object):
    def __init__(self, *args, **kwargs):
        self.id = kwargs['accountId']
        self.first_name = kwargs['firstName']
        self.last_name = kwargs['lastName']
        self.email = kwargs['email']
        self.phone = kwargs['phone']
        self.company_name = kwargs['companyName']
        self.state = kwargs['state']
        self.city = kwargs['city']
        self.zip_code = kwargs['zipCode']
        self.contry_code = kwargs['countryCode']
        self.industry_tag = kwargs['industryTag']
        self.number_of_employees = kwargs['numberOfEmployees']
        self.time_format = kwargs['timeFormat']
        self.href = kwargs['href']

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)
