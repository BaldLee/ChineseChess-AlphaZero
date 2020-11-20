import os
import json
from Keras import Model
import tensorflow as tf

from logging import getLogger
logger = getLogger(__name__)

def load(self, config_path, weight_path):
        if os.path.exists(config_path) and os.path.exists(weight_path):
            logger.debug(f"loading model from {config_path}")
            with open(config_path, "rt") as f:
                self.model = Model.from_config(json.load(f))
            self.model.load_weights(weight_path)
            logger.debug(f"loaded model digest = {self.digest}")
            return True
        else:
            logger.debug(f"model files does not exist at {config_path} and {weight_path}")
            return False

s = None

load(s,"../data/model/model_best_config.json","../data/model/model_best_weight.h5")
