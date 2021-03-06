from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import glob

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

import data_pipeline
import models


tf.logging.set_verbosity(tf.logging.INFO)


if __name__=="__main__":

  model_name = 'test' # or 'all_cnn'
  batch_size = 256
  n_steps = 5000 # with 40,000 training samples, this is about 30 epochs

  cifar = data_pipeline.Cifar10Input()
  train_input_fn = cifar.input_fn_factory(mode='train', batch_size=batch_size)
  eval_input_fn = cifar.input_fn_factory(mode='validate', batch_size=batch_size)

  with tf.Session() as sess:
  
    classifier = tf.estimator.Estimator(
      model_fn=models.model_fn_closure(model_name),
      model_dir='./tensorboard') 

    train_spec = tf.estimator.TrainSpec(
      input_fn=train_input_fn, 
      max_steps=n_steps,
      hooks=[])

    eval_spec = tf.estimator.EvalSpec(input_fn=eval_input_fn)

    tf.estimator.train_and_evaluate(classifier, train_spec, eval_spec)
      
