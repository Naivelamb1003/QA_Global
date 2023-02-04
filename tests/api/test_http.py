import pytest
import requests

@pytest.mark.http
def test_first_request():
    reply_first = requests.get('https://api.github.com/zen')
    print(f"Responce is {reply_first.text}")

@pytest.mark.http
def test_second_request():
    reply_second = requests.get('https://api.github.com/users/defunkt')
    body = reply_second.json()
    headers = reply_second.headers

    assert body['name'] == 'Chris Wanstrath'
    assert reply_second.status_code == 200
    assert headers['Server'] == 'GitHub.com'

@pytest.mark.http
def test_status_code_request():
    r = requests.get('test_status_code_request')

    assert r.status_code == 404

    