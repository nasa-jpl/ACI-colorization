![socialpreview](https://user-images.githubusercontent.com/131310922/236954633-fe29158a-050f-4664-8f56-f5aa2cb5ebd5.png)



# ACI-colorization
SHERLOC ACI Colorization using Co-registered WATSON Images

ACI_colorization is a script that allows for "colorizing" autofocus context imager (ACI) images from SHERLOC, an instrument on the Mars 2020 Perseverance Rover. The colorization process essentially finds and matches keypoints between the ACI (grayscale) image and the WATSON (color) image of the same target and blends the colors, providing a kind of "merge" product. This is useful because ACI images are co-boresighted with the SHERLOC spectrometer and are the highest resolution, thus providing both spectral mapping and textural information. By contrast, the WATSON images are color images that are taken from different standoff distances and under various illumination conditions, thus providing information about the color of rock targets useful for mineral/rock type identification. The colorized ACI is a composite product that provides both color and texture information, and SHERLOC spectral maps can be overlaid on it for spectral-textural correlation. 

## Folder Contents

Folder contents: Jupyter notebook with example, demo images for notebook (aci.png and watson.png), script. 

## Notes

* This process works best abraded surface images, because more keypoints are found. It does not work well with natural surfaces, but you can modify certain variables (e.g. min_matches) to fiddle around with results. 
* OpenCV uses BGR space; matplotlib uses RGB so a color conversion is required to display images here. 

## References

1. Stefan Leutenegger, Margarita Chli, and Roland Yves Siegwart. Brisk: Binary robust invariant scalable keypoints. In Computer Vision (ICCV), 2011 IEEE International Conference on, pages 2548–2555. IEEE, 2011.
2. https://docs.opencv.org/3.4/ 
3. David G. Lowe. Distinctive Image Features from Scale-Invariant Keypoints. International Journal of Computer Vision, 2004. 
4. Vino Mahendran. Feature detection and matching with OpenCV. Francium Tech Blog, 2020. https://blog.francium.tech/feature-detection-and-matching-with-opencv-5fd2394a590. 

## Support

Questions/comments can be directed to sunanda.sharma@jpl.nasa.gov

## Authors 

Sunanda Sharma

## Acknowledgments 

Ken Edgett, Kyle Uckert
