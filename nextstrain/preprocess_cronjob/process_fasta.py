
def main():
    in_file = 'sequences_fasta_2021-04-28.fa'
    out_file = 'new_sequences.fa'
    with open(in_file, 'r') as i, open(out_file, 'w') as o:
        for line in i:
            o.write(  extract_id(line) if line.startswith('>') else line )


def extract_id(line):
    return f">{line.split('|')[1]}\n"

if __name__ == '__main__':
    main()

