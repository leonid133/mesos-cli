import requests_mock
from cli import MesosHttpClient

def test_list_active_frameworks():
    fake_response = """
    """
    with requests_mock.mock() as m:
        m.get('http://fake_mesos_server/frameworks', text=fake_response)
        mock_client = MesosHttpClient(servers='http://fake_mesos_server')
        actual_request = mock_client.list_active_frameworks()
        expected_request = """
        """
    assert expected_request == actual_request

def test_kill_framework_by_id():
    fake_response = """
    """
    with requests_mock.mock() as m:
        m.delete('http://fake_mesos_server/frameworks', text=fake_response)
        mock_client = MesosHttpClient(servers='http://fake_mesos_server')
        id = """"""
        actual_request = mock_client.kill_framework_by_id(id)
        expected_request = """
        """
    assert expected_request == actual_request