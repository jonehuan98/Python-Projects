# Distance Calculator
def distance(p1, p2):
    return (((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)) ** 0.5

# Mean calculator
def meanvalue(totalValue, totalNum):
    return totalValue / totalNum

# Iteration function that is run for each iteration to determine clusters, distance, and mean
def runIteration(centr1, centr2):
    # Clear cluster and distances list for empty list for each iteration, as clusters lists may update for each iteration
    distances1=[]
    distances2=[]
    cluster1 = []
    cluster2 = []

    for i in range(len(coordinates)):
        c1distance = distance(centr1, coordinates[i])
        c2distance = distance(centr2, coordinates[i])
        distances1.append(c1distance)
        distances2.append(c2distance)

        if c1distance < c2distance:
            cluster1.append(coordinates[i])
        else:
            cluster2.append(coordinates[i])

    xcluster1 = [p[0] for p in cluster1]
    ycluster1 = [p[1] for p in cluster1]
    xcluster2 = [p[0] for p in cluster2]
    ycluster2 = [p[1] for p in cluster2]

    centroid1 = (((meanvalue(sum(xcluster1), len(xcluster1))),
                      (meanvalue(sum(ycluster1), len(ycluster1)))))
    centroid2 = (((meanvalue(sum(xcluster2), len(xcluster2))),
                      (meanvalue(sum(ycluster2), len(ycluster2)))))
    
    print("Distance to c1: ", distances1)
    print("Distance to c2: ", distances2)
    print("Cluster 1: ", cluster1)
    print("Cluster 2: ", cluster2)
    print("Mean 1: ", centroid1)
    print("Mean 2: ", centroid2 ,"\n")
    
    return centroid1, centroid2

#iterationNum can be changed to run as many iterations as desired
iterationNum = 2
coordinates = [(0, 0), (1, 0), (1, 1), (0, 1), (-1, 0)]

#initial centroids
initialc1 = (1, 0)
initialc2 = (1, 1)

#range can be changed to run as many iterations as desired, but in the case of the assignment, 2 iterations
for i in range(iterationNum):
    print("Iteration", i+1, ":")
    if i == 0:
        centroid1, centroid2 = runIteration(initialc1, initialc2)
    else:
        centroid1, centroid2 = runIteration(centroid1, centroid2)