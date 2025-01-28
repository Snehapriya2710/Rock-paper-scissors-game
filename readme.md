### **Rock-Paper-Scissors Game with Hand Gesture Recognition**   
This is an interactive Rock-Paper-Scissors game that uses a webcam to detect hand gestures for rock, paper, or scissors using OpenCV and the `cvzone` library.  
**Technologies Used:**  
   - Python  
   - OpenCV  
   - `cvzone` for hand detection  
   - Random module for AI move generation  

**Features:**  
   - Real-time hand gesture recognition using a webcam.  
   - AI opponent with random move generation.  
   - Visual interface with dynamic score tracking.  
   - Win or lose screen when a player reaches 2 points.  

**How to Play:**  
   - Start the game by pressing the `s` key.  
   - Show gestures for:
     - Rock (fist: `[0, 0, 0, 0, 0]`)  
     - Paper (open hand: `[1, 1, 1, 1, 1]`)  
     - Scissors (two fingers: `[0, 1, 1, 0, 0]`)  
   - The game detects your move and determines the winner after 3 seconds.  

**Prerequisites:**  
   Install required libraries using:  
   pip install opencv-python cvzone numpy
 
**How to Run:**  
   - Run the script using:  
     python main.py
   - Press `Esc` to exit.  
