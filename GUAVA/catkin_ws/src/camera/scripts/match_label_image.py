import os


def main():
    path_label = "/Users/dojinkim/Desktop/YOLO/label/"
    path_image = "/Users/dojinkim/Desktop/YOLO/JPEGImages/"
    dir_label_list = os.listdir(path_label)
    dir_image_list = os.listdir(path_image)

    label = [label[:len(label)-4] for label in sorted(dir_label_list)]

    for image in sorted(dir_image_list):
        # if image[:len(image)-4] in label:
        os.rename(path_image + image, path_image + image[7:])


if __name__ == '__main__':
    main()
