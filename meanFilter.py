from skimage import io, img_as_ubyte
import numpy as np


def filter(image_src, image_save=None):
    img = io.imread(image_src)
    row, col, _ = img.shape

    new_r = img[:, :, 0]
    new_g = img[:, :, 1]
    new_b = img[:, :, 2]

    r = new_r.astype(np.uint16)
    g = new_g.astype(np.uint16)
    b = new_b.astype(np.uint16)

    for i in range(1, row-1):
        for j in range(1, col-1):
            new_r[i, j] = int((r[i - 1, j - 1] + r[i - 1, j] + r[i - 1, j + 1] +
                               r[i, j - 1] + r[i, j] + r[i, j + 1] + r[i + 1, j - 1] +
                               r[i + 1, j] + r[i + 1, j + 1]) / 9)
            new_g[i, j] = int((g[i - 1, j - 1] + g[i - 1, j] + g[i - 1, j + 1] +
                               g[i, j - 1] + g[i, j] + g[i, j + 1] + g[i + 1, j - 1] +
                               g[i + 1, j] + g[i + 1, j + 1]) / 9)
            new_b[i, j] = int((b[i - 1, j - 1] + b[i - 1, j] + b[i - 1, j + 1] +
                               b[i, j - 1] + b[i, j] + b[i, j + 1] + b[i + 1, j - 1] +
                               b[i + 1, j] + b[i + 1, j + 1]) / 9)

    img[:, :, 0] = new_r
    img[:, :, 1] = new_g
    img[:, :, 2] = new_b
    if image_save:
        io.imsave(image_save, img)


if __name__ == "__main__":
    filter('1.png', '2.png')
