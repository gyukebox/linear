import xlrd
import numpy as np
import matplotlib.pyplot as plt


class Weatherdata:
    def __init__(self, filename):
        self.filename = filename

    pass


if __name__ == '__main__':
    book = xlrd.open_workbook('WEATHER_DATA.XLS')
    sh = book.sheet_by_index(0)
    a = [element.value for i in range(sh.nrows) for element in sh.row(rowx=i)]
    a = [0 if element == -99999 else element for element in a]

    matrix = np.array(a, dtype=int).reshape((sh.nrows, sh.ncols))
    # print(matrix)

    for row in np.nditer(matrix):
        print(row)
        print('average={}, std={}'.format(np.average(row), np.std(row)))

    plt.figure()
    plt.plot(matrix)
    plt.show()
