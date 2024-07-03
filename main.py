from pathlib import Path
from PIL import Image

def extract_frames(gif_path, output_folder):
    # Open the GIF file
    with Image.open(gif_path) as img:
        # Loop over each frame in the GIF
        for frame_number in range(img.n_frames):
            # Specify the frame to seek to
            img.seek(frame_number)

            # Extract the frame and save it
            frame = img.copy()
            frame.save(f"{output_folder}/frame_{frame_number}.png")

# Example usage
gif_path = './gifs/giphy.gif'
output_folder = 'output_folder'
Path(output_folder).mkdir()
extract_frames(gif_path, output_folder)
