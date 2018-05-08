import requests

from pdf4me.helper.json_converter import JsonConverter
from pdf4me.helper.pdf4me_exceptions import Pdf4meClientException
from pdf4me.helper.token_generator import TokenGenerator

URL = "https://api-dev.pdf4me.com/"


class CustomHttp(object):

    def __init__(self, client_id, secret, path_to_config_file):

        self.client_id = client_id
        self.secret = secret
        self.path_to_config_file = path_to_config_file

        self.token_generator = TokenGenerator(client_id, secret, path_to_config_file)
        self.json_converter = JsonConverter()

    def post_universal_object(self, universal_object, controller):
        """Sends a post request to the specified controller with the given
        universal_object as a body.

        :param universal_object: object to be sent
        :type universal_object: object
        :param controller: swagger controller
        :type controller: str
        :return: post response
        """

        # prepare post request
        token = self.token_generator.get_token()
        request_url = URL + controller
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}

        # convert body to json
        body = self.json_converter.dump(element=universal_object)

        # send request
        res = requests.post(request_url, data=body, headers=headers)

        # read content from response
        json_response = self.json_converter.load(res.text)

        return json_response

    def post_wrapper(self, octet_streams, values, controller):
        """Builds a post requests from the given parameters.

        :param octet_streams: (key: file identifier, value: open(fileName, 'rb'))) pairs
        :type octet_streams: list
        :param values: (key: identifier of value, value: content of value) pairs
        :type values: list
        :param controller: swagger controller
        :type controller: str
        :return: post response
        """

        # prepare post request
        token = self.token_generator.get_token()
        request_url = URL + controller
        header = {'Authorization': 'Bearer ' + token}

        # build files
        if len(octet_streams) != 0:
            files = {key: value for (key, value) in octet_streams}
        else:
            files = None

        # build values
        if len(values) != 0:
            data = {key: value for (key, value) in values}
        else:
            data = None

        # send request
        if files is None:
            if data is None:
                raise Pdf4meClientException("Please provide at least one value or an octet-stream.")
            else:
                res = requests.post(request_url, data=data, headers=header)
        else:
            if data is None:
                res = requests.post(request_url, files=files, headers=header)
            else:
                res = requests.post(request_url, files=files, data=data, headers=header)

        return res.content
