class CliError(Exception):
    pass


class HttpError(CliError):

    def __init__(self, response):
        """
        :param :class:`requests.Response` response: HTTP response
        """
        self.error_message = response.reason or ''
        if response.content:
            content = response.json()
            self.error_message = content.get('message', self.error_message)
            self.error_details = content.get('details')
        self.status_code = response.status_code
        super(HttpError, self).__init__(self.__str__())

    def __repr__(self):
        return 'HttpError: HTTP %s returned with message, "%s"' % \
               (self.status_code, self.error_message)

    def __str__(self):
        return self.__repr__()


class TemporaryRedirectError(HttpError):
    pass


class ServiceUnavailableError(HttpError):
    pass
