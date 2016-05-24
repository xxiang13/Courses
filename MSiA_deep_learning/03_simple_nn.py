# -*- coding: utf-8 -*-
"""
Created on Sat May  7

@author: Xiang Li
"""

import keras.datasets.mnist, numpy as np, time
from numpy.random import rand
tm = time.time()

#%% Load data
losses, accuracies = [], []
(X, Y), (_, _) = keras.datasets.mnist.load_data()
X = X.reshape((len(X), -1)).T / 255.0 # normalize colors
# created Target using size of actual results value Y
# Target holds 10 output nueros, with length(Y) samples
T = np.zeros((len(Y), 10), dtype='uint8').T 
for i in range(len(Y)):
	T[Y[i], i] = 1   
 # create a binary result array of each sample, 
 # like if result = 5, array[5] = 1 => array = [0,0,0,0,1,0,0,0,0]

#%% Setup
# 784 -> 256 -> 128 -> 10
X = X                   # 784 x 60000
T = T.astype('float64') # 10 x 60000

W1 = 2*rand(784, 256).T - 1
W2 = 2*rand(256, 128).T - 1
W3 = 2*rand(128,  10).T - 1

lr = 1e-5
def sigmoid(x): 
    return 1.0/(1.0 + np.e**-x)
    
for i in range(2): # Increase this number for better accuracy
	# Forward pass
	L1 = sigmoid(W1.dot(X))
	L2 = sigmoid(W2.dot(L1))
	L3 = sigmoid(W3.dot(L2))

	# Backward pass (gradient of weights)
	dW3 = (L3 - T) * L3*(1 - L3)
	dW2 = W3.T.dot(dW3)*(L2*(1-L2))
	dW1 = W2.T.dot(dW2)*(L1*(1-L1))

	# Update
	W3 -= lr*np.dot(dW3, L2.T)
	W2 -= lr*np.dot(dW2, L1.T)
	W1 -= lr*np.dot(dW1, X.T)

	loss = np.sum((L3 - T)**2)/len(T.T) # len(T.T) = num of samples
	print("[%04d] MSE Loss: %0.6f LogLoss: %0.6f" % (i, loss, np.log(loss)))

	#%% Additional monitoring code - DO NOT EDIT THIS PART
	import random, matplotlib.pyplot as plt, psutil
	# Throttle code - DO NOT REMOVE THIS. Prevents system crashes.
	if psutil.virtual_memory().percent > 95 or psutil.cpu_times_percent().idle < 5:
		time.sleep(1)
	losses.append(loss)	
	
     # randomly chose 1 case from 60,000 images from training set
	testi = random.choice(range(60000))
	test  = X.T[testi]
	plt.imshow(test.reshape(28,28), cmap='gray')
	plt.show() # true result
 
	cls = np.argmax(L3.T[testi]) # get corresponding prediction (largest probability) of training set
	print("Prediction: %d confidence=%0.2f" % (cls, L3.T[testi][cls]/np.sum(L3.T[testi])))
 
 
	if i % 10 == 9:
		predictions = np.zeros(L3.shape)
  
		for j, m in enumerate(np.argmax(L3.T, axis=1)): #get corresponding predictions for 60,000 images
			predictions[m,j] = 1
   
		acc = np.sum(predictions*T) # get accuracy of each cases = probability of target * 1
		accpct = 100*acc/X.shape[1]
		accuracies.append(accpct)
  
		print("    Speed: %0.2f s/pass" % ((time.time() - tm)/(i+0.01)))
		print("    Accuracy: %d/%d, %0.3f%%" % (acc, X.shape[1], accpct))	
		print("    L1: (Avg=%0.2f, Std=%0.2f, Max=%0.2f) L2: (Avg=%0.2f, Std=%0.2f, Max=%0.2f) L3: (Avg=%0.2f, Std=%0.2f, Max=%0.2f)" % (L1.mean(), L1.std(), L1.max(), L2.mean(), L2.std(), L2.max(), L3.mean(), L3.std(), L3.max()))
		print("    W1: (Avg=%0.2f, Std=%0.2f, Max=%0.2f) W2: (Avg=%0.2f, Std=%0.2f, Max=%0.2f W3: (Avg=%0.2f, Std=%0.2f, Max=%0.2f)" % (W1.mean(), W1.std(), W1.max(), W2.mean(), W2.std(), W2.max(), W3.mean(), W3.std(), W3.max()))
		print("    dW1: (Avg=%0.2f, Std=%0.2f, Max=%0.2f) dW2: (Avg=%0.2f, Std=%0.2f, Max=%0.2f dW3: (Avg=%0.2f, Std=%0.2f, Max=%0.2f)" % (dW1.mean(), dW1.std(), dW1.max(), dW2.mean(), dW2.std(), dW2.max(), dW3.mean(), dW3.std(), dW3.max()))
		
		plt.plot(np.log(losses), color='blue')
		plt.title("Log loss")
		plt.show()
		plt.plot(accuracies, color='blue')
		plt.title("Accuracy")
		plt.show()
  
		import json		
		with open("results-%d.json" % tm, "w") as f:
			f.write(json.dumps({'losses': losses, 'accuracies': accuracies}, indent=1))