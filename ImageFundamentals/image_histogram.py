import cv2
from matplotlib import pyplot as plt

img = cv2.imread("C:/Users/ajape/SOI_DIP/ImageFundamentals/multiple_blocks.png")
print("Number of Pixels in the image: ", img.shape[0] * img.shape[1])

# define a function to compute and plot histogram
def plot_histogram(img, title, mask=None):
   # split the image into blue, green and red channels
   grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   # Set plot params
   plt.title(title)
   plt.xlabel("Bins")
   plt.ylabel("Number of Pixels")

   # Compute Hostpgram
   hist = cv2.calcHist(grey_img, [0], mask, [256], [0, 256])
   plt.plot(hist, color="b")
   plt.xlim([0, 256])
   # plt.ylim([0, grey_img.shape[0] * grey_img.shape[1]])

# compute a histogram for masked image
plot_histogram(img, "Histogram of the Image")

# show the plots
cv2.imshow("Image", img)
cv2.waitKey(0)
plt.show()
