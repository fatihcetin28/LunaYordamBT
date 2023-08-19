from ButtonImages import ButtonImages
import ImageFilaPaths

img1 = ButtonImages(r"C:\Users\faikkamil\Documents\totextdemo.png", "Oppie")

# print(img1.description)
# print(img1.file_path)

# print(img1.to_text())

print(img1.is_image_exist_on_window())
print(img1.locate_center())
