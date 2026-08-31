# Import the libraries 
from random import randint 
from sklearn.linear_model import LinearRegression 

TRAIN_SET_LIMIT = 1000 
TRAIN_SET_COUNT = 100 

TRAIN_INPUT = list() 
TRAIN_OUTPUT= list() 
#Create and append a randomly generated data set to the input and output 
for i in range(TRAIN_SET_COUNT): 
 a = randint(0, TRAIN_SET_LIMIT) 
b = randint(0, TRAIN_SET_LIMIT) 
c = randint(0, TRAIN_SET_LIMIT) 
d = randint(0, TRAIN_SET_LIMIT)

op = (7*a) + (3*b) + (4*c) + (9*d) 
TRAIN_INPUT.append([a,b,c,d]) 
TRAIN_OUTPUT.append(op) 
# Step 2: Create model
model = LinearRegression()
# Step 3: Train model
model.fit(TRAIN_INPUT, TRAIN_OUTPUT)
# Step 4: Give new input
prediction = model.predict([[10, 11, 12, 13]])

# Step 5: Display prediction
print("Prediction:", prediction)