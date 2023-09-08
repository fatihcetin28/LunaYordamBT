import os

# Get the file path of the current module
module_file_path = __file__

# Get the parent directory of the module
module_parent_directory = os.path.dirname(module_file_path)

# Get the parent directory of the module's parent directory
parent_of_module_parent = os.path.dirname(module_parent_directory)


print(os.path.join(parent_of_module_parent,"ButtonImages"))

button_images_path = os.path.join(parent_of_module_parent,"ButtonImages")

uyari_images_path = os.path.join(parent_of_module_parent,"uyariImages")

uyari_title = os.path.join(uyari_images_path,"uyariBaslik.png")

iade_al_button = os.path.join(button_images_path,"iadealbutton.png")

vazgec_button = os.path.join(button_images_path, "vazgecButton.PNG")

odunc_ver_button = os.path.join(button_images_path,"oduncverbutton.png" )

# Opening Modules
uye_odunc_islemleri_button = os.path.join(button_images_path,"uyeoduncislemleri.png")

odunc_islemleri = os.path.join(button_images_path,"odunc.png" )

