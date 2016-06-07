---
title: 'MSiA 490-20 / Ling 400: Homework 2'
author: "Instructor: Klinton Bicknell"
output:
  html_document:
    highlight: pygments
---
_parts adapted from Jorge Moraleda_

**Turning it in**: You'll turn in a zip file via Canvas that contains (a) a write-up as a pdf and (b) the other items described below.

## Tokenization and normalization
The high level goal of this part of the assignment is to explore how differences in preprocessing can affect text analytic results. This also serves to introduce [Apache Lucene Core](https://lucene.apache.org/core/), a powerful text indexing and retrieval library widely used in industry, which we will also be using for later assignments.

1. **Tokenization.** You will compare two widely used tokenizers on a short piece of text named `wsj_0063`. This text was originally published in the _Wall Street Journal_ in 1989 and is now part of the [Penn Treebank](https://www.cis.upenn.edu/~treebank/), a widely used corpus that has been annotated for grammatical structure. While the full Penn Treebank is not free, this file can be found in the corpus's [free sample](http://www.nltk.org/nltk_data/packages/corpora/treebank.zip) as included in the [NLTK](www.nltk.org) project. Note that this data is licensed for non-commercial use only. For the purposes of this exercise we'll be using the raw version of this text, available at `raw/wsj_0063`.

      The two tokenizers to compare are:

      * The [Stanford tokenizer](http://nlp.stanford.edu/software/tokenizer.shtml), included in [Stanford CoreNLP](http://nlp.stanford.edu/software/corenlp.shtml), which was used for the previous assignment. Just as in the previous assignment, note that [Brendan O'Connor's python wrapper](https://github.com/brendano/stanford_corenlp_pywrapper) works well on linux and macs.
      * The standard unicode tokenizer, implemented by [Lucene Core's](https://lucene.apache.org/core/) class [`StandardTokenizer`](http://lucene.apache.org/core/5_3_1/analyzers-common/org/apache/lucene/analysis/standard/StandardTokenizer.html). Like CoreNLP, Lucene is Java software, so if you want to use this on python, you'll need a wrapper. The official one is [PyLucene](http://lucene.apache.org/pylucene/). Note also that, unlike the python wrappers for CoreNLP, PyLucene also works on all major platforms, including Windows.

      You will report the tokenization differences between both approaches. For each line where the tokenization differs between the two approaches, show the original string and the two alternative tokenizations. What patterns do you see in the differences?

2. **Normalization.** You will compare four widely used normalization algorithms, also on `wsj_0063`. Note that in Lucene Core, normalization algorithms are referred to as 'analyzers'. There is a [list of analyzers for English](http://lucene.apache.org/core/5_3_1/analyzers-common/org/apache/lucene/analysis/en/EnglishAnalyzer.html)

      * Lucene Core's [`EnglishAnalyzer`](http://lucene.apache.org/core/5_3_1/analyzers-common/org/apache/lucene/analysis/en/EnglishAnalyzer.html): Lucene Core's default for English, implementing the Porter Stemmer version 2
      * Lucene Core's [`PorterStemFilter`](http://lucene.apache.org/core/5_3_1/analyzers-common/org/apache/lucene/analysis/en/PorterStemFilter.html): implementing the original Porter Stemmer, which is also widely used in analytics
      * Lucene Core's [`KStemFilter`](http://lucene.apache.org/core/5_3_1/analyzers-common/org/apache/lucene/analysis/en/KStemFilter.html): a less aggressive stemmer
      * CoreNLP's lemmatizer: a full-on lemmatizer, not just a quick-and-dirty stemmer; available by requesting `lemma` annotation in CoreNLP.
      
      As for the previous exercise, you will report the differences between these four approaches, for each line where the normalization differs between any of them. Describe the main ways the lemmatizer differs from the stemmers. Also describe the patterns you see in the differences between stemmers.
      
      Note: tokenization must be performed first before normalization. To make this simple, you can use Lucene to tokenize prior to applying the Lucene normalization algorithms and use CoreNLP to tokenizer prior to applying the CoreNLP normalization algorithms.
      
3. **Tokenization and normalization.** You will decide on a tokenization and normalization algorithm to apply to `classbios.txt` from the previous assignment. Make an argument as to why you selected that particular tokenization and normalization algorithm. Format the output so that there is one sentence per line and each token is separated by a space. Include your normalized `classbios.txt` file in the zip.

4. **Basic frequency analysis.** Write a program to calculate the frequency of each (normalized) word in the normalized `classbios.txt` corpus. Report the top 20 most frequent words, excluding stop words and punctuation, and their frequencies. Describe whether you think this list gives much information about this corpus. Did you learn anything about the backgrounds of the class?

5. **Basic bigram analysis.** Write a program to calculate the frequency of each bigram in the corpus (i.e., sequence of two words). Report the top 20 most frequent bigrams, excluding bigrams that include a stop word or punctuation, and their frequencies. Describe whether you think this list gives much information about this corpus. Did you learn anything about the backgrounds of the class?

6. **Sentiment analysis.** For the final exercise, you'll create a naive Bayes classifier to perform binary sentiment analysis on movie reviews. You'll use [Pang & Lee's (2005) polarity dataset 2.0](http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz), which consists of 1000 positive and 1000 negative movie reviews. Note that these reviews have already been pre-processed so that tokenization has already been done. Each review is in its own file, each sentence is on its own line, and each token is followed by a space. Specifically:

      * construct a baseline naive Bayes classifier that uses only words as features. This is the type of naive Bayes classifier we discussed in class, that is equivalent to a unigram language model for each class (positive and negative). To construct it, you'll get the frequencies of every word in the vocabulary in each class, add 1 to all word frequencies in each class, and then normalize each frequency by dividing by the total to get a probability distribution. Finally, take the log of each probability to get a log-probability of each word for each class. [Note that this might be easiest using a vector library like python's `numpy`.] To apply the naive Bayes classifier, you'll calculate the log probability of a test review under each class by summing the log probabilities of each word in the review. (Ignore new words in the test reviews that weren't in training, since your models don't assign them a probability.) Finally, classify according to whichever log probability is higher. (Recall that log probabilities are always negative, so -2 is higher than -4.)
      * evaluate your model: First, train on the first 100 examples in each class (those with filenames beginning with `cv0`), classify the 200 reviews with filenames that begin with `cv6` and `cv7` and report performance: precision, recall, and F score. Then, do the same for training on the first 300 examples, the first 500 examples, and finally, the first 600 examples (`cv0` to `cv5`), in each case testing on those that begin with `cv6` and `cv7`. Do you think performance would improve with even more examples?
      * (optional) for bonus points: make a sentiment analysis system improved in some way from this baseline. This could be switching away from naive Bayes to some other classifier, adding other features, or both. When making your new system, make sure to leave your original system intact. While getting your new system to work, continue testing on the `cv6` and `cv7` files, which we're technically using as a validation set, and make sure that your new system is improving performance on those. Report how much you've improved performance on this set (precision, recall, F score).
      * Finally, evaluate your classifier (and your improved classifier, if you did the bonus) **just once** on the actually held-out test data you haven't yet evaluated on: the 200 files beginning with `cv8` and `cv9`. For this evaluation, train on the first 800 files (`cv0` to `cv7`). Report performance of the original classifier (and your new classifier if you did the bonus) on this data. If your original classifier performance was substantially different evaluated on `cv8` and `cv9` than it was previously on `cv6` and `cv7`, why do you think that was? If you did the bonus, and your new system didn't outperform your original classifier on this new data, but did outperform it previously on the `cv6` and `cv7` files, what do you think happened?
      * **turn it in:** include all your classifier source code and its output predictions for the final test set (`cv8` to `cv9`).