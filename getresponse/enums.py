from enum import Enum


class HttpMethod(Enum):
    GET = 1
    POST = 2
    DELETE = 3


class ObjType(Enum):
    ACCOUNT = 1
    CAMPAIGN = 2
    CONTACT = 3
    CUSTOM_FIELD = 4
