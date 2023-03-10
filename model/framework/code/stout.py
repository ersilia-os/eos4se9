# Initializing and importing necessary libararies
import tensorflow as tf
from rdkit import Chem
import os
import pystow
import pickle
import re
from repack import helper
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


# Print tensorflow version
print("Tensorflow version: "+tf.__version__)

# Always select a GPU if available
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# Scale memory growth as needed
gpus = tf.config.experimental.list_physical_devices("GPU")
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

#Modified by Carolina-carcablop
# current file directory
#the models are downloaded in the checkpoint folder,
#so I set the PYSTOM_HOME variable to the path where the models are located.
root = os.path.dirname(os.path.abspath(__file__))
pystow_home = os.path.abspath(os.path.join(root, "..",".."))

os.environ['PYSTOW_HOME']= pystow_home

# checkpoints directory
default_path= pystow.join("checkpoints")


# Load the packed model forward
reloaded_forward = tf.saved_model.load(default_path.as_posix()+"/translator_forward")


def translate_forward(smiles: str) -> str:
    """Takes user input splits them into words and generates tokens.
    Tokens are then passed to the model and the model predicted tokens are retrieved.
    The predicted tokens gets detokenized and the final result is returned in a string format.

    Args:
        smiles (str): user input SMILES in string format.

    Returns:
        result (str): The predicted IUPAC names in string format.
    """

    # Load important pickle files which consists the tokenizers and the maxlength setting
    inp_lang = pickle.load(open(default_path.as_posix()+"/assets/tokenizer_input.pkl", "rb"))
    targ_lang = pickle.load(open(default_path.as_posix()+"/assets/tokenizer_target.pkl", "rb"))
    inp_max_length = pickle.load(open(default_path.as_posix()+"/assets/max_length_inp.pkl", "rb"))
    if len(smiles) == 0:
        return ''
    smiles = smiles.replace('\\/', '/')
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        smiles = Chem.MolToSmiles(mol, kekuleSmiles=True)
        splitted_list = list(smiles)
        tokenized_SMILES = re.sub(r"\s+(?=[a-z])", "", " ".join(map(str, splitted_list)))
        decoded = helper.tokenize_input(tokenized_SMILES, inp_lang, inp_max_length)
        result_predited = reloaded_forward(decoded)
        result = helper.detokenize_output(result_predited, targ_lang)
        return result
    else:
        return "Could not generate IUPAC name from invalid SMILES."
