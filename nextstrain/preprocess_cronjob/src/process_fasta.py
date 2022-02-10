""" Usage: process_fasta.py <input.fa> [-o output.fa]

-o, --output output.fa      The path of the output file [default: ./output.fa]

"""
from docopt import docopt


def main(args: dict):
    with open(args["<input.fa>"], "r") as i, open(args["--output"], "w") as o:
        for line in i:
            o.write(extract_id(line) if line.startswith(">") else line)


def extract_id(line: str) -> str:
    return f">{ line.split('|')[1] or line }\n"


if __name__ == "__main__":
    main(docopt(__doc__))

