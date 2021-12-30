# kimchi.py
# For converting Python 2 pickles to Python 3
from prepro import *

import os
import dill
import pickle
import argparse
#import class_def

#import vocabulary.Vocabulary
from build_vocab import Vocabulary # Import Foo into main_module's namespace explicitly

def convert(old_pkl):
    """
    Convert a Python 2 pickle to Python 3
    """
    # Make a name for the new pickle
    new_pkl = os.path.splitext(os.path.basename(old_pkl))[0]+"_p3.pkl"

    # Convert Python 2 "ObjectType" to Python 3 object
    dill._dill._reverse_typemap["ObjectType"] = object

    # Open the pickle using latin1 encoding
    with open(old_pkl, "rb") as f:
        loaded = pickle.load(f, encoding="latin1")

    # Re-save as Python 3 pickle
    with open(new_pkl, "wb") as outfile:
        pickle.dump(loaded, outfile)


if __name__ == "__main__":
    #class_def.main()
    #parser = argparse.ArgumentParser(
    #    description="Convert a Python 2 pickle to Python 3"
    #)

    #parser.add_argument("infile", help="Python 2 pickle filename")

    #args = parser.parse_args()

    convert('/home/SERILOCAL/efi.tsamoura/Downloads/DPL.Release/DPL.Release/EL_release/code_data/data/pubmed_parsed/gene_0_new/0/soft_featureset_1/test_5.pkl')
    convert('/home/SERILOCAL/efi.tsamoura/Downloads/DPL.Release/DPL.Release/EL_release/code_data/data/pubmed_parsed/gene_0_new/0/soft_featureset_1/train_3.pkl')
    convert('/home/SERILOCAL/efi.tsamoura/Downloads/DPL.Release/DPL.Release/EL_release/code_data/data/pubmed_parsed/gene_0_new/0/soft_featureset_1/validation_5.pkl')
    convert('/home/SERILOCAL/efi.tsamoura/Downloads/DPL.Release/DPL.Release/EL_release/code_data/data/pubmed_parsed/gene_0_new/0/soft_featureset_1/validation_anno_full.pkl')
    convert('/home/SERILOCAL/efi.tsamoura/Downloads/DPL.Release/DPL.Release/EL_release/code_data/data/pubmed_parsed/embedding_vec_gene.pkl')
    convert('/home/SERILOCAL/efi.tsamoura/Downloads/DPL.Release/DPL.Release/EL_release/code_data/data/pubmed_parsed/vocab_gene.pkl')
    convert('/home/SERILOCAL/efi.tsamoura/Downloads/DPL.Release/DPL.Release/EL_release/code_data/data/gene_key.pkl')