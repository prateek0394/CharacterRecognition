Character Recogntion from Natural Scenic Images
==========================================

Images of characters extracted from natural images containing additional colour information and noise. This images need to be recognized and classified accordingly. Used a pipeline of image processing and machine learning algorithms to obtain appreciable accuracy. The pipeline includes:
  * binarization using Otsus Thresholding followed by Morphological opening and median filter for removing salt and pepper noise.
  * Feature extraction using Histogram of Oriented Gradients to address variation in character size and orientation.
  * Extra-Tree Classifier for classification

---------------------------------------------------------------------------------

The whole pipeline is coded into Matlab and Python.The image Processing part is carried out in Matlab. Extra-Tree classifier coded in python.(Scikit Library of Python).

----------------------------------------------------------------------------------
