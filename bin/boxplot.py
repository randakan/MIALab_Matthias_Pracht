import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    # todo: load the "results.csv" file from the mia-results directory
    # todo: read the data into a list
    # todo: plot the Dice coefficients per label (i.e. white matter, gray matter, hippocampus, amygdala, thalamus)
    #  in a boxplot

    fig, axs = plt.subplots(1, 2)
    fontsize = 10

    # Figure Dice
    path = 'mia-result/'
    folder = '2023-11-22-09-49-00'
    file = pd.read_csv(path + folder + '/results_DICE.csv', sep=';')
    a_plot = file.boxplot(column='DICE', by='LABEL', fontsize=fontsize, ax=axs.flatten()[0], return_type='axes')
    plt.suptitle('')
    a_plot[0].set_title('Dice Values of ' + folder, fontsize=fontsize + 2)
    a_plot[0].set_xlabel('Brain structure', fontsize=fontsize)
    a_plot[0].set_ylabel('Dice score', fontsize=fontsize)
    a_plot[0].set_ylim([0, 1])

    # Figure Hausdorff
    file = pd.read_csv(path + folder + '/results_HSDRF.csv', sep=';')
    b_plot = file.boxplot(column='HDRFDST', by='LABEL', fontsize=fontsize, ax=axs.flatten()[1], return_type='axes')
    plt.suptitle('')
    b_plot[0].set_title('Hausdorff distance of ' + folder, fontsize=fontsize + 2)
    b_plot[0].set_xlabel('Brain structure', fontsize=fontsize)
    b_plot[0].set_ylabel('Hausdorff distance', fontsize=fontsize)
    b_plot[0].set_ylim([0, 20])

    plt.tight_layout()
    plt.show()

    # alternative: instead of manually loading/reading the csv file you could also use the pandas package
    # but you will need to install it first ('pip install pandas') and import it to this file ('import pandas as pd')
    pass  # pass is just a placeholder if there is no other code


if __name__ == '__main__':
    main()
