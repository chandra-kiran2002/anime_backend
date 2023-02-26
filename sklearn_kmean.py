from sklearn.cluster import KMeans
import numpy

def change_image(k,image):
    shape = image.size
    image = image.reshape(shape[0] * shape[1], 3)
    # print("--------------------------------------")
    # print(image)
    km = KMeans(
        n_clusters=5, init='random'
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
    for i in range(shape[1]):
        ans.append([])
        for j in range(shape[0]):
            ans[i].append(km.cluster_centers_[y_km[cnt]])
            cnt += 1
    ans = numpy.array(ans)
    ans = ans.astype('int64')

    print(ans.shape)

    return image
