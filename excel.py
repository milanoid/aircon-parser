from openpyxl import load_workbook

from AirconParser import PassengerParser, HeaderParser
from OutputWriter import OutputWriter
from Passenger import Passenger


def main():
    workbook_source = load_workbook('zdroj.xlsx')
    sheet = workbook_source.active
    passengers = []

    for i in range(8, 197):

        if sheet.cell(i, 3).value is not None:
            parser = PassengerParser(sheet.cell(i, 3).value)
            passengers.append(Passenger(parser.first_name, parser.last_name, parser.gender))

    header_to_parse = sheet.cell(1, 3).value

    writer = OutputWriter(passengers=passengers, header=HeaderParser(header_to_parse))
    writer.write_passengers().write_header().save()


if __name__ == "__main__":
    main()
