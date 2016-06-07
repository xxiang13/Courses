---
title: 'MSiA 490-20 / Ling 400: Homework 3'
author: "Instructor: Klinton Bicknell"
output:
  html_document:
    highlight: pygments
---
_adapted from Jorge Moraleda_

**Turning it in**: You'll turn in a zip file via Canvas that contains (a) a write-up as a pdf, (b) all your code, and (c) the other items described below.

## Document similarity
Calculating document similarity is the first step in many text analytic tasks, including clustering and finding similar documents to a single one known to be of relevance. In this part of the assignment, you'll compare different ways of computing document similarity.

0. **Splitting, tokenization, normalization.** In order to have a set of documents to calculate similarities between, split the `classbios.txt` file into one file per person. (Note that you can use regular expressions to do this.) Then, tokenize and normalize these files using any of the methods (in Lucene or CoreNLP) you used on the previous assignment. Next, remove stopwords and any words that contain non-alphabetic characters (e.g., puncutation or numbers), using any method you like. [No need to say anything about this problem in your write-up, but do include the code in your zip.]

1. **Boolean similarity.** Use the normalized, tokenized bio documents to create a binary term-document matrix, where each row represents a vocabulary item, each column represents a document, and each element is a 0 or 1. In this matrix, each document is represented by a binary vector. From this binary matrix, create a document similarity matrix, where cell _i, j_ gives the similarity of documents _i_ and _j_, and where similarity is given by the cosine between the document vectors: $\dfrac{I \cdot J}{\sqrt{|I| |J|}}$. Save this matrix to a file `boolean.txt`, where values are separated by a space, and where the rows and columns are arranged in alphabetical order of filename (i.e., the same order they were given in `classbios.txt`). Do not include any row or column labels in this file. In your write-up, answer: _Which three pairs of documents are the most similar? Which three pairs are the least similar?_

2. **tf-idf similarity.** Use the normalized, tokenized bio documents to create a term-document matrix of raw frequencies. Then transform this raw frequency matrix into a tf-idf matrix by using the formula $(1+\log(tf))(\log(\dfrac{N}{df}))$ where $tf$ is the term's raw frequency in this document, $df$ is the number of documents the term occurs in, and $N$ is the total number of documents. Now, again, convert this term-document matrix into a document similarity matrix in the same way as before and save it as `tf_idf.txt`, in the same format as before. In your write-up, answer: _Which three pairs of documents are the most similar now? Which three pairs are the least similar? Does this more advanced method seem to be doing a better job than just using binary similarity? Why?_ 


## Indexing and retrieval
On the last assignment, you used Lucene simply to tokenize and normalize text, but its main function is as a full industrial-strength indexing and retrieval library. Thus, indexing text using Lucene is very often the first step to doing analytics. In this part of the assignment, you'll gain practice in using Lucene for indexing and retrieval.

3. **Indexing.** Index the wikipedia pages for countries and their capitals. [This page](https://en.wikipedia.org/wiki/List_of_national_capitals_in_alphabetical_order) contains links to every country and its capital.
    * To accomplish this, first, create a Lucene index. Then, add the text from the wikipedia entry for each capital city and each country. Specifically, add one document to the index for each capital city you extract using four Lucene fields: `city_name`, `country_name`, `city_text`, and `country_text`.
    * As in many cases in real-world analytics, there will be some special cases in which countries have more than one capital. Decide how to treat these cases and document it in your write-up. Also say how many capital cities you included, and how many countries.
    * To download the webpages, you may need to use parts of Java (or python) you haven't used before. For Java, [this](http://docs.oracle.com/javase/tutorial/networking/urls/) is a good introduction to working with URLs. In python, you'll want to check out [urllib](https://docs.python.org/2/library/urllib.html).
    * For specific examples of adding documents to a Lucene index, see [the Lucene tutorial slides](http://kbicknell.github.io/ling400fall2015/dl/ling400_class5c.pdf) from class a couple of weeks ago and [the Lucene in Action](http://www.manning.com/hatcher3/) source code download.
    * There's no need to use any fancy html parsing libraries for this assignment, but you will need to strip out the html from the web pages before sending them on to an `EnglishAnalyzer` and indexing them. One convenient way to do this is to use the [`HTMLStripCharFilter`](https://lucene.apache.org/core/5_3_1/analyzers-common/org/apache/lucene/analysis/charfilter/HTMLStripCharFilter.html) class.
    
4. **Retrieval.** Use the index you just created to find all the **capital cities** whose wikipedia page (the city's page, not the country's page) contains each of the following, and report the results in your write-up.
    * 'Greek' and 'Roman' but not 'Persian': Use a `BooleanQuery` for this. In addition to the Lucene docs, you might find [this page](http://www.avajava.com/tutorials/lessons/how-do-i-combine-queries-with-a-boolean-query.html) a useful reference.
    * 'Shakespeare', even if it's misspelled: Use a `FuzzyQuery` for this.
    * the words 'located below sea level' near each other: Use a `PhraseQuery` with a slop factor of 10. In addition to the Lucene docs, you might find [this page](http://www.avajava.com/tutorials/lessons/how-do-i-query-for-words-near-each-other-with-a-p
hrase-query.html;jsessionid=F8E217756EFD1C548247EDD86E76F844) a useful reference.
    * an interesting query of your choice.

5. **Latent Dirichlet Allocation.** Lucene indexes can conveniently return a frequency-based term-document matrix, which can be fed into topic modeling algorithms such as LDA to provide insights into the major topics described in a corpus. This is what you'll do for this final exercise.
    * First, extract the term-document matrix from your index for the set of **country** pages (not the city pages). See [this example](http://stackoverflow.com/questions/12098083/term-vector-frequency-in-lucene-4-0).
    * Use LDA to create a table with the 10 most frequent topics and the 10 most frequent words in each of them. Report these in your write-up. There are a huge number of LDA packages available to do this, including [JGibbLDA](http://jgibblda.sourceforge.net/) for Java and [lda](https://pypi.python.org/pypi/lda) for python. Use whichever you please. (Note that unless you set random seeds, these results will not be reproducible, since this is a random algorithm. Just an FYI: you are not required to set random seeds.)