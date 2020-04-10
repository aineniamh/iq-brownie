# iqbrownie
taxon hashing for [iqtree](http://www.iqtree.org/). 

### Installation

Recommended install is to clone this repo and create the ``iqbrownie`` environment using [conda](https://docs.conda.io/en/latest/miniconda.html). This will install all dependencies, including ``iqtree``. 

```
conda env create -f environment.yml
```

Otherwise, you can pip install this repository with:

```
pip install git+https://github.com/aineniamh/iq-brownie
```

But you'll need to then install ``iqtree`` and ``snakemake-minimal`` yourself. More details about dependencies are found in the ``environment.yml`` file. 

### Usage

``iqbrownie`` has all the functionality of iqtree, and will pass arguments through to iqtree, but just cocoons your taxon names in a little safe hash. 

```
iqbrownie: taxon hashing so names dont get corrupted when running iqtree

usage: iqbrownie -s ALIGNMENT [options for iqtree]

```

### Output

Your tree file will be output by default in the same directory as your alignment, with the same file name stem sans the ``.fasta``.

### References

B.Q. Minh, H.A. Schmidt, O. Chernomor, D. Schrempf, M.D. Woodhams, A. von Haeseler, R. Lanfear (2020) IQ-TREE 2: New models and efficient methods for phylogenetic inference in the genomic era. Mol. Biol. Evol., in press:. https://doi.org/10.1093/molbev/msaa015

