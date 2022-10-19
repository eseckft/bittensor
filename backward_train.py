import argparse
import time
import datetime
import bittensor
import torch
import os
import wandb
import math
import random
import pandas
import traceback
from rich import print
from rich.console import Console
from rich.style import Style
from rich.table import Table
from rich.traceback import install
from typing import List, Tuple, Callable, Dict, Any, Union, Set
import sys
import tracemalloc
from collections import Counter
import linecache

from bittensor.utils.tokenizer_utils import phrase_cross_entropy

from torch.nn.utils import clip_grad_norm_
from torch.nn import TransformerEncoder, TransformerEncoderLayer
from loguru import logger
from threading import Lock

import pdb

bittensor.logging(debug = True)
wallet = bittensor.wallet()
subtensor = bittensor.subtensor(network = 'nobunaga')
meta = bittensor.metagraph(subtensor = subtensor)
meta.sync()
dend = bittensor.dendrite(wallet = wallet)
config = bittensor._neuron.text.core_validator.neuron.config()
config.nucleus.topk = 100
config.dataset.dataset_name = ['Books3']
config.dataset.num_batches = 100
config.neuron.validation_synapse = 'TextCausalLM'
config.nucleus.dendrite_backward = True
dataset = bittensor.dataset(config = config)
nucleus = bittensor._neuron.text.core_validator.nucleus(config = config, device = 'cpu', subtensor = subtensor )
next(dataset)

count = 0 
random_uids = torch.tensor(list(range(100)))
random_endpoints = [meta.endpoints[46]]
synapse = bittensor.synapse.TextCausalLMNext()

while True:
    _, stats = nucleus.forward(next(dataset) , meta, dend)
    pdb.set_trace()

dataset.close()
del dend