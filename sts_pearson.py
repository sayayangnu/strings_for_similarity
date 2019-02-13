import argparse

def main(sts_data, output_file):
    """Calculate pearson correlation between semantic similarity scores and string similarity metrics.
    Data is formatted as in the STS benchmark"""

    score_types = ["NIST", "BLEU", "Word Error Rate", "Longest common substring", "Levenshtein distance"]


    with open(output_file, 'w') as out:
        out.write(f"Semantic textual similarity for {sts_data}\n")
        # TODO: write scores. See example output for formatting

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sts_data", type=str, default="stsbenchmark/sts-dev.csv",
                        help="text file containing API key")
    parser.add_argument("--output_file", type=str, default="dev_output.txt",
                        help="report on string similarity ")
    args = parser.parse_args()

    main(args.sts_data, args.output_file)
