# AI-Core-Computer-Vision-Project

## Milestone 1

The version control used for this project was Github, a remote repo was created and then cloned into a local folder to begin documenting the project.
Github has many useful attributes and is a great place to showcase your completed projects.

## Milestone 2 

The website [Teachable Machine](https://teachablemachine.withgoogle.com) was used to create the model of this project. Each class is trained with images of yourself showing each option to the camera. The "Nothing" class represents the lack of option in the image. There were 4 different class made in the multi-class classification model (rock, paper, scissors, none). The website essentially takes lots of example images which are given via the users webcam, it then creates a computer vision model and trains it using the labels that were provided by the user. In this project, examples of roughly 300 images per class were given to the computer and labelled with respect to either rock, paper, scissors or none.

The files were downloaded from the Tensorflow tab of Teachable-Machine. The model given was a deep learning model that has no readability, and there was a second file called labels.txt:

```
0 Rock
1 Paper
2 Scissors
3 None
```

This file labels the classes 0-3.

