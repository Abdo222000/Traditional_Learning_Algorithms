

# # creating an empty list
# lst = []
# # number of elements as input
# n = 4
# # iterating till the range
# for i in range(0, n):
#     if(i==0):print("Enter sepallength")
#     if(i==1):print("Enter sepalwidth")
#     if(i==2):print("Enter petallength")
#     if(i==3):print("Enter petalwidth")
#     lst.append(float(input())) # adding the element	
# print(lst)

from multiprocessing.pool import TERMINATE
from turtle import end_fill, end_poly


print("Hello", "how are you?", sep="---")



label = input("0,1,2?\n")
match label:
    case "0" : print("A")
    case "1" : print("B")
    case _ : print("nothing")


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
        filename = 'diabetes.csv'
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

    case "3" : 
        print("Wrong Dataset \n Exiting")
        exit()

    case _ :   exit()



label = input("0,1,2?\n")
match label:
    case "0" : print("A")
    case "1" : print("B")
    case _ : print("nothing")
