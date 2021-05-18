from PIL import Image

# Make some RGB values. 
colors = (255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), (0, 0, 0), (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, (0, 0, 0), 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255)
# Convert list to bytes
#colors = bytes(colors)
img = Image.putpixel(colors)
img.show()
img.save('flag.png')
#im = Image.frombytes("RGB", (width, height), img_bytes)