import base64
import json
import time

import jprops

from msrestazure.azure_active_directory import AADTokenCredentials
import adal

TENANT = "devynooxlive.onmicrosoft.com"
AUTHORITY_URI = "https://login.microsoftonline.com/" + TENANT


class TokenGenerator(object):

    def __init__(self, client_id, secret, path_to_config_file):

        self.client_id = client_id
        self.resource_uri = self.client_id
        self.secret = secret
        self.path_to_config_file = path_to_config_file

    def get_token(self):
        if self.__valid_token() is True:
            return self.__load_token()
        else:
            return self.__get_new_token()

    def __valid_token(self):

        # load token file
        with open(self.path_to_config_file) as fp:
            props = list(jprops.iter_properties(fp))
            token = None
            # check whether token exists
            for key, value in props:
                if key == 'token':
                    token = value

            if token is None:
                return False

        timestamp = token.split('.')[1]
        # correct padding
        timestamp = timestamp + '=' * (-len(timestamp) % 4)
        # json format
        json_bytes = base64.b64decode(timestamp)
        # extract expiration time [sec]
        json_string = json_bytes.decode("utf-8")
        json_object = json.loads(json_string)
        expiration = json_object["exp"]

        # current time
        now = time.time()

        # check
        if now < expiration:
            return True
        else:
            return False

    def __load_token(self):

        # load token file
        with open(self.path_to_config_file) as fp:
            props = jprops.load_properties(fp)
            token = props['token']

        return token

    def __get_new_token(self):

        # generate token
        context = adal.AuthenticationContext(AUTHORITY_URI, api_version=None)
        mgmt_token = context.acquire_token_with_client_credentials(self.resource_uri, self.client_id, self.secret)
        credentials = AADTokenCredentials(mgmt_token, self.client_id)
        token = credentials.token["access_token"]

        with open(self.path_to_config_file) as fp:
            props = list(jprops.iter_properties(fp))

        # store new token
        with open(self.path_to_config_file, 'w') as fp:
            # write all existing values back to file
            for key, value in props:
                if key != 'token':
                    jprops.write_property(fp, key, value)

            jprops.write_property(fp, 'token', token)

        return token
