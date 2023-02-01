import random
import time

import cv2
import numpy as np
from keras.models import load_model

choice_list = ["rock", "paper", "scissors", "None"]

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_computer_choice():
    computer_choice = random.choice(choice_list[:3])
    return computer_choice

def get_prediction(resized_frame):

    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    prediction = prediction.argmax(axis = -1)
    return choice_list[int(prediction)]

user_wins = 0
computer_wins = 0

def get_winner(user_choice, computer_choice):

    global user_wins
    global computer_wins

    if user_choice == computer_choice:
        return print(f"Both players selected {user_choice}. It's a tie!")

    elif user_choice == "rock":
        if computer_choice == "scissors":
            user_wins += 1
            return print("Rock smashes scissors! You win!")
        else:
            computer_wins += 1
            return print("Paper covers rock! You lose.")

    elif user_choice == "paper":
        if computer_choice == "rock":
            user_wins += 1
            return print("Paper covers rock! You win!")
        else:
            computer_wins += 1
            return print("Scissors cuts paper! You lose.")

    elif user_choice == "scissors":
        if computer_choice == "paper":
            user_wins += 1
            return print("Scissors cuts paper! You win!")
        else:
            computer_wins += 1
            return print("Rock smashes scissors! You lose.")

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
            # print("Show 'rock', 'paper' or 'scissors'")

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



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if computer_wins == 3:
    print("You lose, the computer won 3 times!")
elif user_wins == 3:
    print("You won 3 times!")
else:
    pass

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()