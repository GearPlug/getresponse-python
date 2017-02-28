import datetime
import uuid
from getresponse.client import GetResponse
from getresponse.excs import UniquePropertyError

new_id = uuid.uuid4().hex

getresponse = GetResponse('8a93e7ef8c2feb0c82986b503081af7e')

# account = getresponse.accounts()
#
# print('1. CUENTA:', account.id, account.time_format)
#
# campaigns = getresponse.get_campaigns({'sort': {'name', 'desc'}})
#
# print('2. CAMPAÑAS:')
#
# for campaign in campaigns:
#     print('     ', campaign.id, campaign.name, campaign.created_on)
#
# campaign = getresponse.get_campaign('TzXlN')
# print('3. CAMPAÑA:', campaign.id, campaign.name)
#
# print('4. CREAR CAMPAÑA:')
# campaign = {
#     "name": new_id,
# }
# try:
#     campaign = getresponse.create_campaign(campaign)
#     print('     ', campaign.id, campaign.name)
# except UniquePropertyError:
#     print('     ', 'La campaña no se pudo crear, el nombre ya existe')
#
contacts = getresponse.get_contacts()

print('5. CONTACTOS:')

for contact in contacts:
    print('     ', contact.id, contact.created_on, contact.created_on, contact.changed_on)
#

#
# contact = getresponse.get_contact('PIaPkN')
# if contact:
#     print('6. CONTACTO:', contact.id, contact.name)
#
# print('7. CREAR CONTACTO:')
# values = {
#     "email": "tavito.286@gmail.com",
#     "campaign": {
#         'campaignId': campaign.id,
#     },
# }
#
# try:
#     new_contact = getresponse.create_contact(values)
#     print('     ', 'Contacto en cola para ser creado.')
# except UniquePropertyError:
#     print('     ', 'El contacto no se pudo crear, el correo ya existe')
#
# if contact:
#     print('8. BORRAR CONTACTO:')
#     contact = getresponse.delete_contact(contact.id)
