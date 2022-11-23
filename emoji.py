import io
import os
import string
from os import path
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# It is important to use io.open to correctly load the file as UTF-8
# text = io.open(path.join(d, 'happy-emoji.txt')).read()
text = io.open('happy-emoji.txt').read()

# the regex used to detect words is a combination of normal words, ascii art, and emojis
# 2+ consecutive letters (also include apostrophes), e.x It's
normal_word = r"(?:\w[\w']+)"
# 2+ consecutive punctuations, e.x. :)
ascii_art = r"(?:[{punctuation}][{punctuation}]+)".format(punctuation=string.punctuation)
# a single character that is not alpha_numeric or other ascii printable
emoji = r"(?:[^\s])(?<![\w{ascii_printable}])".format(ascii_printable=string.printable)
regexp = r"{normal_word}|{ascii_art}|{emoji}".format(normal_word=normal_word, ascii_art=ascii_art,
                                                      emoji=emoji)

# Generate a word cloud image
# The Symbola font includes most emoji
font_path = 'Symbola.ttf' # path.join(d, 'fonts', 'Symbola', 'Symbola.ttf')
wc = WordCloud(font_path=font_path, regexp=regexp).generate(text)
wc.to_svg()
# Display the generated image:
# the matplotlib way:
# import matplotlib.pyplot as plt
# plt.imshow(wc)
# plt.axis("off")
# plt