# getresponse

getresponse is an API wrapper for GetResponse written in Python.

## Installing

```
pip install getresponse
```

## Usage

```
from getresponse.client import GetResponse
from getresponse.excs import UniquePropertyError

getresponse = GetResponse('YOUR_API_KEY_HERE')
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
    new_contact = getresponse.create_contact(values)
    print('Contact in queue to be created.')
except UniquePropertyError:
    print("Cannot created: contact's email already exists.")
```
Delete a contact:
```
contact = getresponse.delete_contact('CONTACT_ID_HERE')
```

## Requirements
- requests
