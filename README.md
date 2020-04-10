# iqbrownie
taxon hashing for [iqtree](http://www.iqtree.org/). 

### Installation

Recommended install is to create the ``iqbrownie`` environment using [conda](https://docs.conda.io/en/latest/miniconda.html). This will install all dependencies, including ``iqtree``. 

```
conda env create -f environment.yml
```

### Usage

``iqbrownie`` has all the functionality of iqtree, and will pass arguments through to iqtree, but just cocoons your taxon names in a little safe hash. 

```
usage: iqbrownie -s ALIGNMENT [options for iqtree]

iqbrownie: taxon hashing so names dont get corrupted when running iqtree

optional arguments:
  -s ALIGNMENT
```

### Output

Your tree file will be output by default in the same directory as your alignment, with the same file name stem sans the ``.fasta``.

### References

B.Q. Minh, H.A. Schmidt, O. Chernomor, D. Schrempf, M.D. Woodhams, A. von Haeseler, R. Lanfear (2020) IQ-TREE 2: New models and efficient methods for phylogenetic inference in the genomic era. Mol. Biol. Evol., in press:. https://doi.org/10.1093/molbev/msaa015

