#!/usr/bin/python
"""Usage: annotate.py <directory> [-g PATTERN] [--tempdir TEMPDIR]
    [-t THREADS] [-o OUTDIR]

-g PATTERN          Glob pattern [default: *.fa].
--tempdir TEMPDIR   Temporary directory
-o OUTDIR           Output directory [default: ./].
-t THREADS          Number of threads to use [default: 4].

"""
import os, sys, subprocess, datetime, requests, glob, pandas as pd
from docopt import docopt


def main(args):

    for seq_file in glob.glob(f"{args['<directory>']}/{args['-g']}"):
        print(f"Running pangolin on {seq_file}")
        try:
            cmd = subprocess.run(
                f"pangolin "
                f"--outdir {args['-o'] or args['<directory>']} "
                f"--tempdir {args['--tempdir']} "
                f"--outfile {os.path.basename(seq_file)}.csv "
                f"--min-length 1000 "
                f"--threads {args['-t']} "
                f"{seq_file}",
                shell=True,
                capture_output=True
            )
            cmd.check_returncode()
        except subprocess.CalledProcessError as e:
            print(f"Error running pangolin on {seq_file}: {e.output}")
    dfs = pd.concat([
        pd.read_csv(file, sep="\t")
        for file
        in glob.glob(f"{args['-o']}/*.csv")
    ])
    dfs.to_csv(f"{args['-o']}/combined.csv", sep="\t", index=False)
    print(dfs)


if __name__ == "__main__":
    args = docopt(__doc__)
    main(args)

