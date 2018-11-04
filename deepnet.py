from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets(".", one_hot=True, reshape=False)



#Learning parameters

learning_rate = 0.001
training_epochs = 20 
batch_size = 128
display_step = 1 

#MNIST data input (img shpae: 28 *28)
n_input = 784 

#MNIST total classes (0-9 digits)
n_classes = 10 

#parameter tuning 

#determines the size of the hidden layer in the neural network. 
#aka the width of a layer 
n_hidden_layer = 256 

#Weights and biases 

#store layers weights and bias 

#hidden for hidden layer 
#out for ouput later 

weight = {'hidden_layer': tf.Variable(tf.random_normal([n_input, n_hidden_layer])), 'out': tf.Variable(tf.random_normal([n_hidden_layer, n_classes]))}
bias   = {'hidden_layer': tf.Variable(tf.random_normal([n_hidden_layer])), 'out': tf.Variable(tf.random_normal([n_classes]))}

#input 

x = tf.placeholder("float", [None, 28, 28, 1]) 
y = tf.placeholder("float", [None, n_classes])


#function above reshapes the 28px by 28px matrices in x into row vectors of 784px

x_flat = tf.reshape(x, [-1, n_input])


#multilayer perceptron 

layer_1 = tf.add(tf.matmul(x_flat, weights['hidden_layer']),\
    biases['hidden_layer'])

layer_1 = tf.nn.relu(layer_1)

#output later witjh linear activation 

logits = tf.add(tf.matmul(layer_1, weights['out']), biases['out'])

#Optimizer 

#Define loss and optimizer 

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=labels)) 
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

# Calculate accuracy
correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))



#Session 

# Initializing the variables

init = tf.gloabal_variables_initializer()

#launch the graph 

with tf.Session() as sess: 
	sess.run(init)
	#Training Cycles 
	for epoch in range(training_epochs):
		total_batch = int(mnist.train.num_examples/batch_size)
		#loop over all batches 
		for i in range (total_batch):
			batch_x, batch_y = mnist.train.next_batch(batch_size)
			#Run optimization op (backprop) and cost op ( to get loss value)

			sess.run(optimizer, feed_dict={x: batch_x, y: batch_y})









\
