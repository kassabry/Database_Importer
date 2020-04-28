import csv
from faker import Faker
import sys


def data_gen():
    # Initializes the faker object
    fake = Faker()
    # Takes the filename and tuple from the command line
    filename = sys.argv[1]
    tuple_count = int(sys.argv[2])

    # Opens the filename from command line in write mode
    with open(filename, 'w', newline='') as csvfile:
        # Makes the writer delimiter a pipe bar
        data_writer = csv.writer(csvfile, delimiter='|', quotechar='"', quoting = csv.QUOTE_MINIMAL)

        # Makes a list of faked attributes in a specific order relative to the importing
        Faker.seed(0)
        for x in range(tuple_count):
            list_row = [fake.first_name(), fake.last_name(), fake.street_address(),
                        fake.city(), fake.postcode(), fake.company(), fake.job(),
                        fake.credit_card_number(), fake.credit_card_expire(), fake.credit_card_security_code(),
                        fake.phone_number(), fake.ssn(), fake.license_plate(),
                        fake.company_email(), fake.domain_name()]
            # Writes the list above to the csv file
            data_writer.writerow(list_row)


# Runs the function with everything
data_gen()
