class Bankrupt:
    def __init__(self, id):
        self.__id = id
        self.__type = ''
        self.__case_id = ''
        self.__cancel_reason = ''
        self.__authority = ''
        self.__cancel_date = ''
        self.__bankruptcy_date = ''
        self.__concentration_date = ''
        self.__case_status = ''
        self.__destruction_date = ''
        self.__delay_date = ''

    def get_id(self):
        return self.__id

    def get_type(self):
        return self.__type

    def get_case_id(self):
        return self.__case_id

    def get_cancel_reason(self):
        return self.__cancel_reason

    def get_authority(self):
        return self.__authority

    def get_cancel_date(self):
        return self.__cancel_date

    def get_bankruptcy_date(self):
        return self.__bankruptcy_date

    def get_concentration_date(self):
        return self.__concentration_date

    def get_case_status(self):
        return self.__case_status

    def get_destruction_date(self):
        return self.__destruction_date

    def get_delay_date(self):
        return self.__delay_date

    def set_id(self, id):
        self.__id = id

    def set_type(self, type):
        self.__type = type

    def set_case_id(self, case_id):
        self.__case_id = case_id

    def set_cancel_reason(self, cancel_reason):
        self.__cancel_reason = cancel_reason

    def set_authority(self, authority):
        self.__authority = authority

    def set_cancel_date(self, cancel_date):
        self.__cancel_date = cancel_date

    def set_bankruptcy_date(self, bankruptcy_date):
        self.__bankruptcy_date = bankruptcy_date

    def set_concentration_date(self, concentration_date):
        self.__concentration_date = concentration_date

    def set_case_status(self, case_status):
        self.__cancel_date = case_status

    def set_destruction_date(self, destruction_date):
        self.__cancel_date = destruction_date

    def set_delay_date(self, delay_date):
        self.__delay_date = delay_date
