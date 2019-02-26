import numpy as np
from skimage import io, color, img_as_uint


def OtsuAlgThreshold(img_src):
    '''大津法图像分割

    Arguments:
        img_src {np.array} -- m*n*1
    '''

    histogram = np.zeros(256, dtype=np.int16)
    value = np.zeros(256)

    row, col = img_src.shape

    _cnt = row*col

    for i in range(row):
        for j in range(col):
            histogram[img_src[i, j]] += 1
    
    # histogram = histogram / _cnt
    value = histogram*np.array([i for i in range(256)])

    best_thresold = 0
    max_variance = 0.0  # 类间方差中间值保存
    for threshold in range(256):
        n0 = histogram[:threshold].sum()
        n1 = histogram[threshold:].sum()
        w0 = n0 / _cnt  # 前景像素点数所占比例
        w1 = n1 / _cnt  # 背景像素点数所占比例
        u0 = value[:threshold].sum()  # 前景平均灰度
        u1 = value[threshold:].sum()  # 背景平均灰度

        u = u0 * w0 + u1 * w1  # 整个图像平均灰度

        tmp_var = w0 * np.power((u - u0), 2) + w1 * np.power((u - u1), 2)
 
        if tmp_var > max_variance:
            best_thresold = threshold
            max_variance = tmp_var

    ret_img = np.where(img_src > best_thresold, 255, 0)

    return best_thresold, ret_img
    
if __name__ == "__main__":
    import time
    img = io.imread('1.png')
    t1 = time.time()
    k, ret = OtsuAlgThreshold(img)
    print(time.time() - t1)
    io.imsave('otsu.png', ret)