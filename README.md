# Common Word Translator
---
This is a command line program to translate words into a provided text file into their 
[most common ten hundred word][1] replacements (if possible), a la [xkcd thing explainer][2].

## Installation
---
This program is provided as a python package and can be installed through the command:
    
    python setup.py install

## Translating text
---
To translate a text file, use the `translate_common_word` script located under `bin`. This script requires a 
*word embedding* (in text format), a *common words dictionary*, an *input text file* to be translated, 
and an *output destination*.

#### Translation Command Example

    prompt$ ./bin/translate_common_words data/text9.vec data/1000.dicin ~/Downloads/pg345.txt ~/Downloads/output.txt
    Setting up translator...
    Reading source...
    Translating text...
    Replaced 38388 words from 167231 in 20284 sentences
    Writing translation...
    Done

I have provided an embedding (`data/text9.vec`) and dictionary (`data/1000.dicin`). The provided word embedding
was constructed from some wikipedia article data and may not contain a complete matching vocabulary for the
input document. Any words that are not considered common and are not contained within the embedding are not
replaced.

I utilized [Facebook AI Research's fastText][3] to generate the embedding. Feel free to generate your own and
use it in translations instead.

## Limitations
---
As mentioned in the translation section, it only replaces words that can be found in the word embedding. It also
does not attempt to maintain any kind of fluency, and does not account for groups of words that should be considered
for joint replacement. These limitations, however, do reuslt in quirky, sometimes comedic output.

[1] http://splasho.com/upgoer5/phpspellcheck/dictionaries/1000.dicin
[2] https://xkcd.com/thing-explainer/
[3] https://github.com/facebookresearch/fastText
