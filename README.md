# Introduction
The purpose of the following repositories is to provide guidance on tracking mice's behavior, particularly for Novel Object Recognition experiments (NOR experiments). NOR experiments can sometimes be very hard for the human eye to track; this program harnesses the powers of Deep Learning Models and custom code to automatically and more accurately track a rat's inspection of novel objects. 

# Specifications
For the following code to work, here are some specifications:

* It is highly recommended that you record the video from a "top-down view" with ONE ANIMAL PER VIDEO
* Use the same videos for all steps of the process. I highly recommend against using different sets of videos or newly cropped videos. It is very important to ensure the resolutions of the videos stay the same until the very end. 
*  Make sure to modify programs to fit your needs, use the comments to help you
*  Make some amazing discoveries!

# Instructions
## Step 1: DeepLabCut(DLC) Pose-Coordinates
* After trial and error, DLC seems to be the best means for generating pose coordinates for rats. The same process can be used for mice, too

* Use the following link ([](https://github.com/sajivhar4118/Rat-NOR/blob/eb7543edfa4221fd62312f15e0a52ddd2293d5c0/DLC-Documentation.md)) to produce pose coordinates for all animals in your videos successfully.
* For those without access to Northwestern Quest, ask your institution to download the most recent version of DLC. If you are doing it individually, here is the installation guide for DLC on your PC: 
    * If your institution provides services similar to Northwestern's Quest, feel free to do the first half of the process (GUI Heavy) on your PC and run the model on the super-computer.

* Once Pose Coordinates have been produced, move on to the next step

## Step 2: Roboflow for Object Detection
* The purpose of this step is to track the movement of and location of objects in the video (if there are any in the video)
* Use following link ([](https://github.com/sajivhar4118/Rat-NOR/blob/eb7543edfa4221fd62312f15e0a52ddd2293d5c0/Roboflow-Documentation.md)) to access the instructions 
* Again, make sure the same videos used for DLC are used here with the same resolution and fps! The use of different videos will most definitely yield bad results
* Move to the next step once the code snippet is copied

## Step 3: Generating the YoloV9 Model
* YoloV9 has been a very promising program for creating object recognition deep-learning models.
* Use the following link ([](https://github.com/sajivhar4118/Rat-NOR/blob/eb7543edfa4221fd62312f15e0a52ddd2293d5c0/Training_YoloV9_Public_Final.ipynb)) to open up the Google Colab (.ipynb)
* Caution: One .txt file is created for each frame of each video until everything is combined in the last code node, so it is highly recommended that you run the inference code with 6-8 videos at a time 

## Step 4: Final Data Processing
* Use the following link ([](https://github.com/sajivhar4118/Rat-NOR/blob/eb7543edfa4221fd62312f15e0a52ddd2293d5c0/Final_Processing.md)) to work through and create your final dataset with the amount of frames/time your animal has spent observing each object. 
* Tweak parameters as needed
