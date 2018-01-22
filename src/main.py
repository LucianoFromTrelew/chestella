import argparse

def create_parser():
    parser = argparse.ArgumentParser(
        prog="cst",
        description="argparse test")

    parser.add_argument("name")

    return parser

def main():
    parser = create_parser()
    parser.parse_args()

if __name__ == "__main__":
    main()
