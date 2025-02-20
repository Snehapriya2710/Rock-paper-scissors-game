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
   - Win or lose screen when a player reaches n [i.e.,2] points.  

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
**Sample Output**
![image](https://github.com/user-attachments/assets/63c19dff-6730-443c-a6e4-408128db4d46)


![image](https://github.com/user-attachments/assets/c5299aca-d591-4b2a-9149-b2a44def7446)


![image](https://github.com/user-attachments/assets/09e4ba06-b266-4748-b7c4-7ebb17d882f6)


