# ImageFilter for using filter() function
from PIL import Image, ImageFilter
import os 

class data: 
    def __init__(self, image_name, standard_deviation,question): 
        self.image_name = image_name 
        self.standard_deviation = standard_deviation
        self.question = question

# this array/list is according to the data provided in the questions
data_list = [
    data("office_noisy.png",0.5,"Question_0_σ=0.5"),
    data("office_noisy.png",1,"Question_0_σ=1"),
    data("office_noisy.png",2,"Question_0_σ=2"),
    data("office_noisy.png",5,"Question_0_σ=5"),
    data("office_noisy.png",10,"Question_0_σ=10"),
    data("office_noisy.png",50,"Question_0_σ=50"),
    data("office_noisy.png",7.74,"Question_3_σ=7.74"),
]

# looping through the data_list
for d in data_list: 

    # Opening the image 
    folder_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(folder_path, d.image_name)
    image = Image.open(image_path)

    # Blurring image by sending the ImageFilter.
    # using GaussianBlur. ImageFilter.GaussianBlur(radius: float = ...)
    # radius: Standard deviation of the Gaussian kernel(σ).
    image = image.filter(ImageFilter.GaussianBlur(d.standard_deviation))

    # saving the images in diffused_images folder according to their names
    image.save(os.path.join(folder_path, "diffused_images/"+d.question+".png"))

    # Displaying the image
    # image.show will display the images but it displays the images with temporary names
    # images with questions names will be saved in the diffused_images folder after running the code
    image.show()



