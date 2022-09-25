import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def get_data(file):
    df = pd.read_csv((file), sep='\t')
    df.columns = ['gen', 'nevals', 'avg', 'stddev', 'min', 'max']
    x = df['nevals'].cumsum(axis=0)
    means = list()
    stds = list()
    std_const = 25 ## for readability of deviation that the areas do not overlap

    for i in range(1, 1002):
        l = list(df['max'][:i])
        idx = l.index(max(l))
        means.append(df['avg'][idx])
        stds.append(df['stddev'][idx] / std_const)

    return [x, np.array(means), np.array(stds)]

def plot_results(data, mut_int):
    plt.rcParams["figure.figsize"] = [15, 10]
    plt.rcParams["figure.autolayout"] = True

    plt.figure('figure')
    plt.xlabel('Evaluated individuals')
    plt.ylabel('Fitness')

    if mut_int is not None:
        plt.title(f'Mutation intensity of {mut_int}')
        plt.plot(data[0], data[1])
        plt.fill_between(data[0], list(data[1] - data[2]), list(data[1] + data[2]), alpha=.3)
        plt.savefig(f'C:\\PATH\\TO\\FOLDER\\avg-stddev plot mutation intensity of {mut_int}.png')
    else:
        for i in data:
            plt.plot(data[i][0], data[i][1], label=f'mutation intensity = {i}')
            plt.fill_between(data[i][0], list(data[i][1] - data[i][2]), list(data[i][1] + data[i][2]), alpha=.3)
        plt.legend()
        plt.savefig(f'C:\\PATH\\TO\\FOLDER\\avg-stddev plot all mutation intensities together.png')

    plt.close('figure')


if __name__ == '__main__':
    d = dict()
    for i in ['0', '005', '010', '020', '030', '040', '050']:
        file = f'C:\\PATH\\TO\\FOLDER\\final-results-{i}.txt'
        data = get_data(file)
        d[i] = list(data)
        plot_results(data, i)

    plot_results(d, None)
