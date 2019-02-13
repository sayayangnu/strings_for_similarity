import argparse

def main(sts_data):
    """Calculate Levenshtein distance for pairs of strings
    Data is formatted as in the STS benchmark"""

    # read the dataset. Open the text file in an editor to see the fields
    texts = []
    labels = []

    # iterate through a few examples to inspect the texts and scores
    # prints nothing while len(texts) == 0
    for i,pair in enumerate(texts[:10]):
        t1 = ""
        t2 = ""
        print(f"Sentences: {t1}\t{t2}")
        # calculate the edit distance using nltk
        dist = 0
        print(f"Label: {labels[i]}, edit distance: {dist}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sts_data", type=str, default="stsbenchmark/sts-dev.csv",
                        help="text file containing API key")
    args = parser.parse_args()

    main(args.sts_data)
