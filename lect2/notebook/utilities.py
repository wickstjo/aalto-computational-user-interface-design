import re, time
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
from collections import Counter

#import matplotlib.pyplot as plt




def showmenu(labels):
    def on_button_clicked(b):                                  # store clicks to data.csv
        with output:
            with open('data.csv','a') as fd:
                m = re.search(r'description=\'(.*)\'', str(b)) # extract label from button object str
                button_label = m.group(1)
                index = labels.index(button_label)
                fd.write(str(index) + "," + button_label + "," + str(time.time()) + "\n")
    def closed_button(b):
        menu.close()

    elements = []
    for label in labels:
        if label == "-":
            elements.append(widgets.Label(" "))
        else:
            element = widgets.Button(description=label, button_style='info', disabled=False)
            element.on_click(on_button_clicked)
            elements.append(element)
    elements.append(widgets.Label(" "))
    closebutton = widgets.Button(description='Stop', button_style='',disabled=False)
    closebutton.on_click(closed_button)
    elements.append(closebutton)

    menu = widgets.VBox(elements)
    output = widgets.Output()
    display(menu,output)

# Parses user data, returns a Counter object with click counts
def parsedata():
    return Counter(re.findall('[a-z\-]+', open('data.csv').read(), flags=re.IGNORECASE))

# By Tayyaba Taimur
def plothistogram(menuList):
    frequencies = parsedata()
    xBar = []
    yBar = []

    for item in menuList:
        if(frequencies[item] is not None):
            xBar.append(item)
            yBar.append(frequencies[item])
    y_pos = np.arange(len(xBar))
    plt.bar(y_pos, yBar, align='center', alpha=0.5)
    plt.xticks(y_pos, xBar)
    plt.ylabel('Clicks')
    plt.show()
