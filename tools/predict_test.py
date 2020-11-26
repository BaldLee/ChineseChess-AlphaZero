from multiprocessing import Process
from threading import Thread
import os
import json
import hashlib
import numpy as np
from keras.engine.training import Model
import tensorflow as tf
import keras.backend as K


class tmp:
    def __init__(self):
        self.model = None
        self.graph = None

    def load(self, config_path, weight_path):
        if os.path.exists(config_path) and os.path.exists(weight_path):
            print(f"loading model from {config_path}")
            with open(config_path, "rt") as f:
                self.model = Model.from_config(json.load(f))
            self.model.load_weights(weight_path)
            self.graph = tf.get_default_graph()
            print(f"loaded model digest = {self.fetch_digest(weight_path)}")
            return True
        else:
            print(
                f"model files does not exist at {config_path} and {weight_path}")
            return False

    @staticmethod
    def fetch_digest(weight_path):
        if os.path.exists(weight_path):
            m = hashlib.sha256()
            with open(weight_path, "rb") as f:
                m.update(f.read())
            return m.hexdigest()
        return None


def get_path():
    d = os.path.dirname
    project_dir = d(d(os.path.abspath(__file__)))
    data_dir = os.path.join(project_dir, "data")
    model_dir = os.path.join(data_dir, "model")
    config_path = os.path.join(model_dir, "model_best_config.json")
    weight_path = os.path.join(model_dir, "model_best_weight.h5")
    return config_path, weight_path


def worker(config_path, weight_path):
    print("\n\t\t\t\tSTART!!!\n")
    tf.disable_v2_behavior()
    config = tf.ConfigProto(allow_soft_placement=True,
                            gpu_options=tf.GPUOptions(visible_device_list='0'))
    sess = tf.Session(config=config)
    K.set_session(sess)
    s = tmp()
    s.load(config_path, weight_path)
    data = np.zeros(shape=(1, 14, 10, 9), dtype=np.float32)
    with s.graph.as_default():
        p, v = s.model.predict_on_batch(data)
        print(f"p:{p}")
        print(f"v:{v}")
    print("\n\t\t\t\tDONE!!!\n")


config_path, weight_path = get_path()
p1 = Thread(target=worker, args=(config_path, weight_path))
# p2 = Process(target=worker)
p1.start()
# p2.start()
# p1.join()
# p2.join()
# print("done")
# worker()
