import cv2


def main():

    # to read image for file
    # to read grayscale mode -> cv2.imread(path, 0)
    image = cv2.imread("images/image.jpg")

    # Extracting the height and width of an image
    h, w = image.shape[:2]

    # Displaying the height and width
    print("Height = {},  Width = {}".format(h, w))

    # Extracting RGB values.
    # Here we have randomly chosen a pixel
    # by passing in 100, 100 for height and width.
    (B, G, R) = image[100, 100]

    # Displaying the pixel values
    print("R = {}, G = {}, B = {}".format(R, G, B))

    # We can also pass the channel to extract
    # the value for a specific channel
    B = image[100, 100, 0]
    print("B = {}".format(B))

    # Extracting the Region of Interest (ROI)
    region = image[100: 500, 200: 700]

    # Resize
    resize = cv2.resize(image, (800, 800))

    # Calculating the ratio
    ratio = 800 / w

    # Creating a tuple containing width and height
    dim = (800, int(h * ratio))

    # Resizing the image
    resize_aspect = cv2.resize(image, dim)

    # We are copying the original image,
    # as it is an in-place operation.
    output = image.copy()

    # Parameters
    # Image
    # Top-left corner co-ordinates
    # Bottom-right corner co-ordinates
    # Color (in BGR format)
    # Line width
    rectangle = cv2.rectangle(output, (int(w * 0.2), int(h * 0.2)), (int(w * 0.8), int(h * 0.8)), (255, 255, 255), 2)

    # Parameters
    # Image
    # Top-left corner co-ordinates
    # Bottom-right corner co-ordinates
    # Color (in BGR format)
    # Line width
    # Adding the text using putText() function
    rectangle = cv2.putText(rectangle, 'OpenCV Tutorial', (int(w * 0.2), int(h * 0.15)), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2)

    # to show image with new window
    cv2.imshow("image", image)
    cv2.imshow("region", region)
    cv2.imshow("resize", resize)
    cv2.imshow("resize_aspect", resize_aspect)
    cv2.imshow("rectangle", rectangle)

    cv2.imwrite("filename.jpg", rectangle)

    # To hold the window on screen
    cv2.waitKey(0)

    # It is for removing/deleting created GUI window from screen and memory
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
