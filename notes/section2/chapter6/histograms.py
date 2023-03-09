import cv2
import numpy as np
from matplotlib import pyplot as plt

def build_sample_image():
    tones = np.arange(start=60, stop=240, step=30)
    result = np.ones((50, 50, 3), dtype='uint8') * 30
    for tone in tones:
        img = np.ones((50, 50, 3), dtype='uint8') * tone
        result = np.concatenate((result, img), axis=1)
    return result

def build_sample_image2():
    return np.fliplr(build_sample_image())


def main():
    img1 = build_sample_image()
    cv2.imshow('sample 1',img1)
    cv2.waitKey()
    cv2.destroyAllWindows()
    img2 = build_sample_image2()
    cv2.imshow('sample 2',img2)
    cv2.waitKey()
    cv2.destroyAllWindows()


    # histograms on grayscale images
    # opencv uses the cv2.calcHist() to calculate the histogram
    # can be used in single channel images or multi chanel
    # the signature is cv2.calcHist(images, channels, mask, histSize, ranges, hist, accumulate)
    # images is the source of the image provided as a list [image]
    # channels represents the index of the channel for which we want to calculate [0](gray scale)
    #   [0], [1], [2], multichanel color systems
    # mask when we want to calculate the histogram of a specific region defined by the mask
    #   the default is none, meaning we want to calculate the whole image
    # histsize represents the number of beans provided as a list. [256] for example (y axis)
    # ranges represents the range of intensity values, for example, [0, 256] (x axis)

    # grayscale histograms without a mask
    image = build_sample_image2()
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    plt.plot(hist)
    plt.show()

    image = cv2.imread('./images/witcher.jpeg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    cv2.imshow('image',image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    plt.plot(hist)
    plt.show()


    # gray scale histograms with a mask
    # we need to create an array with the same dimentions as the image
    # the 255 pixels (white) in the array is where we want the histogram to be calculated
    # the black pixels will be ignored
    mask = np.zeros(image.shape, dtype='uint8')
    mask[30:190, 30:190] = 255
    hist_mask = cv2.calcHist([image], [0], mask, [256], [0, 256])
    plt.plot(hist)
    plt.show()

    # color histograms
    # we need to calculate one histogram for each channel
    img = cv2.imread('./images/witcher.jpeg')
    histblue = cv2.calcHist([img], [0], None, [256], [0, 256])
    histgreen = cv2.calcHist([img], [1], None, [256], [0, 256])
    histred = cv2.calcHist([img], [2], None, [256], [0, 256])

    cv2.imshow('witchaaa', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    plt.plot(histblue, color='b')
    plt.plot(histgreen, color='g')
    plt.plot(histred, color='r')
    plt.show()

    # color histograms with masks follow the same logic
    

    # histograms can be compared to check how alike images are in color
    # since we dont have the positions of the pixels on the histogram
    # a common aproach is to divide the image into several blocks
    # of pixels and compare these, than make an average
    # there are 4 available metrics to compare histograms
    # correl, chisqr, intersect, bhattacharyya -> all available in cv2
    # the function to compare is cv2.compareHist(H1, H2, method)


if __name__ == '__main__':
    main()