import jprops

from pdf4me.helper.custom_http import CustomHttp
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException

DEFAULT_CONFIG_PROPERTIES = '../config.properties'


class Pdf4meClient(object):

    def __init__(self, client_id=None, secret=None, path_to_config_file=DEFAULT_CONFIG_PROPERTIES):

        # in case either client_id or secret is not provided, load them from the property file
        if client_id is None or secret is None:

            # load client_id and secret from property file
            try:
                with open(path_to_config_file) as fp:
                    props = list(jprops.iter_properties(fp))
                    prop_client_id = None
                    prop_secret = None

                    # check whether client_id and secret exist
                    for key, value in props:
                        if key == 'client_id':
                            prop_client_id = value
                        elif key == 'secret':
                            prop_secret = value

                    if prop_client_id is None:
                        raise Pdf4meClientException('Please store the client_id in the ' + path_to_config_file + ' file'
                                                    ' or provide your client_id in the Pdf4meClient constructor.')
                    elif prop_secret is None:
                        raise Pdf4meClientException('Please store the secret in the ' + path_to_config_file + ' file'
                                                    ' or provide your secret in the Pdf4meClient constructor.')
            except IOError:
                raise Pdf4meClientException('The config.properties file is not stored at \'' + path_to_config_file +
                                            '\'. Please initialize the Pdf4meClient object with the correct path to your '
                                            'conifg.properties file. Or else provide your clientId AND secret in the '
                                            'Pdf4meClient constructor.')

            self.custom_http = CustomHttp(prop_client_id, prop_secret)
        else:
            self.custom_http = CustomHttp(client_id, secret)
