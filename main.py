import numpy as np
import matplotlib.pyplot as plt
import copy

x = np.array([12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72])
y = np.array([39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24])

k = 3
# centroids[i] = [x, y]
centroids = {
    i: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}
    
fig = plt.figure(figsize=(5, 5))
plt.scatter(x, y, color='k')
colmap = {0: 'r', 1: 'g', 2: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

def calcular(x,y, centroids):
    d = dict()
    
    for i in centroids.keys():
        # sqrt((x1 - x2)^2 - (y1 - y2)^2)
        d[i] = ( np.sqrt(
            (x - centroids[i][0]) ** 2 + (y - centroids[i][1]) ** 2
            )
        )

    aux = list()
    for key in d.keys():
        aux.append(d[key])
      
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    d['closest'] = np.argmin(aux, axis=0)
    
    d['color'] = [colmap[x] for x in d['closest']]
    return d

df = calcular(x, y, centroids)

fig = plt.figure(figsize=(5, 5))
plt.scatter(x, y, color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

old_centroids = copy.deepcopy(centroids)

def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(x[np.where(df['closest']==i)])
        centroids[i][1] = np.mean(y[np.where(df['closest']==i)])
    return k

centroids = update(centroids)

fig = plt.figure(figsize=(5, 5))
ax = plt.axes()
plt.scatter(x, y, color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
for i in old_centroids.keys():
    old_x = old_centroids[i][0]
    old_y = old_centroids[i][1]
    dx = (centroids[i][0] - old_centroids[i][0]) * 0.75
    dy = (centroids[i][1] - old_centroids[i][1]) * 0.75
    ax.arrow(old_x, old_y, dx, dy, head_width=2, head_length=3, fc=colmap[i], ec=colmap[i])
plt.show()


df = calcular(x, y, centroids)

# Plot results
fig = plt.figure(figsize=(5, 5))
plt.scatter(x, y, color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

# Continue until all assigned categories don't change any more
while True:
    closest_centroids = copy.deepcopy(df['closest'])
    centroids = update(centroids)
    df = calcular(x, y, centroids)
    if (closest_centroids == df['closest']).all():
        break

fig = plt.figure(figsize=(5, 5))
fig.suptitle('Cluster final', fontsize=16)
plt.scatter(x, y, color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()
