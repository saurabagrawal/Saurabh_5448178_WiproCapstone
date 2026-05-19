import csv


def get_test_data(file_path):

    data = []

    with open(file_path, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            data.append(row["product"])

    return data