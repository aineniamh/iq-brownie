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


