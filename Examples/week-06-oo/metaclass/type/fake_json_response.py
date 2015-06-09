from mock import MagicMock
import requests

#
#  a function we want to test
#
def make_request():
    response = requests.post( '/fake_uri/', {} )
    if response.status_code == 200:
        response_json = response.json()
        # do other import stuff with response here...
        return response_json

fake_response = type( 'FakeResponse', (), {
    'status_code' : 200,
    'text' : 'success',
    'json' : lambda self: { 'meta' : { '_id': 1231235 } },
})()

requests.post = MagicMock( return_value=fake_response )

if __name__ == '__main__':
    response_json = make_request()
    assert response_json == { 'meta' : { '_id': 1231235 } }
    

