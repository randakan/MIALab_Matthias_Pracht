import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk

import glob
import os


def main():
    # Create object
    root = tk.Tk()

    # Adjust size
    root.geometry("400x200")

    # Dropdown menu options
    list_of_files = glob.glob("data_archive/*/") + glob.glob("mia-result/*/")  # * means all, if you need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    baseline = "baseline"
    options = list_of_files + [baseline]

    # datatype of menu text
    clickedBase = tk.StringVar()
    clickedOther = tk.StringVar()

    # initial menu text
    clickedBase.set(baseline)
    clickedOther.set(latest_file)

    # Create Dropdown menu
    dropBase = tk.OptionMenu(root, clickedBase, *options)
    dropBase.pack(expand=True)
    dropOther = tk.OptionMenu(root, clickedOther, *options)
    dropOther.pack(expand=True)

    def show():
        # destroy
        root.destroy()

        # get path
        pathBase = clickedBase.get()
        pathOther = clickedOther.get()
        if not pathBase or not pathOther:
            raise "noooooooooo"

        readFiles(pathBase)
        readFiles(pathOther)

        plt.show()

    # Create button
    button = tk.Button(root, text="I've chosen", command=show)
    button.pack(expand=True)

    # Execute tkinter
    root.mainloop()
    print("bye")


def readFiles(completePath):
    path = os.path.dirname(completePath)
    folder = os.path.basename(completePath)

    fig, axs = plt.subplots(1, 2)
    fontsize = 10

    # Figure Dice
    column = 'DICE'
    file = pd.read_csv('./' + path + '/' + folder + '/results_DICE.csv', sep=';')
    a_plot = file.boxplot(column=column, by='LABEL', fontsize=fontsize, ax=axs.flatten()[0], return_type='axes')
    plt.suptitle('')
    a_plot[column].set_title('Dice Values of ' + folder, fontsize=fontsize + 2)
    a_plot[column].set_xlabel('Brain structure', fontsize=fontsize)
    a_plot[column].set_ylabel('Dice score', fontsize=fontsize)
    a_plot[column].set_ylim([0, 1])

    # Figure Hausdorff
    column = 'HDRFDST'
    file = pd.read_csv('./' + path + '/' + folder + '/results_HSDRF.csv', sep=';')
    b_plot = file.boxplot(column=column, by='LABEL', fontsize=fontsize, ax=axs.flatten()[1], return_type='axes')
    plt.suptitle('')
    b_plot[column].set_title('Hausdorff distance of ' + folder, fontsize=fontsize + 2)
    b_plot[column].set_xlabel('Brain structure', fontsize=fontsize)
    b_plot[column].set_ylabel('Hausdorff distance', fontsize=fontsize)
    b_plot[column].set_ylim([0, 20])

    plt.tight_layout()

    #plt.show()

    # alternative: instead of manually loading/reading the csv file you could also use the pandas package
    # but you will need to install it first ('pip install pandas') and import it to this file ('import pandas as pd')
    pass  # pass is just a placeholder if there is no other code


if __name__ == '__main__':
    main()
