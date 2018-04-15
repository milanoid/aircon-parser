class PassengerParser:

    def __init__(self, string_to_parse):
        self.string_to_parse = string_to_parse
        self.last_name, self.first_name = self.string_to_parse.split("/")
        # infant detection
        if self.last_name.startswith("2"):
            self.last_name = self.last_name.strip("2")  # parent
            self.has_infant = True
        else:
            self.has_infant = False
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


class InfantParser:

    def __init__(self, string_to_parse):
        self.last_name, self.first_name = string_to_parse.split("/")


class HeaderParser:

    def __init__(self, string_to_parse):
        self.string_to_parse = string_to_parse
        self.routing = self.get_routing()
        self.flight_date = self.get_date_of_flight()
        self.flight_number = self.get_flight_number()

    def get_routing(self):
        return self.string_to_parse.split(" / ")[0]

    def get_date_of_flight(self):
        day, month, year = self.string_to_parse.split(" / ")[1].split(" ")[2].split("/")
        return "20{}/{}/{}".format(year, month, day)

    def get_flight_number(self):
        return self.string_to_parse.split(" / ")[1][:7].strip(" ").replace(" ","")
