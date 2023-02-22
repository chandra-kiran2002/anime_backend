import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img



def normalize_data(image):
    return image/255
def modify_cluster(image,clusters,centroids):
    img_shape = clusters.shape
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            temp_distance = []
            for k in centroids:
                temp_distance.append(distance(k,image[i][j]))
            clusters[i][j]=np.argmin(temp_distance)
    return clusters


def modify_centroids(clusters,centroids,image):
    temp_sum = np.full(shape=(len(centroids),3),fill_value=0,dtype='float64')
    temp_count = np.full(shape=len(centroids),fill_value=0)
    for i in range(clusters.shape[0]):
        for j in range(clusters.shape[1]):
            # print(clusters[i][j][0])
            temp_sum[clusters[i][j][0]][0] += image[i][j][0]
            temp_sum[clusters[i][j][0]][1] += image[i][j][1]
            temp_sum[clusters[i][j][0]][2] += image[i][j][2]
            temp_count[clusters[i][j]] +=1

    for i in range(temp_sum.shape[0]):
        if temp_count[i] != 0:
            temp_sum[i][0] /= temp_count[i]
            temp_sum[i][1] /= temp_count[i]
            temp_sum[i][2] /= temp_count[i]
        else:
            temp_sum[i][0] = image[random_valuei(image),random_valuej(image)][0]
            temp_sum[i][1] = image[random_valuei(image),random_valuej(image)][1]
            temp_sum[i][2] = image[random_valuei(image),random_valuej(image)][3]

    return temp_sum

def distance(p,q):
    return np.sqrt(np.sum((p-q)**2))

def random_valuei(image):
    temp = image.shape[0]
    return int(temp*np.random.random())
def random_valuej(image):
    temp = image.shape[1]
    return int(temp*np.random.random())
def create_centroids(k,image):
    x=[]
    for i in range(k):
        x.append(image[random_valuei(image),random_valuej(image)])
    return x

def fun(k,image):
    # print(image.shape)
    clusters = np.full((image.shape[0], image.shape[1], 1), fill_value=-1)
    image = normalize_data(image)
    centroids = create_centroids(k,image)
    # print(centroids)
    for i in range(10):
        clusters = modify_cluster(image,clusters,centroids)
        centroids = modify_centroids(clusters,centroids,image)
        if i!=9:
            clusters = np.full((image.shape[0], image.shape[1], 1), fill_value=-1)
        print(i," ",end="")
    # print()
    for i in range(centroids.shape[0]):
        for j in range(centroids.shape[1]):
            centroids[i][j] = int(centroids[i][j]*255)//1
    centroids = centroids.astype('int64')


    centroids = np.array(centroids)
    # print(centroids)

    for i in range(clusters.shape[0]):
        for j in range(clusters.shape[1]):
            image[i][j] = centroids[clusters[i][j]]
    # image = image.astype('int64')
    # print(image)
    # plt.imshow(image)
    # plt.show()
    return image







