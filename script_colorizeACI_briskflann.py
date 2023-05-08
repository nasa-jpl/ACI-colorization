# ACI Colorization
# S. Sharma / Updated March 6, 2023
# Aim: This script uses the SHERLOC ACI and WATSON images to produce colorized ACIs. 

# The basic steps it follows are:
#   1. Import images (one aci, one watson)
#   2. Convert both to grayscale
#   3. Detect keypoints that match across the two images by using BRISK, a binary descriptor using Hamming distance
#   4. Use the Flann Based Matcher that uses nearest search methods to find the best matches
#   5. If a minimum number of matches is found, an overlay is created. Color is provided by moving into HSV space. 

# TO RUN THIS, put this into terminal while you're in the correct folder: python script_colorizeACI_briskflann.py --aci aci.png --watson watson.png 

import argparse
import cv2
import numpy as np


def colorize_ACI(watson, aci):
    watson_color = watson.copy()
    watson = cv2.cvtColor(watson, cv2.COLOR_BGR2GRAY)
    aci = cv2.cvtColor(aci, cv2.COLOR_BGR2GRAY)

    MIN_MATCHES = 30

    detector = cv2.BRISK_create()
    kp1, des1 = detector.detectAndCompute(watson, None)
    kp2, des2 = detector.detectAndCompute(aci, None)
    kp1_img = cv2.drawKeypoints(watson, kp1, None, color=(255,255,0))
    kp2_img = cv2.drawKeypoints(aci, kp2, None, color=(255,255,0))

    cv2.imshow('watson', kp1_img)
    cv2.waitKey()

    cv2.imshow('aci', kp2_img)
    cv2.waitKey()

    index_params = dict(algorithm=6,
                        table_number=6,
                        key_size=12,
                        multi_probe_level=2)
    search_params = {}
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    print('Number of Matches:')
    print(len(good_matches))

    if len(good_matches) > MIN_MATCHES:
        print('I found a match')
        src_points = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_points = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        m, mask = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)
        corrected_img = cv2.warpPerspective(watson_color, m, (aci.shape[1], aci.shape[0]))
        corrected_img = cv2.cvtColor(corrected_img, cv2.COLOR_BGR2HSV)
        corrected_img[:,:,2] = aci.astype(np.uint8)
        corrected_img = cv2.cvtColor(corrected_img, cv2.COLOR_HSV2BGR)
        return corrected_img
    return aci


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--aci", default='aci.png', help="path for the ACI image")
    parser.add_argument("--watson", default='watson.png', help="path for the WATSON image")
    args = parser.parse_args()

    im1 = cv2.imread(args.aci)
    im2 = cv2.imread(args.watson)

    img = colorize_ACI(im2, im1)
    cv2.imwrite('colorized_aci.png', img)
    cv2.imshow('Colorized ACI', img)
    cv2.waitKey()
