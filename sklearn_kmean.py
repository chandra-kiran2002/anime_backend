from sklearn.cluster import KMeans
import numpy
import matplotlib.pyplot as plt

def change_image(k,image):
    shape = image.shape
    image = image.reshape(shape[0] * shape[1], 3)
    km = KMeans(
        n_clusters=k, init='random'
    )
    y_km = km.fit_predict(image)
    ans = []
    colors = km.cluster_centers_
    for i in range(len(km.cluster_centers_)):
        for j in range(3):
            colors[i][j] = int(colors[i][j])
    colors = colors.astype('int64')
    print(colors)

    cnt = 0
    for i in range(shape[0]):
        ans.append([])
        for j in range(shape[1]):
            ans[i].append(km.cluster_centers_[y_km[cnt]])
            cnt += 1
    ans = numpy.array(ans)
    ans = ans.astype('int64')

    print(ans.shape)
    plt.imshow(ans)
    plt.show()
    return ans
