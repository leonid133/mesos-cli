import requests
import requests.exceptions

class MesosHttpClient(object):

    """Client Interfeace for the Mesos HTTP"""

    def __init__(self, server, timeout=10):
        self.session = requests.Session()
        self.server = server
        self.timeout = timeout

    def _do_request(self, method, path, data=None):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = None
        server = self.server
        while response is None:
            url = ''.join([server.rstrip('/'), path])
            try:
                response = self.session.request(method, url, data=data, headers=headers, timeout=self.timeout)
            except requests.exceptions.RequestException as e:
                print(str(e))

        return response

    def list_active_frameworks(self):
        active_frameworks = self._do_request('GET', '/frameworks')
        return active_frameworks

    def kill_framework_by_id(self, framework_id=None):
        data = framework_id.to_json()
        self._do_request('DELETE', '/frameworks', data=data)
