import cv2
import os

def make_video_from_images(folder_path, output_video_file, fps=30):
    # Get all image files in the folder
    image_files = [img for img in os.listdir(folder_path) if img.endswith(".png") or img.endswith(".jpg")]
    image_files.sort()  # Sort the images if they are numbered

    # Check if there are any images
    if not image_files:
        print("No images found in the folder.")
        return

    # Read the first image to determine the video size
    frame = cv2.imread(os.path.join(folder_path, image_files[0]))
    if frame is None:
        print(f"Failed to read the image: {image_files[0]}")
        return

    height, width, layers = frame.shape
    print(f"Image dimensions: {width}x{height}, Number of images: {len(image_files)}")

    # Initialize the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use other codecs as well, depending on your platform
    video = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

    # Process each image
    for image in image_files:
        frame = cv2.imread(os.path.join(folder_path, image))
        if frame is not None:
            video.write(frame)  # Write the frame to the video
        else:
            print(f"Failed to read the image: {image}")

    video.release()
    print(f"Video saved as {output_video_file}, FPS: {fps}")

# Folder containing images and output video file
folder_path = 'rgb'
output_video_file = 'output_video.mp4'

# Create the video
make_video_from_images(folder_path, output_video_file)
