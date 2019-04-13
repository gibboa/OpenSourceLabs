from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import PIL.ImageOps  

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
'''
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()     
'''
train_images = train_images / 255.0

test_images = test_images / 255.0

im1 = Image.open("pants1.jpg")
im2 = Image.open("tshirt1.jpg")
im3 = Image.open("boot1.jpg")

im1 = im1.resize((28,28))
im2 = im2.resize((28,28))
im3 = im3.resize((28,28))

im1 = im1.convert("L")
im2 = im2.convert("L")
im3 = im3.convert("L")

im1.save("pants_converted2.png")
im2.save("shirt_converted2.png")
im3.save("boot_converted2.png")

im1 = PIL.ImageOps.invert(im1)
im2 = PIL.ImageOps.invert(im2)
im3 = PIL.ImageOps.invert(im3)

#im1 = im1 / 255.0
#im2 = im2 / 255.0
#im3 = im3 / 255.0

im1.save("pants_converted.png")
im2.save("shirt_converted.png")
im3.save("boot_converted.png")

test_images3 = [im1, im2, im3]

np_im1 = np.array(im1)
np_im2 = np.array(im2)
np_im3 = np.array(im3)

#
np_im1 = np_im1 / 255.0
np_im2 = np_im2 / 255.0
np_im3 = np_im3 / 255.0

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(np_im1.shape)
print("this maybe?")
#print(test_images3)
#print(np_im1)
#cp3_images = [np_im3, np_im3, np_im1]
test_images2 = np.array([np_im1, np_im2, np_im3])
print(test_images2.shape)

#print("here goes", test_images.shape)
'''
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()         
'''

plt.figure()
plt.imshow(test_images2[0])
plt.colorbar()
plt.grid(False)
plt.show()

plt.figure()
plt.imshow(test_images2[1])
plt.colorbar()
plt.grid(False)
plt.show()   

plt.figure()
plt.imshow(test_images2[2])
plt.colorbar()
plt.grid(False)
plt.show()        

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

predictions = model.predict(test_images2)

#print("what does my image look like?")
#print(test_images2[0])
#print("OH....................")

print(predictions[0])
print("the pick is", class_names[np.argmax(predictions[0])])
print(predictions[1])
print("the pick is", class_names[np.argmax(predictions[1])])
print(predictions[2])
print("the pick is", class_names[np.argmax(predictions[2])])
#start main here for part 3?
def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  
  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'
  
  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1]) 
  predicted_label = np.argmax(predictions_array)
 
  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')
'''
  # Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i+9000, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i+9000, predictions, test_labels)
plt.show()
'''
'''
im1 = Image.open("pants1.jpg")
im2 = Image.open("tshirt1.jpg")
im3 = Image.open("boot1.jpg")

im1 = im1.resize((25,25))
im2 = im2.resize((25,25))
im3 = im3.resize((25,25))

im1 = im1.convert("L")
im2 = im2.convert("L")
im3 = im3.convert("L")

im1.save("pants_converted.png")
im2.save("shirt_converted.png")
im3.save("boot_converted.png")

np_im1 = np.array(im1)
np_im2 = np.array(im2)
np_im3 = np.array(im3)

np_im1 = np_im1 / 255
np_im2 = np_im2 / 255
np_im3 = np_im3 / 255

#print(np_im1)
cp3_images = [np_im3, np_im2, np_im1]
'''
  # Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red
num_rows = 3
num_cols = 1
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions, test_labels, test_images3)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions, test_labels)
plt.show()