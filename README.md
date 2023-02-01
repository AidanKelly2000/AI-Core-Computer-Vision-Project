# AI-Core-Computer-Vision-Project

This program is used to play rock, paper, scissors using the webcam and it gets a prediction of whether the user was showing rock, paper or scissors with their hand and then decides if they won or not against the computers randomly generated output of rock, paper, scissors. The model was produced using techable machine and the deep learning model is considered to be a computer-vision model which uses tensorflow. 

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

This file labels the classes from 0-3 in order for the code to be easier to understand.

## Milestone 3

For this project there was a new conda environment created, this was done using:

```
create the conda environment with a specified python version by using:
conda create -n computer_vision python=3.8

activate the environment:
conda activate

check your list of conda environments:
conda env list
```

the following dependencies were required for this project:

```
opencv-python, tensorflow, and ipykernel
```

They were installed using pip by running the following command conda install pip. Then, to install the rest of the libraries, run pip install opencv-python etc...



## Milestone 4

Then a file called manual_rps.py was created to understand the theory of rock, paper, scissors. The purpose of this program was to create the game in which the computer plays against the user, this used the random module which would allow the computer to randomly pick between rock, paper or scissors. From there the functions get_computer_choice and get_user_choice were used to output the choices of the user and the computer. From there the get winner function is able to decide who won. For the purpose of the later milestones, a win counter has been added:

```python
import random

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    options = ['rock', 'paper', 'scissors']
    if user_choice in options:
        return user_choice
    else:
        print("Invalid choice, please enter rock, paper, or scissors")
        return get_user_choice()


def get_winner(computer_choice, user_choice):
    user_wins = 0
    computer_wins = 0
    while user_wins < 2 and computer_wins < 2:
        if computer_choice == user_choice:
            print("It's a tie!")
        elif computer_choice == 'rock' and user_choice == 'scissors':
            print("You lost!")
            computer_wins += 1
        elif computer_choice == 'paper' and user_choice == 'rock':
            print("You lost!")
            computer_wins += 1
        elif computer_choice == 'scissors' and user_choice == 'paper':
            print("You lost!")
            computer_wins += 1
        else:
            print("You won!")
            user_wins += 1
        print("Computer wins: {} User wins: {}".format(computer_wins,user_wins))
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
    if computer_wins == 3:
        print("Computer wins: 3")
        print("Computer wins the game!")
    else:
        print("User wins: 3")
        print("You win the game!")

def play():
    get_winner(get_user_choice(), get_computer_choice())

play()
```

The play function is used to play the game, by taking in the arguments: get_user_choice(), get_computer_choice()

## Milestone 5

The last file to create was the camera_rps.py, this file was responsible for using the prediction of the computer and matching it to the webcam input the user gives. 

the output of the model that was downloaded is a list of probabilities for each class. therefore it will pick the class with the highest probability. So, for example, assuming you trained the model in this order: "Rock", "Paper", "Scissors", and "Nothing", if the first element of the list is 0.8, the second element is 0.1, the third element is 0.05, and the fourth element is 0.05, then, the model predicts that the user showed "Rock" to the camera with a confidence of 0.8.

It was important to have the computer run the camera continuosly, this is done by adding in the capture frame code at each time step of the while true loop:

```python
start = time.time()

while user_wins < 3 and computer_wins < 3:

    while True:



        if time.time() - start > 7:

            prediction = get_prediction(resized_frame)
            print (f"the prediction of the user is: {prediction}")
            computer_choice = get_computer_choice()
            user_choice = prediction
            get_winner(user_choice, computer_choice)
            start = time.time()
            break

        elif time.time() - start > 5:

            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            cv2.imshow('frame', frame)
            print("Show 'rock', 'paper' or 'scissors'")

        elif time.time() - start > 2:

            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            cv2.imshow('frame', frame)
            # print(1)

        elif time.time() - start > 1:

            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            cv2.imshow('frame', frame)
            # print(2)

        elif time.time() - start > 0:

            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            cv2.imshow('frame', frame)
            # print(3)
```

this copy pasted code block is used to read in frames, resize them as a numpy array so that the computer can eventually read it as an array of tensors in the DL model.

As there is frames being continuosly read, the program cant use the sleep function in the countdown as this would stop the entire program momentarily. Instead the     time.time() module is used so that the program is constantly running, hence the camera is constantly running. The theory of the win counter from the manual_rps.py is also implemented in the camera_rps.py, so that the user will know if they beat the computer 3 times, or if the computer beat them 3 times.