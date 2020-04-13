import argparse
import os.path
import os
import sys
import pprint
import json
import subprocess

from . import _program

thisdir = os.path.abspath(os.path.dirname(__file__))
cwd = os.getcwd()

    input:
        config["alignment"]
    output:
        fasta = config["outdir"] + "/temp/hash.fasta"
        
def anonymise_headers(alignment,output):


    c = 0
    with open(output.fasta, "w") as fw:
        for record in SeqIO.parse(input[0],"fasta"):
            c+=1
            taxon_hash = ""
            if "EPI_ISL_406801" in record.id: # this is the WH04 GISAID ID
                taxon_hash = f"taxoutgroup_Atax"
            else:
                taxon_hash = f"tax{c}tax"
            taxa_hash.store(record.id,taxon_hash)
            fw.write(f">{taxon_hash}\n{record.seq}\n")
        
        print(f"{c+1} anonymised sequences written to {output.fasta}")



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
    pass_to_iqtree = " ".join(iqtree_config)
    print(pass_to_iqtree)

    threads = 1
    try:
        for i in range(len(iqtree_config)):
            if iqtree_config[i] == "-nt":
                threads = int(iqtree_config[i+1])
    except:
        threads =1




    alignment = os.path.join(cwd, args.alignment)
    if not os.path.exists(alignment):
        sys.stderr.write('Error: cannot find alignment at {}\n'.format(alignment))
        sys.exit(-1)
    else:
        print(f"The alignment file is {alignment}")

    outname = ".".join(alignment.split(".")[:-1])+".tree"
    print("Outname:", outname)

    iq_tree_call = ["iqtree","-s",alignment]
    for i in iqtree_config:
        iq_tree_call.append(i)
    print(iq_tree_call)
    
    status = subprocess.call(iq_tree_call) 

    # next, make the config_string

    # config = {"alignment":alignment, "pass_to_iqtree":pass_to_iqtree}

    # run subtyping
    # status = snakemake.snakemake(snakefile, printshellcmds=True,
    #                              forceall=True,
    #                              config=config,cores=threads,lock=False
    #                              )

    if status: # translate "success" into shell exit code of 0
       return 0
    return 1

if __name__ == '__main__':
    main()