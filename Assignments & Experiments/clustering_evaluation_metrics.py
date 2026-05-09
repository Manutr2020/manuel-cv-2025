# LDA-T317: Assignment 5.4 -- Template

import numpy as np
from collections import Counter, defaultdict

def purity(reference, clustered):
    """ Measure the purity of clusters, when a set of data points with
        particular reference labels are allocated to specific clusters """

    assert len(reference) == len(clustered), \
        "There must be as many data points in the reference as in the clusters."

    total_points = len(reference)
    cluster_to_labels = defaultdict(list) # defaultdict is a dictionary that automatically creates a default value for a key that does not exist yet.
    # This allows us to append values without checking if the key already exists.

    for ref_label, cluster_label in zip(reference, clustered):
        cluster_to_labels[cluster_label].append(ref_label)

    majority_sum = 0
    for labels in cluster_to_labels.values():
        majority_sum += Counter(labels).most_common(1)[0][1]

    return majority_sum / total_points 


def precision_b_cubed(reference, clustered):
    """ B-CUBED algorithm by Bagga and Baldwin for computing the precision
        between the reference labels of a set of data points
        compared to clusters these points have been allocated to """

    assert len(reference) == len(clustered), \
        "There must be as many data points in the reference as in the clusters."

    n = len(reference)
    precision_sum = 0

    for i in range(n):
        same_cluster = (clustered == clustered[i])
        same_label = (reference == reference[i])

        correct_in_cluster = np.sum(same_cluster & same_label)
        cluster_size = np.sum(same_cluster)
        precision_sum += correct_in_cluster / cluster_size

    return precision_sum / n


def recall_b_cubed(reference, clustered):
    """ B-CUBED algorithm by Bagga and Baldwin for computing the recall
        between the reference labels of a set of data points
        compared to clusters these points have been allocated to """

    assert len(reference) == len(clustered), \
        "There must be as many data points in the reference as in the clusters."

    n = len(reference)
    recall_sum = 0

    for i in range(n):
        same_cluster = (clustered == clustered[i])
        same_label = (reference == reference[i])

        correct_in_cluster = np.sum(same_cluster & same_label)
        label_size = np.sum(same_label)
        recall_sum += correct_in_cluster / label_size

    return recall_sum / n


# TESTS

def test1():
    """ This is the clustering used as an example in the document
        describing how these evaluation measures work """

    reference1 = np.array(["a", "b", "b", "b", "b", "b", "b", "b", "c", "c",
                           "c", "c", "c", "a", "a", "a", "b", "b", "c", "c"])
    clustered1 = np.array([1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
                           2, 2, 2, 3, 3, 3, 3, 4, 4, 4])
    
    print("Test 1: The purity is supposed to be 0.75 and it is",
          purity(reference1, clustered1)) 
    print("Test 1: The precision is supposed to be ~0.632 and it is",
          precision_b_cubed(reference1, clustered1)) 
    print("Test 1: The recall is supposed to be ~0.504 and it is",
          recall_b_cubed(reference1, clustered1)) 
    print()

    
def test2():
    """ This is the same as test1, but the order of the data points
        has changed and also the numbering of the clusters. The results
        should still be the same. """

    reference2 = np.array(['c', 'c', 'c', 'a', 'a', 'c', 'b', 'b', 'b', 'a',
                           'b', 'c', 'a', 'b', 'b', 'c', 'b', 'b', 'b', 'c'])
    clustered2 = np.array([4, 2, 4, 1, 3, 4, 4, 1, 2, 3,
                           1, 2, 3, 1, 4, 4, 1, 3, 1, 4])

    print("Test 2: The purity is supposed to be 0.75 and it is",
          purity(reference2, clustered2)) 
    print("Test 2: The precision is supposed to be ~0.632 and it is",
          precision_b_cubed(reference2, clustered2)) 
    print("Test 2: The recall is supposed to be ~0.504 and it is",
          recall_b_cubed(reference2, clustered2)) 
    print()


def test3():
    """ All data points in their own clusters """

    reference3 = np.array(["dog", "cat", "cat", "mouse", "dog", "mouse",
                           "mouse", "mouse", "rat", "dog", "dog", "dog"])
    clustered3 = np.array([5, 3, 0, 2, 9, 7, 1, 6, 8, 4, 11, 10])

    print("Test 3: The purity is supposed to be 1.0 and it is",
          purity(reference3, clustered3)) 
    print("Test 3: The precision is supposed to be 1.0 and it is",
          precision_b_cubed(reference3, clustered3)) 
    print("Test 3: The recall is supposed to be ~0.333 and it is",
          recall_b_cubed(reference3, clustered3)) 
    print()

    
def test4():
    """ All data points in the same cluster """

    reference4 = np.array(["dog", "cat", "cat", "mouse", "dog", "mouse",
                           "mouse", "mouse", "rat", "dog", "dog", "dog"])
    clustered4 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    print("Test 4: The purity is supposed to be ~0.417 and it is",
          purity(reference4, clustered4)) 
    print("Test 4: The precision is supposed to be ~0.319 and it is",
          precision_b_cubed(reference4, clustered4)) 
    print("Test 4: The recall is supposed to be 1.0 and it is",
          recall_b_cubed(reference4, clustered4)) 
    print()


def main():

    # Run the tests
    test1()
    test2()
    test3()
    test4()

if __name__ == "__main__":
    main()
