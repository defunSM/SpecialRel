import sys, os, math
import optparse

import SpecialRel as sprl
import matplotlib.pyplot as plt
import numpy as np

def time_of_the_object(v, b, x):
    return (1 / v) * x + b

def given_velocity_and_initial_position(v, b=0, limit=11, lower_limit=-11):

    data = []

    for i in np.arange(lower_limit,limit):
        data.append(i)
        data.append(time_of_the_object(v, b, i))

    print(data)

    return data

def retrieve_ycoords(data):

    y_axis_coord = []

    for i in np.arange(len(data)):
        if (i % 2 != 0):
            y_axis_coord.append(data[i])

    return y_axis_coord

def retrieve_xcoords(data):

    x_axis_coord = []

    for i in np.arange(len(data)):
        if (i % 2 == 0):
            x_axis_coord.append(int(data[i]))

    return x_axis_coord


def space_time_graph(data, name_of_object="object"):

    x = retrieve_xcoords(data)
    y = retrieve_ycoords(data)

    slope, intercept = np.polyfit(x, y, 1)

    # Create a list of values in the best fit line
    abline_values = [slope * i + intercept for i in x]


    plt.axhline(linewidth=2, color='black')
    plt.axvline(linewidth=2, color='black')

    # Plot the best fit line over the actual values
    plt.ylabel('Time (s)')
    plt.xlabel('Space (m)')
    plt.grid(True)
    plt.plot(x, y, '--', label=name_of_object)
    plt.legend(loc='upper left')

    plt.axis('tight')

    # plt.plot(x, abline_values, 'b')
    plt.title("SpaceTime Graph")
    plt.show()




def main():

    p = optparse.OptionParser()
    p.add_option('--velocity', '-v', default=0.2)
    p.add_option('--intercept', '-b', default=0)
    p.add_option('--upperlimit', '-u', default=11)
    p.add_option('--lowerlimit', '-l', default=-11)
    p.add_option('--objectname', '-n', default="object")
    p.add_option('--gammafactor', '-g', default=1)


    options, arguments = p.parse_args()

    v = float(options.velocity)
    b = float(options.intercept)
    ul = float(options.upperlimit)
    ll = float(options.lowerlimit)
    n = options.objectname

    data = given_velocity_and_initial_position(v, b, ul, ll)

    space_time_graph(data, n)








if __name__=="__main__":
    main()
