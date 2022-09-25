import matplotlib.pyplot as plt
import pandas as pd


def get_data(file):
    df = pd.read_csv((file), sep='\t')
    x = df['nevals'].cumsum(axis=0)
    y = [max(list(df['max     '][:i])) for i in range(1, 1002)]

    return [x, y]


def plot_results(data, mut_int):
    plt.rcParams["figure.figsize"] = [15, 10]
    plt.rcParams["figure.autolayout"] = True

    plt.figure('figure')
    plt.xlabel('Evaluated individuals')
    plt.ylabel('Fitness')

    if mut_int is not None:
        plt.title(f'Mutation intensity of {mut_int}')
        plt.plot(data[0], data[1])
        plt.savefig(f'C:\\PATH\\TO\\FOLDER\\best individuals plot mutation intensity of {mut_int}.png')
    else:
        for i in data:
            plt.plot(data[i][0], data[i][1], label=f'mutation intensity = {i}')
        plt.legend()
        plt.savefig(f'C:\\PATH\\TO\\FOLDER\\best individuals plot all mutation intensities together.png')

    plt.close('figure')


if __name__ == '__main__':
    d = dict()
    for i in ['0', '005', '010', '020', '030', '040', '050']:
        file = f'C:\\PATH\\TO\\FOLDER\\final-results-{i}.txt'
        data = get_data(file)
        d[i] = list(data)
        plot_results(data, i)

    plot_results(d, None)
