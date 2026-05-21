import csv


def get_test_data(file_path):

    data = []

    with open(file_path, newline='', encoding="utf-8") as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            data.append(
                {
                    "product": row["product"],
                    "size": row["size"],
                    "quantity": row["quantity"],
                    "donation": row["donation"],
                    "pincode": row["pincode"],
                    "expected_title": row["expected_title"]
                }
            )

    return data