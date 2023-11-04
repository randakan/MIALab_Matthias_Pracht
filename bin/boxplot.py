import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    # todo: load the "results.csv" file from the mia-results directory
    # todo: read the data into a list
    # todo: plot the Dice coefficients per label (i.e. white matter, gray matter, hippocampus, amygdala, thalamus)
    #  in a boxplot

    path = 'mia-result/'
    folder = '2023-11-04-12-37-03'
    file = pd.read_csv(path + folder + '/results.csv', sep=';')
    file.boxplot(column='DICE', by='LABEL', fontsize=12)
    plt.suptitle('')
    plt.title('Dice Values of ' + folder, fontsize=14)
    plt.xlabel('Brain structure', fontsize=12)
    plt.ylabel('Dice score', fontsize=12)
    plt.show()

    # alternative: instead of manually loading/reading the csv file you could also use the pandas package
    # but you will need to install it first ('pip install pandas') and import it to this file ('import pandas as pd')
    pass  # pass is just a placeholder if there is no other code


if __name__ == '__main__':
    main()
