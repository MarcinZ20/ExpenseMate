from rest_framework.versioning import AcceptHeaderVersioning

class CustomAcceptHeaderVersioning(AcceptHeaderVersioning):
    '''Custom api versioning settings class'''

    default_version = '1.0',
    allowed_versions = {'1.0', }
    version_param = 'version'