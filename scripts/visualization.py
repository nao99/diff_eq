import csv
import matplotlib.pyplot as plt


if __name__ == "__main__":
    csv_path = './../data/data.csv'

    with open(csv_path, 'r') as data:
        reader = csv.reader(data)

        exactly_values = {
            "x": [],
            "u": [],
        }

        euler_values = {
            "x": [],
            "u": [],
        }

        rugne_kutta_values = {
            "x": [],
            "u": [],
        }

        euler_error = {
            "x": [],
            "u": [],
        }

        rugne_kutta_error = {
            "x": [],
            "u": [],
        }

        for index, row in enumerate(reader):
            if 0 == index:
                continue

            rowValues = row[0].split(';')

            exactly_values['x'].append(rowValues[0])
            exactly_values['u'].append(rowValues[1])

            euler_values['x'].append(rowValues[0])
            euler_values['u'].append(rowValues[2])

            rugne_kutta_values['x'].append(rowValues[0])
            rugne_kutta_values['u'].append(rowValues[3])

            euler_error['x'].append(rowValues[0])
            euler_error['u'].append(rowValues[4])

            rugne_kutta_error['x'].append(rowValues[0])
            rugne_kutta_error['u'].append(rowValues[5])

        plt.plot(exactly_values['x'], exactly_values['u'])
        plt.show()

        plt.plot(euler_values['x'], euler_values['u'])
        plt.show()

        plt.plot(rugne_kutta_values['x'], rugne_kutta_values['u'])
        plt.show()

        plt.plot(euler_error['x'], euler_error['u'])
        plt.show()

        plt.plot(rugne_kutta_error['x'], rugne_kutta_error['u'])
        plt.show()
