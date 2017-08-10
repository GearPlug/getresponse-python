class CustomField(object):
    def __init__(self, *args, **kwargs):
        self.id = args[0]
        self.href = None
        self.name = None
        self.field_type = None
        self.value_type = None
        self.type = None
        self.hidden = None
        self.values = None

    def __repr__(self):
        return "<CustomField(id='{}', name='{}'>".format(self.id, self.name)


class CustomFieldManager(object):
    def create(self, obj):
        if isinstance(obj, list):
            _list = []
            for item in obj:
                custom_field = self._create(**item)
                _list.append(custom_field)
            return _list

        custom_field = self._create(**obj)
        return custom_field

    def _create(self, *args, **kwargs):
        custom_field = CustomField(kwargs['customFieldId'])
        if 'href' in kwargs:
            custom_field.href = kwargs['href']
        if 'name' in kwargs:
            custom_field.name = kwargs['name']
        if 'fieldType' in kwargs:
            custom_field.field_type = kwargs['fieldType']
        if 'valueType' in kwargs:
            custom_field.value_type = kwargs['valueType']
        if 'type' in kwargs:
            custom_field.type = kwargs['type']
        if 'hidden' in kwargs:
            custom_field.hidden = kwargs['hidden']
        if 'values' in kwargs:
            custom_field.values = kwargs['values']
        return custom_field
