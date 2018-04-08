from openpyxl import load_workbook


class OutputWriter:

    def __init__(self, passengers, header, filename="output.xlsx"):
        self.passengers = passengers
        self.header = header
        self.filename = filename
        self.destination_workbook = load_workbook(self.filename)

    def write_passengers(self):
        i = 5  # first passenger starts on row 5
        j = 1  # holds passenger's number
        for passenger in self.passengers:
            self.destination_workbook.active.cell(i, 1).value = j
            self.destination_workbook.active.cell(i, 2).value = passenger.gender
            self.destination_workbook.active.cell(i, 3).value = passenger.last_name
            self.destination_workbook.active.cell(i, 4).value = passenger.first_name
            i += 1
            j += 1

        return self

    def write_header(self):
        self.destination_workbook.active.cell(2, 2).value = self.header.routing
        self.destination_workbook.active.cell(2, 3).value = self.header.flight_date
        self.destination_workbook.active.cell(2, 4).value = self.header.flight_number
        self.destination_workbook.active.cell(2, 6).value = len(self.passengers)
        return self

    def save(self):
        self.destination_workbook.save(self.filename)
