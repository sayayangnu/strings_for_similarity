Semantic textual similarity using string similarity
---------------------------------------------------

This project examines string similarity metrics for semantic textual similarity.
Though semantics go beyond the surface representations seen in strings, some of these
metrics constitute a good benchmark system for detecting STS.


Data is from the [STS benchmark](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark).

## lab.py

`lab.py` calculates Levenshtein distance for sentence pairs in an STS dataset.

Example usage:

`python lab.py --data stsbenchmark/sts-dev.csv`

## sts_pearson.py

### Homework: 
* Parse the STS data and calculate string similarity metrics (specified in starter code)
for each pair of sentences. 
* Calculate Pearsons R between each metric and the gold standard labels.
* Write the correlations to a file; see `dev_output.txt` for target.
* Check in `test_output.txt` (using `sts-test.csv`) for grading. The order you report the metrics isn't important.
* **HINT:** Normalize case.
* **HINT:** Use `sklearn` for pearsons and `nltk` for most similarity metrics.
* **HINT:** The `nltk` implementation of NIST is buggy where overlap doesn't occur; catch `ZeroDivisionError` 
and record 0, the lowest NIST score.
* **HINT:** Word Error Rate is Levenshtein distance on words.
* **HINT:** Sentence order is not important in the STS dataset, but it is for some metrics.
In these cases, calculate the metric both ways and sum.

TODO: Replace the instructions above with a description of your code.
* Use `.md` filetype
* ~ 1 sentence about each of the metrics used.
* Describe what your script does. Be affirmative and efficient 
(see [guidelines for documenting the Python language]( 
https://devguide.python.org/documenting/#affirmative-tone) )
* Include a usage example showing command line flags
* Describe your output
* More README philosophy [here](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project) 
