import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    # todo: load the "results.csv" file from the mia-results directory
    # todo: read the data into a list
    # todo: plot the Dice coefficients per label (i.e. white matter, gray matter, hippocampus, amygdala, thalamus)
    #  in a boxplot

    # Figure Dice
    path = 'mia-result/'
    folder = '2023-11-10-12-10-07'
    file = pd.read_csv(path + folder + '/results_DICE.csv', sep=';')
    file.boxplot(column='DICE', by='LABEL', fontsize=12)
    plt.suptitle('')
    plt.title('Dice Values of ' + folder, fontsize=14)
    plt.xlabel('Brain structure', fontsize=12)
    plt.ylabel('Dice score', fontsize=12)

    # Figure Hausdorff
    plt.figure()
    file = pd.read_csv(path + folder + '/results_HSDRF.csv', sep=';')
    file.boxplot(column='HSDRF', by='LABEL', fontsize=12)
    plt.suptitle('')
    plt.title('Hausdorff distance of ' + folder, fontsize=14)
    plt.xlabel('Brain structure', fontsize=12)
    plt.ylabel('Hausdorff distance', fontsize=12)
    plt.show()

    # alternative: instead of manually loading/reading the csv file you could also use the pandas package
    # but you will need to install it first ('pip install pandas') and import it to this file ('import pandas as pd')
    pass  # pass is just a placeholder if there is no other code


if __name__ == '__main__':
    main()
