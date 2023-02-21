import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--shards",
    default=5,
    type=int,
    help="Split the dataset in the given number"
)
args = parser.parse_args()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(args.shards)
    pass


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
