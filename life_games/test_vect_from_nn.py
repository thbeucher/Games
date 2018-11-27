import numpy as np
import tensorflow as tf
import tensorflow.contrib.eager as tfe


tfe.enable_eager_execution()


def forward(x, layers):
  for layer in layers:
    output = layer(x)
    x = output
  return output


def get_loss(x, y, layers):
  output = forward(x, layers)
  loss = tf.losses.mean_squared_error(y, output)
  return loss


def validation(x, y, layers, dump=False):
  x = tf.convert_to_tensor(x, tf.float32)
  y = np.array(y)
  output = forward(x, layers)
  output = tf.math.round(output)
  loss = tf.losses.mean_squared_error(y, output)
  if dump:
    print('output -> {}\ntarget -> {}'.format(output, y))
  return (False, loss) if loss == 0 else (True, loss)


def launch_train(layers):
  optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
  running = True
  epoch = 0
  while running:
    for i, el in enumerate(x):
      optimizer.minimize(lambda: get_loss(el, target[i], layers))
    running, loss = validation(x, target, layers)
    if epoch % 100 == 0:
      print('epoch {} | loss = {}'.format(epoch, loss))
    if tf.equal(loss, 0.):
      running = False
    epoch += 1


def init_layers():
  pass


def save(to_save, save_path='models/arrow_direction/'):
  saver = tfe.Saver([t for var in self.to_save for t in var.variables])
  saver.save(save_path)


def load(to_load, save_path='models/arrow_direction/'):
  saver = tfe.Saver([t for var in self.to_load for t in var.variables])
  saver.restore(save_path)


if __name__ == '__main__':
  moves = {'right': np.array([0, 5]), 'down': np.array([90, 5]), 'left': np.array([180, 5]), 'up': np.array([270, 5])}

  x = [np.array([[0], [100]]), np.array([[100], [0]]), np.array([[200], [100]]), np.array([[100], [200]])]
  x = [tf.convert_to_tensor(el.reshape((1, 2)), tf.float32) for el in x]
  target = [np.array([[0], [5]]).T, np.array([[90], [5]]).T, np.array([[180], [5]]).T, np.array([[270], [5]]).T]


  learner_layer = tf.layers.Dense(10, activation=tf.nn.relu)
  predicter_layer = tf.layers.Dense(2, activation=None)
  layers = [learner_layer, predicter_layer]

  launch_train(layers)

  validation(x, target, layers, dump=True)
