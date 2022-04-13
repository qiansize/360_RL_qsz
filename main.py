import argparse
import json
import math
import sys
import string
import os
import numpy as np
from importlib.machinery import SourceFileLoader
from collections import namedtuple

import headset
import navigation_graph as ng
from sabre360 import Session
from sabre360 import set_config

if __name__ == '__main__':
    config=set_config()
    session = Session(config)
    session.run()