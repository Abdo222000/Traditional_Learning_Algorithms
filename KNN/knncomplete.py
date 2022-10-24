# Make Predictions with k-nearest neighbors on the Iris Flowers Dataset
from csv import reader
from math import sqrt
from random import randrange

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
		print('[%s] => %d' % (value, i))
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for _ in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores

# kNN Algorithm
def k_nearest_neighbors(train, test, num_neighbors):
	predictions = list()
	for row in test:
		output = predict_classification(train, row, num_neighbors)
		predictions.append(output)
	return(predictions)



chosen_dataset = input("choose dataset \n 1- iris \n 2- diabetes \n")
match chosen_dataset:
    case "0" : 
        print("iris")
        filename = 'iris_without_id.csv'
        dataset = load_csv(filename)
        for i in range(len(dataset[0])-1):
            str_column_to_float(dataset, i)
        # convert class column to integers
        str_column_to_int(dataset, len(dataset[0])-1)
        # define model parameter
        num_neighbors = 5
        # define a new record
        #row = [5.3,1,2.1,1.6]
        # creating an empty list
        lst = []
        # iterating till the range
        for i in range(0, len(dataset[0])-1):
            if(i==0):print("Enter sepallength")
            if(i==1):print("Enter sepalwidth")
            if(i==2):print("Enter petallength")
            if(i==3):print("Enter petalwidth")
            lst.append(float(input())) # adding the element	
        print(lst)

    case "1" : 
        print("diabetes")
        # Make a prediction with KNN on diabetes Dataset
        filename = 'diabetes.csv'
        dataset = load_csv(filename)
        for i in range(len(dataset[0])-1):
        	str_column_to_float(dataset, i)
        # convert class column to integers
        str_column_to_int(dataset, len(dataset[0])-1)
        # define model parameter
        num_neighbors = 5
        # define a new record
        lst = []
        # iterating till the range
        for i in range(0, len(dataset[0])-1):
            if(i==0):print("Enter sepallength")
            if(i==1):print("Enter sepalwidth")
            if(i==2):print("Enter petallength")
            if(i==3):print("Enter petalwidth")
            lst.append(float(input())) # adding the element	
        print(lst)

    case _ : 
        print("Wrong Dataset \n Exiting")
        exit()




# Make a prediction with KNN on Iris Dataset
filename = 'diabetes.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
# define model parameter
num_neighbors = 5
# define a new record
row = [400,512,32000,64,16,32,320]


filename = 'iris_without_id.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
# define model parameter
num_neighbors = 5
# define a new record
#row = [5.3,1,2.1,1.6]
# creating an empty list
lst = []
# iterating till the range
for i in range(0, len(dataset[0])-1):
    if(i==0):print("Enter sepallength")
    if(i==1):print("Enter sepalwidth")
    if(i==2):print("Enter petallength")
    if(i==3):print("Enter petalwidth")
    lst.append(float(input())) # adding the element	
print(lst)

# predict the label
label = predict_classification(dataset, lst, num_neighbors)
print('Data=%s, Predicted: %s' % (lst, label))
n_folds = 5
scores = evaluate_algorithm(dataset, k_nearest_neighbors, n_folds, num_neighbors)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))