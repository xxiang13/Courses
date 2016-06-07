---
title: 'MSiA 490-20 / Ling 400: Homework 1'
author: "Instructor: Klinton Bicknell"
output:
  html_document:
    highlight: pygments
---
_adapted from Jorge Moraleda and Jurafsky & Martin (2008)_

**Turning it in**: You'll turn in everything described below as a zip file via Canvas.

## Regular expressions
In this assignment you will write a program that will take as input one plain text file and will print as output every sentence of the input file that contains a time point. Finding time points is a frequent task in text analytics. Regular expressions are well suited for this task and that is what we will use for this assignment.

A time point could be an absolute date (e.g. "October 31st, 2013" or "10/31/13"), an absolute time (e.g. "14:00 PST") or even a relative time (e.g. "the day my mother was born"). However the sentence "Many days I eat toast for breakfast." does not contain a time point.

The examples above exemplify that in this task, as is often the case in text analytics, problems are not well defined at the onset. In this case, what is or not a time point will depend on the actual problem one is trying to solve. For this assignment you will have to decide what patterns you want your program to capture.

### Relevant packages

There are two components to this task. One is to split the text file into sentences and the other is to determine which sentences contain a time point using regular expressions.

**Sentence splitting** To split the file into sentences, I recommend using [Stanford CoreNLP](http://nlp.stanford.edu/software/corenlp.shtml), to become familiar with the package, since we will be using it for later assignments. You may also want to read the [documentation for its tokenizer](http://nlp.stanford.edu/software/tokenizer.shtml), since it also performs sentence segmentation.

CoreNLP is Java software, so you may use it natively from Java. To access it from within Python, you'll need to use a wrapper. One good one is [Brendan O'Connor's](https://github.com/brendano/stanford_corenlp_pywrapper), which works on Unix/Linux/Mac systems. More python wrappers are listed at the bottom of [the main CoreNLP page](http://nlp.stanford.edu/software/corenlp.shtml). 

**Regular expressions**

Java and Python both have good built-in regular expression support: the [`re` module](https://docs.python.org/2/library/re.html) in Python and [java.util.regex](http://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html) in Java. In both languages, regular expressions are constructed from strings. You can assemble a very large string by concatenating smaller strings using the `+` operator. Assembling your final regular expression string from shorter substrings will allow you to give meaningful names to each substring and reuse them.

### Deliverables
1. A folder named `src` containing all your source code.

2. A plain text file `classbios_timepoints.txt` containing the output of your program when run with `classbios.txt` as input, one sentence per line.

3. A plain text file `readme.txt` containing an explanation of which patterns you have chosen or not chosen to capture, and any other thoughts you would like to share.

4. A plain text file `regex.txt` containing the regular expression that you have chosen to use to detect time points. If you used substrings, include the substrings and the logic to assemble them instead of the final string itself. It will help with understanding what you've done!

## Finite-state automata
<figure><img src="fsa.svg" style="width:400px"></figure>

5. For the above non-deterministic finite-state automaton, write 10 strings that the automaton would accept in a file called `fsa.txt`, one string per line.