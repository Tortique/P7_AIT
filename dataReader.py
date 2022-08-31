import csv


def reader(filename):
    try:
        with open(filename) as csvfile:
            data_files = csv.reader(csvfile, delimiter=",")
            next(csvfile)

            data = []

            for row in data_files:
                if float(row[1]) <= 0 or float(row[2]) <= 0:
                    pass
                else:
                    action = (row[0], int(float(row[1]) * 100), float(row[1]) * float(row[2]) / 100)
                    data.append(action)
            return data
    except FileNotFoundError:
        print(f"\nFile '{filename}' does not exist.")
