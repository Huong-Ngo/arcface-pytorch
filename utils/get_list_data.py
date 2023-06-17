import os
from pathlib import Path
import random

def get_person_image_paths(path_person_set: str) -> dict:
    """Creates mapping from person name to list of images.
    Args:
        path_person_set (str): Path to dataset that contains folder of images.
    Returns:
        Dict[str, List]: Mapping from person name to image paths,
                         For instance {'name': ['/path/image1.jpg', '/path/image2.jpg']}
    """
    
    person_paths=[]
    for person_path in os.listdir(path_person_set):
      if '.ipynb' not in person_path:
        person_paths.append(Path(path_person_set+'/'+person_path))
    return {
        path.name:list(str(path)+'/'+file for file in list(os.listdir(path))) for path in person_paths
    }


def get_list_data_file(root: str, file_path: str):
    person_paths = get_person_image_paths(root)
    list_person = list(person_paths.keys())
    list_label = list(range(len(list_person)))
    f = open(file_path, "w")
    for key, list_img_paths in person_paths.items():
        for img_path in list_img_paths:
            try:
                line = img_path + ' ' + str(list_person.index(key)) + '\n'
                f.write(line)
            except:
               print(line)
    f.close()


def get_list_data_file_val(root: str, file_path: str):
    random.seed(100)
    person_paths = get_person_image_paths(root)
    list_person = list(person_paths.keys())
    # list_label = list(range(len(list_person)))
    f = open(file_path, "w")
    list_imgs = []
    list_labels = []
    for key, list_img_paths in person_paths.items():
        for img_path in list_img_paths:
            list_imgs.append(img_path)
            list_labels.append(key)

    for img_path1 in list_imgs:
        
        img_path2 = random.choice(list_imgs)
            
        while list_labels[list_imgs.index(img_path1)] == list_labels[list_imgs.index(img_path2)]:
            img_path2 = random.choice(list_imgs)
        line = img_path1 + ' ' + img_path2 + ' ' + '0' +'\n'
        # else:
        #     line = img_path1 + ' ' + img_path2 + ' ' + '0' +'\n'              
        
        f.write(line)
    f.close()



