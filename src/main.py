import argparse
import sys
from project.Project import Project


def create_parser():
    parser = argparse.ArgumentParser(
        prog="chestella",
        description="chestella: a c-project manager")

    subparser = parser.add_subparsers()

    #init command
    init_parser = subparser.add_parser('init', help='create a new project')
    init_parser.add_argument('name', help='Name of the brand new project')

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    Project(args.name)



if __name__ == "__main__":
    main()
