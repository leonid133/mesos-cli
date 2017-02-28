import simplejson as json
import requests
import requests.exceptions
import time
from .exceptions import CliError, TemporaryRedirectError, ServiceUnavailableError


class MesosHttpClient(object):

    """Client Interface for the Mesos HTTP"""

    def __init__(self, server, timeout=10):
        self.session = requests.Session()
        self.server = server
        self.timeout = timeout

    def _do_request(self, method, path, data=None):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = None
        server = self.server
        timeout = time.time() + self.timeout
        while response is None and time.time() < timeout:
            url = ''.join([server.rstrip('/'), path])
            try:
                response = self.session.request(method, url, data=data, headers=headers, timeout=self.timeout)
            except requests.exceptions.RequestException as e:
                print 'Error while calling to ', url, str(e)

        if response is None:
            raise CliError('Mesos server does not respond')

        if response.status_code == 307:
            raise TemporaryRedirectError(response)

        if response.status_code == 503:
            raise ServiceUnavailableError(response)

        return response

    def list_active_frameworks(self):
        response = self._do_request('GET', '/frameworks')
        try:
            frameworks = json.loads(response.text)
            active_frameworks = [x for x in frameworks['frameworks'] if x['active']]
        except Exception:
            active_frameworks = None
        return active_frameworks

    def kill_framework_by_id(self, framework_id=None):
        data = '"{"id":"'+framework_id+'"}"'
        response = self._do_request('DELETE', '/frameworks', data=data)
        return response
