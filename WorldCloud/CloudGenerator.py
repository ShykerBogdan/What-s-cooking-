import numpy as np
import json
import os
import re
from PIL import Image
from os import path, getcwd
from wordcloud import WordCloud
from matplotlib import pyplot as plt


def getFrequencyDictForText():
    with open('IngredientsCount.txt') as f:
        return json.load(f)

def makeImage(FrequencyDict):
    d = getcwd()
    mask = np.array(Image.open(path.join(d, "WorldCloud\\images.png")))

    wc = WordCloud(background_color="white", max_words=1000, scale=100)
    # generate word cloud
    wc.generate_from_frequencies(FrequencyDict)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

makeImage(getFrequencyDictForText())