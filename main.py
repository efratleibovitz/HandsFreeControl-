import cv2
import mediapipe as mp
from camera.hand_service import HandService
from camera.gesture_controller import GestureController
from microphone.voice_service import VoiceService
from microphone.voice_controller import VoiceController

# --- setup ---
hand_service = HandService()
gesture_controller = GestureController()
voice_controller = VoiceController()
voice_service = VoiceService(on_command=voice_controller.handle)

voice_service.start()
cap = cv2.VideoCapture(0)

print("AirCommand is running! Press Q to quit.")

while True:
    success, img = cap.read()
    if not success: break

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    hand = hand_service.process_frame(mp_image)

    if hand:
        gesture, gesture_label, scroll_label = gesture_controller.process(hand)

        color = (0, 0, 255) if gesture == "fist" else (0, 255, 0)
        cv2.putText(img, gesture_label, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
        if scroll_label:
            cv2.putText(img, scroll_label, (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 0), 3)

    cv2.imshow("AirCommand", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
voice_service.stop()
cv2.destroyAllWindows()
