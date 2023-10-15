from config import auth_token, config_url
import requests
import json
import cv2

def get_config():

    # URL and headers
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    # Send the POST request
    response = requests.get(config_url, headers=headers)
    response_json = json.loads(response.text)
    return response_json

def parse_image(response, image):
    worker_url = response['url']
    pipeline_id = response['pipeline_id']
    mode = "preempt"  # Replace with the desired mode ("reject", "preempt", or "queue")
    processing_mode = "sync"  # Replace with "async" if needed

    # Construct the URL for the request
    request_url = f"{worker_url}/pipelines/{pipeline_id}/source?mode={mode}&processing={processing_mode}"

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    with open(image, 'rb') as f:
        files = {'file': f}
        response = requests.post(request_url, headers=headers, files=files)

    response_json = json.loads(response.text)
    return response_json

def find_eye_positions(response):
    for obj in response["objects"]:
        if "keyPoints" in obj:
            for keypoint in obj["keyPoints"][0]["points"]:
                if keypoint.get("classLabel") == "right eye":
                    right_eye = keypoint
                elif keypoint.get("classLabel") == "left eye":
                    left_eye = keypoint
    return left_eye, right_eye

def capture_image(type):
    # Initialize the webcam
    cap = cv2.VideoCapture(0)  # 0 indicates the default camera (built-in webcam)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open the camera.")
    else:
        # Capture a single frame from the webcam
        ret, frame = cap.read()

        # Check if the frame was captured successfully
        if not ret:
            print("Error: Could not capture a frame.")
        else:
            # Save the captured frame as an image file
            cv2.imwrite(type + ".jpg", frame)
            print("Image captured and saved")

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

def set_posture(config, type):
    # set posture
    posture = {}
    ready = input(f"Situate yourself in a {type} posture and press enter")
    capture_image(type)

    eyepop_results = parse_image(config, type + '.jpg')
    left_eye, right_eye = find_eye_positions(eyepop_results)
    posture['left_x'] = left_eye['x']
    posture['right_x'] = right_eye['x']
    posture['dx'] = left_eye['x'] - right_eye['x']
    return posture

