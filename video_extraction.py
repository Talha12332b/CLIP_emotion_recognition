import cv2
import os
video_names =os.listdir("C:\\Users\\talha\\Documents\\CLIP\\test-1e\\test-1\\test-1")
# video_names[0]
# Load the video
for video_name in video_names:
    if '.zip' not in video_name:
        video_path = os.path.join("C:\\Users\\talha\\Documents\\CLIP\\test-1e\\test-1\\test-1", video_name)
        num_frames_to_capture = 10
        output_dir = 'C:\\Users\\talha\\Documents\\CLIP\\unzip_folder'

        cap = cv2.VideoCapture(video_path)

        # Get the total number of frames in the video
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Calculate the interval at which to capture frames
        interval = total_frames // num_frames_to_capture

        # Get the video name without extension
        video_name = os.path.splitext(os.path.basename(video_path))[0]

        # Directory to save frames
        os.makedirs(output_dir, exist_ok=True)

        # Loop through the video and capture frames at the specified intervals
        for i in range(num_frames_to_capture):
            frame_number = i * interval
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            ret, frame = cap.read()
            if ret:
                # Construct the frame filename
                frame_filename = os.path.join(output_dir, f'{video_name}_frame_{frame_number}.jpg')
                # Save the frame
                cv2.imwrite(frame_filename, frame)
            else:
                print(f"Failed to capture frame at {frame_number}")

        # Release the video capture object
        cap.release()

        print(f"Frames saved in {output_dir} directory.")
