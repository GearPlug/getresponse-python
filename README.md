![](https://img.shields.io/badge/version-0.1.4-success) ![](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10%20|%203.11-4B8BBE?logo=python&logoColor=white)
# getresponse-python

*getresponse-python* is an API wrapper for GetResponse written in Python.

## Installing

```
pip install getresponse-python
```

## Usage

```
from getresponse.client import GetResponse
from getresponse.excs import UniquePropertyError

getresponse = GetResponse('YOUR_API_KEY_HERE')
```
For GetResponse Enterprise platform:
```
from getresponse.client import GetResponseEnterprise

getresponse = GetResponseEnterprise('YOUR_API_KEY_HERE', 'YOUR_DOMAIN_NAME', 'YOUR_API_ENDPOINT')
```
Get account info:
```
account = getresponse.accounts()

print('Account:', account.id, account.name)
```
Get all campaigns:
```
campaigns = getresponse.get_campaigns({'sort': {'name', 'desc'}})

for campaign in campaigns:
    print('Campaign:' campaign.id, campaign.name)
```
Get a campaign:
```
campaign = getresponse.get_campaign('CAMPAIGN_ID_HERE')

print('Campaign:', campaign.id, campaign.name)
```
Create a campaign:
```
campaign = {
   "name": 'UNIQUE_ID_HERE',
}

try:
   campaign = getresponse.create_campaign(campaign)
   print('Campaign:', campaign.id, campaign.name)
except UniquePropertyError:
   print("Cannot create: campaign's name already exists.")
```
Get all contacts:
```
# Example:
contacts = getresponse.get_contacts({'sort[createdOn]': 'ASC', 'query[name]': 'juan'})
for contact in contacts:
    print('Contact:', contact.id, contact.name)
```
Get a contact:
```
contact = getresponse.get_contact('CONTACT_ID_HERE')
if contact:
    print('Contact:', contact.id, contact.name)
```
Create a contact:
```
values = {
    "email": "CONTACT_EMAIL_HERE",
    "campaign": {
        'campaignId': 'CAMPAIGN_ID_HERE',
    },
}

try:
    contact = getresponse.create_contact(values)
    print('Contact in queue to be created.')
except UniquePropertyError:
    print("Cannot created: contact's email already exists.")
```
Delete a contact:
```
contact = getresponse.delete_contact('CONTACT_ID_HERE')
```
Update a contact:
```
body = {
    "name": "Test Name",
    "customFieldValues": [
        {"customFieldId": "pLQSI0", "value": ["comment 1234"]},
        {"customFieldId": "pLQSu3", "value": ["+573108889999"]},
    ],
}
contact = getresponse.update_contact(self, contact_id, body)
```
Get all custom fields:
```
custom_fields = getresponse.get_custom_fields({'sort': {'name', 'desc'}})
for custom_field in custom_fields:
    print('Custom Field:', custom_field.id, custom_field.name)
```
Get a custom field:
```
custom_field = getresponse.get_custom_field('CUSTOM_FIELD_ID_HERE')
if custom_field:
    print('Custom Field:', custom_field.id, custom_field.name)
```
## Requirements
- requests

## Contributing
We are always grateful for any kind of contribution including but not limited to bug reports, code enhancements, bug fixes, and even functionality suggestions.
#### You can report any bug you find or suggest new functionality with a new [issue](https://github.com/GearPlug/getresponse-python/issues).
#### If you want to add yourself some functionality to the wrapper:
1. Fork it ( https://github.com/GearPlug/getresponse-python )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Adds my new feature')
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request
