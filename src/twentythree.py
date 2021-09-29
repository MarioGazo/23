import argparse
import requests
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class TwentyThree:
    """ Where to send requests """
    REQUEST_URL = 'http://localhost/assets/'

    """ Response object """
    response = {}

    def __init__(self):
        # Set argument parser, positional method and id (not mandatory) and optional type, title, label and url
        arg_parser = argparse.ArgumentParser(description='Perform one of the methods')
        arg_parser.add_argument('method', type=str, help='Provide method to be executed')
        arg_parser.add_argument('id', nargs='?', type=int, help='Provide id of asset')
        arg_parser.add_argument('--type', type=str)
        arg_parser.add_argument('--title', type=str)
        arg_parser.add_argument('--label', type=str)
        arg_parser.add_argument('--url', type=str)

        # Parse CLI arguments
        self.args = arg_parser.parse_args()
        self.method = self.args.method

        # Try to make request
        try:
            self.response = {
                'create': self.create,
                'read': self.read,
                'update': self.update,
                'delete': self.delete
            }[self.method]()
        except KeyError:
            raise Exception('Provide valid method: create, read, update, delete')
        except requests.exceptions.ConnectionError:
            raise Exception('Connection error')

        # Check response
        if self.response.status_code != 200:
            raise Exception('Request failed, code: '+str(self.response.status_code))
        print(self.response.text)

    def create(self) -> requests.request:
        """ Create asset, need correct type, title,  label and url """
        # Check needed values
        if None in [self.args.type, self.args.title, self.args.label, self.args.url]:
            raise Exception('Provide all parameters for asset creation')
        # Check type
        if self.args.type not in ['photo', 'video']:
            raise Exception('Asset can only be of type photo or video')

        # Check URL validity
        if self.check_url_invalidity():
            raise Exception('Provided URL is not valid')

        # Send POST request
        return requests.post(
            self.REQUEST_URL,
            {'type': self.args.type, 'title': self.args.title, 'label': self.args.label, 'url': self.args.url}
        )

    def read(self) -> requests.request:
        """ Read single asset or all of them, depending if ID is provided """
        # Check if id is set,
        if self.args.id is not None:
            self.REQUEST_URL += str(self.args.id)

        # Send GET request
        return requests.get(self.REQUEST_URL)

    def update(self) -> requests.request:
        """ Update asset, needs ID, title, label and url """
        # Check if id is set
        if self.args.id is None:
            raise Exception('Provide id of asset you want to update')

        # Check URL validity
        if self.args.url is not None and self.check_url_invalidity():
            raise Exception('Provided URL is not valid')

        # Send PUT request
        return requests.put(
            self.REQUEST_URL + str(self.args.id),
            {'title': self.args.title, 'label': self.args.label, 'url': self.args.url}
        )

    def delete(self) -> requests.request:
        """ Delete asset, needs ID """
        # Check if id is set
        if self.args.id is None:
            raise Exception('Provide id of asset you want to delete')

        # Send DELETE request
        return requests.delete(self.REQUEST_URL + str(self.args.id))

    def check_url_invalidity(self) -> bool:
        """ Returns True if URL is valid, False if it is not """
        validate = URLValidator()
        try:
            validate(self.args.url)
            return False
        except ValidationError:
            return True


if __name__ == '__main__':
    """ START HERE """
    twentyThree = TwentyThree()
