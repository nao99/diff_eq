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

            exactly_values['x'].append(float(rowValues[0]) * 1000)
            exactly_values['u'].append(float(rowValues[1]) * 1000)

            euler_values['x'].append(float(rowValues[0]) * 1000)
            euler_values['u'].append(float(rowValues[2]) * 1000)

            rugne_kutta_values['x'].append(float(rowValues[0]) * 1000)
            rugne_kutta_values['u'].append(float(rowValues[3]) * 1000)

            euler_error['x'].append(float(rowValues[0]) * 1000)
            euler_error['u'].append(float(rowValues[4]) * 1000)

            rugne_kutta_error['x'].append(float(rowValues[0]) * 1000)
            rugne_kutta_error['u'].append(float(rowValues[5]) * 1000)

        fig, ax = plt.subplots()

        ax.plot(exactly_values['x'], exactly_values['u'])

        ax.set_xlabel('1000x')
        ax.set_ylabel('1000u')

        plt.title('Exactly solution')
        plt.show()

        fig, ax = plt.subplots()

        ax.plot(euler_values['x'], euler_values['u'])

        ax.set_xlabel('1000x')
        ax.set_ylabel('1000u')

        plt.title('Euler solution')
        plt.show()

        fig, ax = plt.subplots()

        ax.plot(rugne_kutta_values['x'], rugne_kutta_values['u'])

        ax.set_xlabel('1000x')
        ax.set_ylabel('1000u')

        plt.title('Runge Kutta solution')
        plt.show()

        fig, ax = plt.subplots()

        ax.plot(euler_error['x'], euler_error['u'])

        ax.set_xlabel('1000x')
        ax.set_ylabel('1000u')

        plt.title('Euler error')
        plt.show()

        fig, ax = plt.subplots()

        ax.plot(rugne_kutta_error['x'], rugne_kutta_error['u'])

        ax.set_xlabel('1000x')
        ax.set_ylabel('1000u')

        plt.title('Runge Kutta error')
        plt.show()
