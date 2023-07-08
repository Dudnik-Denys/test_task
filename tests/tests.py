import requests
from requests_data import *


def test_create_board_positive():
    data = {
        'name': 'my_test_board',
    }

    data = data | BASE_DATA

    response = requests.post(BASE_URL + 'boards/', data)
    assert response.status_code == 200, f'wrong status code, {response.status_code} {response.content}'
    assert response.json()['name'] == data['name'], f'wrong board name, {response.status_code} {response.content}'
    return response.json()['id']


def test_get_exist_board_positive():
    response = requests.get(BASE_URL + 'boards/' + '64a85c9c41b0bb749633f4c4', BASE_DATA, headers=BASE_HEADERS)
    assert response.status_code == 200, f'wrong status code, {response.status_code} {response.content}'


def test_get_created_board_positive():
    new_board_id = test_create_board_positive()
    response = requests.get(BASE_URL + 'boards/' + new_board_id, BASE_DATA, headers=BASE_HEADERS)
    assert response.status_code == 200, f'wrong status code, {response.status_code} {response.content}'


def test_update_board_positive():
    data = {
        'name': 'updated_name'
    }

    data = data | BASE_DATA

    response = requests.put(BASE_URL + + 'boards/' + '64a85c9c41b0bb749633f4c4', data)

    assert response.status_code == 200, f'wrong status code, {response.status_code} {response.content}'
    assert response.json()['name'] == data['name'], f'wrong board name, {response.status_code} {response.content}'


def test_delete_board():
    response = requests.get(BASE_URL + 'boards/' + '64a861277713f9004a4d5073', BASE_DATA, headers=BASE_HEADERS)
    assert response.status_code == 200, f'wrong status code, {response.status_code} {response.content}'


def test_get_board_negative():
    response = requests.get(BASE_URL + 'boards/' + '64a85c9c41b0bb749633f4c5', BASE_DATA, headers=BASE_HEADERS)
    assert response.status_code == 404, f'wrong status code, {response.status_code} {response.content}'

def test_create_new_list_positive():
    data = {
        'name': 'new_list',
        'idBoard': '64a85c9c41b0bb749633f4c4'
    }

    data = data | BASE_DATA

    response = requests.post(BASE_URL + 'lists/', data)
    assert response.status_code == 200, f'wrong status code {response.status_code} {response.content}'
    return response.json()['id']


def test_get_list_positive():
    response = requests.get(BASE_URL + 'lists/' + '64a953458deea37e2b8d1e73', BASE_DATA)
    assert response.status_code == 200, f'wrong status code {response.status_code} {response.content}'
    assert response.json()['name'] == 'new_list', f'wrong list name, {response.status_code} {response.content}'


def test_get_list_negative():
    response = requests.get(BASE_URL + 'lists/' + '64a953458deea37e2b8d1e74', BASE_DATA)
    assert response.status_code == 404, f'wrong status code {response.status_code} {response.content}'


def test_create_card_positive():
    data = {
        'idList': '64a953458deea37e2b8d1e73',
        'name': 'new_card'
    }

    data = data | BASE_DATA

    response = requests.post(BASE_URL + 'cards/', data, headers=BASE_HEADERS)
    assert response.status_code == 200, f'wrong status code {response.status_code} {response.content}'
    assert response.json()['name'] == 'new_card', f'wrong card name {response.status_code} {response.content}'
