import argparse
import os.path
import snakemake
import sys
import pprint
import json

from . import _program


thisdir = os.path.abspath(os.path.dirname(__file__))
cwd = os.getcwd()

def main(sysargs = sys.argv[1:]):
    parser = argparse.ArgumentParser(prog = _program, 
    description='iqbrownie: taxon hashing so names dont get corrupted when running iqtree',
    usage='''iqbrownie -s ALIGNMENT [options for iqtree]''')

    parser.add_argument('-s', action="store", dest="alignment")

    if len(sysargs)<2:
        parser.print_help()
        sys.exit(-1)
    else:
        args = parser.parse_args(sysargs[:2])

    iqtree_config =sysargs[2:]
    pass_to_iqtree = "!".join(iqtree_config)
    print(pass_to_iqtree)

    threads = 1
    try:
        for i in range(len(iqtree_config)):
            if iqtree_config[i] == "-nt":
                threads = int(iqtree_config[i+1])
    except:
        threads =1

    # first, find the Snakefile
    snakefile = os.path.join(thisdir, 'scripts/Snakefile')
    if not os.path.exists(snakefile):
        sys.stderr.write('Error: cannot find Snakefile at {}\n'.format(snakefile))
        sys.exit(-1)
    else:
        print("Found the snakefile")

    alignment = os.path.join(cwd, args.alignment)
    if not os.path.exists(alignment):
        sys.stderr.write('Error: cannot find alignment at {}\n'.format(alignment))
        sys.exit(-1)
    else:
        print(f"The alignment file is {alignment}")

    # next, make the config_string

    config = {"alignment":alignment, "pass_to_iqtree":pass_to_iqtree}

    # run subtyping
    status = snakemake.snakemake(snakefile, printshellcmds=True,
                                 forceall=True,
                                 config=config,cores=threads,lock=False
                                 )

    if status: # translate "success" into shell exit code of 0
       return 0
    return 1

if __name__ == '__main__':
    main()