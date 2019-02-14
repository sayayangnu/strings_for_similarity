from nltk.metrics.distance import edit_distance
import argparse

def main(sts_data):
    """Calculate Levenshtein distance for pairs of strings
    Data is formatted as in the STS benchmark"""

    # read the dataset
    texts = []
    labels = []

    with open(sts_data, 'r') as dd:
        for line in dd:
            fields = line.strip().split("\t")
            labels.append(float(fields[4]))
            t1 = fields[5].lower()
            t2 = fields[6].lower()
            texts.append((t1, t2))

    print(f"Found {len(texts)} STS pairs")

    for i,pair in enumerate(texts[200:210]):
        t1, t2 = pair
        print(f"Sentences: {t1}\t{t2}")
        # calculate the edit distance
        dist = edit_distance(t1, t2)
        print(f"Label: {labels[i]}, edit distance: {dist}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sts_data", type=str, default="stsbenchmark/sts-dev.csv",
                        help="sts data")
    args = parser.parse_args()

    main(args.sts_data)
