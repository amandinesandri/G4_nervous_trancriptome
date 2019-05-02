#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import sys
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show
import sys
import matplotlib.patches
import pylab


#argument: la feature gene_type, le file, le score


def box_plot(file_name, feature, score):
	
	df=pd.read_csv(file_name, sep=None, engine="python")
	counts=df[feature].value_counts()
	total_number_of_category=counts.size

	"""
	#des prints pour tester les values
	print("premier index du counts ---> ", counts.index[0])
	print("total_number_of_category : ", total_number_of_category)
	print("liste des catégories : ", counts.index)
	print("data_"+counts.index[1])
	"""

	data_name=[]
	data=[]
	for i in range(total_number_of_category):
	    data_name.append(("data_"+counts.index[i]))
	    #print("la liste des datas à boxploter est : ", data_name)
	    #data[i]= les valeurs de scores G4 (ie =df[score] quand colonne des features correspond [...]
	    #[...] à un certain index ie quand df[feature]==counts.index[i]
	    data.append(df.loc[df[feature] == counts.index[i]][score])
	#print("la liste des score extraite est :\n ", data[1], "\n")

	fig, ax1 = plt.subplots(figsize=(20, 10))
	fig.canvas.set_window_title('A Boxplot Example')
	fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

	bp = ax1.boxplot(data, notch=0, sym='+', vert=1, whis=1.5)
	plt.setp(bp['boxes'], color='black')
	plt.setp(bp['whiskers'], color='black')
	plt.setp(bp['fliers'], color='red', marker='+')
	# Add a horizontal grid to the plot, but make it very light in color
	# so we can use it for reading data values but not be distracting
	ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
		       alpha=0.5)
	# Hide these grid behind plot objects
	ax1.set_axisbelow(True)
	ax1.set_title('Distribution of '+score+' score')
	ax1.set_xlabel(feature)
	ax1.set_ylabel(score)


	# Set the axes ranges and axes labels
	ax1.set_xlim(0.5, total_number_of_category + 0.5)
	top = 40
	bottom = -5
	ax1.set_ylim(bottom, top)
	ax1.set_xticklabels(data_name,
		            rotation=45, fontsize=8)

	# Due to the Y-axis scale being different across samples, it can be
	# hard to compare differences in medians across the samples. Add upper
	# X-axis tick labels with the sample medians to aid in comparison
	# (just use two decimal places of precision)
	medians = list(range(total_number_of_category))

	pos = np.arange(total_number_of_category) + 1
	upperLabels = [str(np.round(s, 2)) for s in medians]
	weights = ['bold', 'semibold']
	for tick, label in zip(range(total_number_of_category), ax1.get_xticklabels()):
	    k = tick % 2
	    ax1.text(pos[tick], top - (top*0.05), upperLabels[tick],
		     horizontalalignment='center', size='x-small', weight=weights[k])


	plt.savefig('G4_box_plot_'+score+'score'+feature+'.png')

	plt.show()


def usage(error_message=False):
    """
Explain the arguments to add as input
    """
    print("Usage: python PATH/TO/box_plot.py [OPTIONS...]")
    print("Use -h, -? or --help to show this message\n")
    print("Options:")
    print("  -f, --file-name\tTake the name of the file where there is the features to be plotted")
    print("  -c, --category    \tTake the feature name of the column containing the features to be plotted")
    print("  -s, --score     \tTake the name of the score cGcC, G4NN or G4H containing the ")
    print("  -e, --error     \tRaise errors and exceptions\n")
    if error_message:
        print("UsageError:", error_message)
        sys.exit(500)
    else:
        sys.exit(0)

def main():
    """
    Handles arguments.
    """
    option_dict = {}
    for no, arg in enumerate(sys.argv):
        if arg[0] == "-":
            if arg in ["-h","-?","--help"]:
                usage()
            elif arg in ["-v","--verbose",
                    "-e","--error"]:
                option_dict[arg] = True
            elif arg in ["-f","--file-name",
                    "-c","--category", "-s", "--score"]:
                option_dict[arg] = sys.argv[no+1]
            else:
                usage('Argument "%s" not recognized'%arg)
    if len(sys.argv) == 1:
        usage()
    try:
        box_plot(option_dict.get("-f") or option_dict.get("--file-name"),
                option_dict.get("-c") or option_dict.get("--category"), 
		option_dict.get("-s") or option_dict.get("--score"))
    except:
        if "-e" in option_dict.keys() or "--error" in option_dict.keys():
            raise
        else:
            usage('An option is missing, incorrect or not authorized')

if __name__ == '__main__':
    main()
