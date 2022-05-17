class Project221ossException(Exception):

    def __init__(self, message: str = "", status_code=500, extra: dict = None):
        self.detail_dict = {
            "message": message
        }

        if extra:
            self.detail_dict = {
                **self.detail_dict,
                **extra
            }

        self.status_code = status_code

    def get_json(self):
        return self.detail_dict

    def get_code(self):
        return self.status_code

    ...


class ValueOrValidateException(Project221ossException):
    def __init__(self, status_code=400, message: str = "", extra: dict = None):
        super().__init__(status_code=status_code, message=message, extra=extra)
