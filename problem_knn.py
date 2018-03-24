#!/usr/bin/env python
#coding:utf-8
#####################################################################################
#       1年52組1番　青谷芳宏
#   人工知能特論レポート課題　(kNN法)
#   
#   表示結果 : 
#       k = 1 -----> A
#       k = 2 -----> 近傍の訓練データが同数になるため分類できない
#       k = 3 -----> A
#####################################################################################
import numpy as np

print np.version.full_version

class_list = np.array(['A', 'B'])

def knn(train_data, class_data, test_datai, k):
    distance_list = np.array([])
    for i in range(len(train_data)):
        distance_list = np.append(distance_list, distance(train_data[i], test_data))
    #  print "distance_list : ", distance_list
    
    
    #  print "np.argsort(distance_list) : ", np.argsort(distance_list)
    index = np.argsort(distance_list)
    
    nn_class_list = np.array([])
    for i in xrange(k):
        nn_class_list = np.append(nn_class_list, class_data[index[i]])
    #  print "nn_class_list : ", nn_class_list

    class_num_list = check_class(nn_class_list)
    
    if len(class_num_list) == 1:
        print "The class of test data is ", class_list[int(class_num_list[0])]
    else:
        print "The class of test data cannot be determined."
        print "Candidates --->", 
        for i in range(len(class_num_list)):
            print " ", class_list[i], 
        print ""


def check_class(data):
    count_list = np.zeros(len(class_list))
    for i in range(len(data)):
        for j in range(len(class_list)):
            if data[i] == class_list[j]:
                count_list[j] += 1
    #  print "count_list : ", count_list
    max_count = np.max(count_list)
    class_num_list = np.array([])
    for i in range(len(count_list)):
        if count_list[i] == max_count:
            class_num_list = np.append(class_num_list, i)
    #  print "class_num_list : ", class_num_list
    return class_num_list


def distance(data1, data2):
    u = data1 - data2
    return np.linalg.norm(u)


def main(train_data, test_data):
    pass

if __name__=="__main__":
    train_data = np.array([[1.2, 3.3, 44.5],
                           [2.2, 0.4, 20.9],
                           [1.4, 2.8, 34.3],
                           [3.4, 4.0, 15.9]])
    class_data = np.array(['B', 'B', 'A', 'A'])
    test_data = np.array([2.0, 3.1, 29.9])

    print "k = 1 : "
    knn(train_data, class_data, test_data, 1)
    print "k = 2 : "
    knn(train_data, class_data, test_data, 2)
    print "j = 3 : "
    knn(train_data, class_data, test_data, 3)

