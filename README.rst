DamerauLevenshteinDerivor

Author: Amber & Zooko Wilcox-O'Hearn

Contact: amber@cs.toronto.edu, zooko@zooko.com

Released under the GNU AFFERO GENERAL PUBLIC LICENSE, see COPYING file for details.

============
Introduction
============
Functionality in Brief:

DamerauLevenshteinDerivor reads a vocabulary file that has one word per line in
it, storing the words into a Judy array.  The vocabulary can then be queried.
In addition, derivor will return a list of all words in the vocabulary that are
of Damerau-Levenshtein distance one from a given word.

The storage and calculations are done in C and available through the C
executable, as well as through a Python interface.  

============
Dependencies
============
DamerauLevenshteinDerivor requires:

A C compiler, Python, make, Judy Trees library (http://judy.sourceforge.net/)

It was tested under the following versions:

* Judy Trees  1.0.5
* Ubuntu 12.04.2 LTS
* Python 2.7.3
* GNU make 3.81

========
Building
========
run
::

 $ make

=================
Running the tests
=================
run
::

 $ make test

==========
Installing
==========
run
::

 $ make install

This will copy the ``derivor`` executable into $prefix/bin
and will execute ``python setup.py install``, which will result in the
derivor Python module being copied into the appropriate place in
your Python installation.

===========
Example Use
===========

>>> from DamerauLevenshteinDerivor import cderivor
>>> d = cderivor.Derivor('/bin/derivor', 'my_vocabulary_file')
>>> d.variations('as')
['a', 'is', 'us', 'al', 'an', 'at', 'has', 'was']
>>> d.inV('as')
True
>>> d.inV('asx')
False
