def dct_to_fasta(d, fn):
    import re, sys, traceback, os
    fileName, fileExtension = os.path.splitext(fn)
    try:
        assert fileExtension.lower() in [".fasta", ".fa", ".fas", ".fna", ".ffn", ".faa", ".frn"]
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print('An error occurred on line {} in statement {}'.format(line, text))
        exit(1)
    try:
        with open(fn, "w") as fw:
            for k, v in d.items():
                fw.write(">"+k+"\n"+v+"\n")
        return True
    except Exception as e:
        print e
        return False

def fasta_to_dct(fn):
    from Bio import SeqIO
    import re, sys, traceback, os
    fileName, fileExtension = os.path.splitext(fn)
    try:
        assert fileExtension.lower() in [".fasta", ".fa", ".fas", ".fna", ".ffn", ".faa", ".frn"]
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print('An error occurred on line {} in statement {}'.format(line, text))
        exit(1)
    dct = {}
    for sequence in SeqIO.parse(open(fn), "fasta"):
        dct[sequence.description.replace(" ", "_")] = str(sequence.seq)
    return dct


def main():
    print("In main of fasta_tools.py")
