class PassengerParser:

    def __init__(self, string_to_parse):
        self.string_to_parse = string_to_parse
        self.last_name, self.first_name = self.string_to_parse.split("/")
        self.last_name = self.last_name.strip("1")
        self.gender = self.get_gender_and_strip_gender_from_first_name()

    def get_gender_and_strip_gender_from_first_name(self):

        if self.first_name.endswith("MR"):
            self.first_name = self.first_name[:-2]
            return "MR"

        elif self.first_name.endswith("MRS"):
            self.first_name = self.first_name[:-3]
            return "MRS"

        elif self.first_name.endswith("CHD"):
            self.first_name = self.first_name[:-3]
            return "CHD"

        else:
            return "?"


class HeaderParser:

    def __init__(self, string_to_parse):
        self.header_to_parse = string_to_parse
        self.routing = self.get_routing()
        self.flight_date = self.get_flight_number()
        self.flight_number = self.get_flight_number()

    @staticmethod
    def get_routing():
        # todo
        return "FCO-BIO"

    @staticmethod
    def get_date_of_flight():
        # todo
        return "2018-5-25"

    @staticmethod
    def get_flight_number():
        # todo
        return "ENT882"
