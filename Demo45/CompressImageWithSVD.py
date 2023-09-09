import numpy as np
from PIL import Image
from numpy.linalg import svd
from matplotlib import pyplot as plt
img = Image.open("jojo.jpg")
img.show()

imgary = np.array(img)
imgary = imgary / 255
original_bytes = imgary.nbytes
print(original_bytes)
print(imgary.shape)

img_red = imgary[:,:,0]
img_green = imgary[:,:,1]
img_blue = imgary[:,:,2]
print(img_red.shape)
print(img_green.shape)
print(img_blue.shape)

U_r, S_r, V_r = svd(img_red, full_matrices=True)
U_g, S_g, V_g = svd(img_green, full_matrices=True)
U_b, S_b, V_b = svd(img_blue, full_matrices=True)

k = 50
U_r_k = U_r[:, 0:k]
V_r_k = V_r[0:k, :]
U_g_k = U_g[:, 0:k]
V_g_k = V_g[0:k, :]
U_b_k = U_b[:, 0:k]
V_b_k = V_b[0:k, :]

S_r_k = S_r[0:k]
S_g_k = S_g[0:k]
S_b_k = S_b[0:k]
print(U_r_k.shape)
print(S_r_k.shape)
print(V_r_k.shape)

compressed_bytes = sum([matrix.nbytes for matrix in [U_r_k,V_r_k,U_g_k,V_g_k,U_b_k,V_b_k,S_r_k,S_g_k,S_b_k]])
ratio = compressed_bytes / original_bytes
print(ratio)

image_red_approx = np.dot(U_r_k, np.dot(np.diag(S_r_k), V_r_k))
image_green_approx = np.dot(U_g_k, np.dot(np.diag(S_g_k), V_g_k))
image_blue_approx = np.dot(U_b_k, np.dot(np.diag(S_b_k), V_b_k))
row, col, _ = imgary.shape
img_reconstructed = np.zeros((row, col, 3))
img_reconstructed[:, :, 0] = image_red_approx
img_reconstructed[:, :, 1] = image_green_approx
img_reconstructed[:, :, 2] = image_blue_approx

img_reconstructed[img_reconstructed < 0] = 0
img_reconstructed[img_reconstructed > 1] = 1
print(img_reconstructed.shape)

fig = plt.figure(figsize=(10,5))
a = fig.add_subplot(1,1,1)
imgplot = plt.imshow(img_reconstructed)
plt.show()