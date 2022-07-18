

# For webcam input:
cap = cv2.VideoCapture("Just_Dance_2019-A_Little_Party_Never_Killed_Nobody_1080.mp4")
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.


    # Consol Log : record point result
    

    results.pose_landmarks
    #f.close()


    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', image)
    
cap.release()





class JustDance(Exception):
    def __init__(self):
        import cv2
        import mediapipe

        self.opencv = cv2
        self.mediapipe = mediapipe

        self.mp_drawing = self.mediapipe.solutions.drawing_utils
        self.mp_drawing_styles = self.mediapipe.solutions.drawing_styles
        self.mp_pose = self.mediapipe.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)
        self.ext = False
        self.thread = False

        #self.video = cv2.VideoCapture("Just_Dance_2019-A_Little_Party_Never_Killed_Nobody_1080.mp4")
        self.cap = cv2.VideoCapture(0)
        self.image = None
        self.success = False
        
        self.data = ""

        pass


    def drawlandmark(self, image, results):
        return self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS, landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style())

    def recordlandmark(self, results):
        landmarks = results.pose_landmarks.landmark
        data.append(landmarks[self.mp_pose.RIGHT_SHOULDER.value])

    def main(self):
        if not self.thread:
            while True:
                if self.opencv.waitKey(5) & 0xFF == 27:
                    self.ext = True
                    break
                self.getcam()
                self.recog()
        else:
            pass
        self.cap.release()
        pass

    def recog(self):
        while True:
            if self.ext: break
            if not self.success: continue
            image = self.image
            image.flags.writeable = False
            image = self.opencv.cvtColor(image, self.opencv.COLOR_BGR2RGB)
            results = pose.process(image)
            image.flags.writeable = True
            image = self.opencv.cvtColor(image, self.opencv.COLOR_RGB2BGR)


    def getcam(self):
        while True:
            if self.ext == True: break
            self.success, self.image = cap.read()