# ImageFilter for using filter() function
from PIL import Image, ImageFilter
import os 

# Opening the image 
folder_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(folder_path, 'office_noisy.png')
image = Image.open(image_path)

# Blurring image by sending the ImageFilter.
# using GaussianBlur. ImageFilter.GaussianBlur(radius: float = ...)
# radius: Standard deviation of the Gaussian kernel(σ).
image = image.filter(ImageFilter.GaussianBlur(4))

# Displaying the image
image.show()



