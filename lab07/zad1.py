import numpy as np
from matplotlib import pyplot as plt

data = np.zeros((128, 128, 3), dtype=np.uint8)
kernel = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
def convolve(img, kernel):
    new_img = np.zeros((img.shape[0] - kernel.shape[0] + 1, img.shape[1] - kernel.shape[1] + 1, 3), dtype=np.uint8)
    for x in range(new_img.shape[0]):
        for y in range(new_img.shape[1]):
            for z in range(3):
                suma = 0
                for x_k in range(kernel.shape[0]):
                    for y_k in range(kernel.shape[1]):
                        suma += img[x + x_k, y + y_k, z] * kernel[x_k, y_k]
                new_img[x, y, z] = suma
    return new_img



def convolve_stride_2(img, kernel):
    new_img = np.zeros((int((img.shape[0] - kernel.shape[0]) / 2 + 1), int((img.shape[1] - kernel.shape[1]) / 2 + 1), 3), dtype=np.uint8)
    for x in range(new_img.shape[0]):
        for y in range(new_img.shape[1]):
            for z in range(3):
                suma = 0
                for x_k in range(kernel.shape[0]):
                    for y_k in range(kernel.shape[1]):
                        suma += img[x * 2 + x_k, y * 2 + y_k, z] * kernel[x_k, y_k]
                new_img[x, y, z] = suma
            
    return new_img




def draw(img, x, y, color):
    img[x, y] = [color, color, color]


draw(data, 5, 5, 100)
draw(data, 6, 6, 100)
draw(data, 5, 6, 255)
draw(data, 6, 5, 255)


for i in range(128):
    for j in range(128):
        if (i-64)**2 + (j-64)**2 < 900:
            draw(data, i, j, 200)
        elif i > 100 and j > 100:
            draw(data, i, j, 255)
        elif (i-15)**2 + (j-110)**2 < 25:
            draw(data, i, j, 150)
        elif (i-15)**2 + (j-110)**2 == 25 or (i-15)**2 + (j-110)**2 == 26:
            draw(data, i, j, 255)

plt.imshow(data, interpolation='nearest')
plt.show()
plt.imshow(convolve(data, kernel), interpolation='nearest')
plt.show()
plt.imshow(convolve_stride_2(data, kernel), interpolation='nearest')
plt.show()
