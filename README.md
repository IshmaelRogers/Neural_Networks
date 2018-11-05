# Neural_Networks

#Nodes layers and edges 

Given some data the neural network draws a line that best seperates the points. 

Look like neurons in the brain

Calculates some equation on some input and calculates whether or not to output 1 or 0

### Classification problems

student 1
Test 9/10
Grades: 8/10 Y 

student 2
Test 3/10
grades 4/10 N

student 3 
Test: 7/10
Grades: 6/10 ? 

Plot (x,y) x = test y = grades

Look at previous data to make a prediction about new data. 

Question? How to find the line that seperates the data

## Linear boundaries

w1x1 + w2x2 + b = 0
Wx + b = 0 
W = (w1, w2)
x = (x1, x2)
y = label (either 1 or 0)

Prediction 

y_hat = { 1 if Wx+b >= 0; over the line
        { 0 if Wx+b <= 0: under the line
        
Goal: y_hat needs to ressemble y as close as possible 


### Perceptrons 

Are the building blocks of neural networks. They allow the computer to convert the boundary equation into a useful graph.
We must create a node that consists of data and the boundary line that seperates them. Next, we create input nodes that allow the perceptron to recieve new data, plot the points and check if the points lie in the positve region of the boundary line. 

![What is this](perceptron.png)

The score is the way that define our criteria for selection. For example:

Consider a case in cyber security monitoring where we have designed a system that checks for one particular anamoly. In this case, our system checks for two criteria. The amount of requests the firewall is taking (n_firewall_Requests) and the performance of the system (sys_health) . A linear equation is created in order to assigned each anomoly a score. 
        Score = 3 * sys_health + 2 * grades - 9
        ## Prediction:
        Score >= 0 Threat
        Score >= 0 Non-threat 
        
Step function 

returns 1 i
        

### Logical operators 

AND - follow stardard "and" logic 
OR 
XOR 

In order to implement perceptrons as logical operators, take the desired truth table (AND, OR, XOR, etc.) use the perceptrons to plot the the data and seperate the positive from the negative region. 

### TODO find the weights and bias to create the perceptrons as logical operators. 

There are two ways to go from an AND perceptron to an OR perceptron 

1. Increase the weight 
2. Decrease the magnitude of the bias 


### The perceptron Trick 

Logical operators (using perceptrons) should not be built by the human operator. Instead they should build themselves given some results. 

The following defines the base line for the perceptron algorithm. 

Given some data a perceptron will find a line and then pick a random linear equation. Next the perceptron will look at how bad the line is doing and move the line around until it gets better. To do this we need "ask" the points to move the line, either closer or farther, in order to correctly classify them correctly.


## Make a line move closer to a point 

Given some linear equation we define a line: 

nx1 + mx2 - b = 0

Plot the bounday line to get a positive and negative region 

We generalize to a misclassified point 

(x,y)

Let's discuss a way to make the bounday line come closer to the points. 

We use a learning rate to allow the line to make small steps towards the point without moving too drastically and potenitally misclassifying other points. 

Multiply learning rate Lr to the misclassified point's coordinates and then perform an operation depending on where the point resides using our equation of a line to give us a new line. 

## The point is misclassifed in the posive region (i.e the point belongs in the negative region) 

We subtract
   n       m     -b
-  x(Lr) y(Lr) 1(Lr)
____________________

New line 
(n-x(Lr))X1 + (m-y(Lr))X2 + (-b - 1(Lr))= 0 

## The pointt is misclassified in the negative region (i.e the point belongs in the positive region)

We add

   n       m     -b
+  x(Lr) y(Lr) 1(Lr)
____________________

New Line 
(n + x(Lr))X1 + (m + y(Lr))X2 + (-b + 1(Lr))= 0 

Psuedocode: Repeat the following algorithm until we get no errors or we reach a disired number of iterations

1. Start with some random weights and bias W1...Wn, b
2. for every misclassified point (x1,...,xn)
        if the prediction = 0:
                for i= 1...n
                        change weight Wi + Lr(xi)
                        change bias b = Lr
        if the prediction = 1:
                for i= 1...n
                        change weight  Wi - Lr(xi)
                        change basis  b + Lr
                        
  
                        

### Introduction



Neural networks have the ability to allow machines to learn almost in a simliar way as humans. They can be used to perform powerful tasks such as self driving cars, 
