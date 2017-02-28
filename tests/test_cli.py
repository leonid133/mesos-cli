import simplejson as json
import requests_mock
import sys
sys.path.append('.')
#sys.path.append('..')
from cli import MesosHttpClient


def test_list_active_frameworks():
    fake_response = open('tests/frameworks.json').read()
    with requests_mock.mock() as m:
        m.get('http://fake_mesos_server/frameworks', text=fake_response)
        mock_client = MesosHttpClient(server='http://fake_mesos_server')
        actual_request = mock_client.list_active_frameworks()
        if actual_request:
            for x in actual_request:
                actual_framework_id = x['id']
        else:
            actual_framework_id = None
        expected_framework_id = "62049115-5717-4ba0-8c5e-bff9321019c5-0000"
    assert expected_framework_id == actual_framework_id


def test_kill_framework_by_id():
    fake_response = """"""
    with requests_mock.mock() as m:
        m.delete('http://fake_mesos_server/frameworks', text=fake_response)
        mock_client = MesosHttpClient(server='http://fake_mesos_server')
        id = """62049115-5717-4ba0-8c5e-bff9321019c5-0000"""
        actual_request = mock_client.kill_framework_by_id(id)
        expected_status_code = 200
    assert expected_status_code == actual_request.status_code

    with requests_mock.mock() as m:
        m.get('http://fake_mesos_server/frameworks', text=fake_response)
        mock_client = MesosHttpClient(server='http://fake_mesos_server')
        actual_request = mock_client.list_active_frameworks()
        if actual_request:
            for x in actual_request:
                actual_framework_id = x['id']
        else:
            actual_framework_id = None
        expected_framework_id = None
    assert expected_framework_id == actual_framework_id

if __name__ == '__main__':
    test_list_active_frameworks()
    test_kill_framework_by_id()
