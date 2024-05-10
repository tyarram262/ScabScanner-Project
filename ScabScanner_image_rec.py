import cv2
import os
import numpy as np
from skimage import exposure

# Function to extract features from an image
def extract_features(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Extract HOG features
    hog = cv2.HOGDescriptor()
    features = hog.compute(gray)
    
    # Normalize the image
    features = exposure.rescale_intensity(features, out_range=(0, 255))
    
    return features.flatten()

# Function to compare an image with a dataset
def compare_with_dataset(image_path, dataset_path):
    # Extract features from the input image
    query_features = extract_features(image_path)
    
    # Iterate through images in the dataset
    min_distance = float('inf')
    classification = None
    for class_label in os.listdir(dataset_path):
        class_dir = os.path.join(dataset_path, class_label)
        for filename in os.listdir(class_dir):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                dataset_image_path = os.path.join(class_dir, filename)
                
                # Extract features from the dataset image
                dataset_features = extract_features(dataset_image_path)
                
                # Calculate distance between features
                distance = np.linalg.norm(query_features - dataset_features)
                
                # Update minimum distance and classification
                if distance < min_distance:
                    min_distance = distance
                    classification = class_label
    
    return classification

# Provide paths to the input image and dataset directory
input_image_path = r'C:\Users\Druv Pabba\OneDrive\Desktop\Wound_dataset\Laceration\laseration (8).jpg'
dataset_path = r'C:\Users\Druv Pabba\OneDrive\Desktop\Wound_dataset'

# Call the function to compare with the dataset
classification = compare_with_dataset(input_image_path, dataset_path)
print("The input image belongs to class:", classification)
if classification == "laceration":
    print("Here are the first-aid steps to treat your laceration: \n 1. Wash your hands. This helps avoid infection. \n 2.Stop the bleeding. \n 3.Clean the wound. \n 4. Put on an antibiotic or petroleum jelly. \n 5. Cover the wound. \n 6.Change the covering. \n 7.Get a tetanus shot. \n 8.Watch for signs of infection.")
if classification == "Laceration":
    print("Here are the first-aid steps to treat your laceration: \n 1. Wash your hands. This helps avoid infection. \n 2.Stop the bleeding by appyling pressure. \n 3.Clean the wound. \n 4. Put on an antibiotic or petroleum jelly. \n 5. Cover the wound. \n 6.Change the covering. \n 7.Get a tetanus shot. \n 8.Watch for signs of infection.")
if classification == "lacerations":
    print("Here are the first-aid steps to treat your laceration: \n 1. Wash your hands. This helps avoid infection. \n 2.Stop the bleeding. \n 3.Clean the wound. \n 4. Put on an antibiotic or petroleum jelly. \n 5. Cover the wound. \n 6.Change the covering. \n 7.Get a tetanus shot. \n 8.Watch for signs of infection.")
if classification == "cut":
    print("Here is what to do if you have a cut: \n Rinse the cut or wound with water and apply pressure with sterile gauze, a bandage, or a clean cloth. If blood soaks through the bandage, put another bandage on top of the first and keep applying pressure. Raise the injured body part to slow bleeding. When bleeding stops, cover the wound with a new, clean bandage.")
if classification == "cuts":
    print("Here is what to do if you have a cut: \n Rinse the cut or wound with water and apply pressure with sterile gauze, a bandage, or a clean cloth. If blood soaks through the bandage, put another bandage on top of the first and keep applying pressure. Raise the injured body part to slow bleeding. When bleeding stops, cover the wound with a new, clean bandage.")
if classification == "Cut":
    print("Here is what to do if you have a cut: \n Rinse the cut or wound with water and apply pressure with sterile gauze, a bandage, or a clean cloth. If blood soaks through the bandage, put another bandage on top of the first and keep applying pressure. Raise the injured body part to slow bleeding. When bleeding stops, cover the wound with a new, clean bandage.")
if classification == "Cuts":
    print("Here is what to do if you have a cut: \n Rinse the cut or wound with water and apply pressure with sterile gauze, a bandage, or a clean cloth. If blood soaks through the bandage, put another bandage on top of the first and keep applying pressure. Raise the injured body part to slow bleeding. When bleeding stops, cover the wound with a new, clean bandage.")
if classification == "stab wound":
    print("Here are first-aid steps to help:\nApply direct pressure to try and control bleeding. If you can control the bleeding with pressure, keep holding for 10 minutes as it takes this amount of time for clots to form. Keep checking their vital signs, level of consciousness and breathing – expect that they may deteriorate.")
if classification == "Stab wound":
    print("Here are first-aid steps to help:\nApply direct pressure to try and control bleeding. If you can control the bleeding with pressure, keep holding for 10 minutes as it takes this amount of time for clots to form. Keep checking their vital signs, level of consciousness and breathing – expect that they may deteriorate.")
if classification == "Ingrown nail":
    print("Here are the first-aid steps: \ns1.Soak your foot in warm water mixed with Epsom salt or soapy, sudsy water twice daily. \n2.Keep your foot dry the rest of the time. \n3.Gently lift the edge of your nail.\n4.Use an antibiotic cream and a bandage. \n5.Wear roomy shoes or sandals. \n6. Use pain relievers such as ibuprofen or acetaminophen, if needed. ")
if classification == "ingrown nail":
    print("Here are the first-aid steps: \ns1.Soak your foot in warm water mixed with Epsom salt or soapy, sudsy water twice daily. \n2.Keep your foot dry the rest of the time. \n3.Gently lift the edge of your nail.\n4.Use an antibiotic cream and a bandage. \n5.Wear roomy shoes or sandals. \n6. Use pain relievers such as ibuprofen or acetaminophen, if needed. ")
if classification == "Ingrown Nail":
    print("Here are the first-aid steps: \ns1.Soak your foot in warm water mixed with Epsom salt or soapy, sudsy water twice daily. \n2.Keep your foot dry the rest of the time. \n3.Gently lift the edge of your nail.\n4.Use an antibiotic cream and a bandage. \n5.Wear roomy shoes or sandals. \n6. Use pain relievers such as ibuprofen or acetaminophen, if needed. ")
if classification == "Burns":
    print("Here are the first-aid steps: \n1.Cool the burn. \n2.Remove rings or other tight items from the burned area.\n3.Don't break blisters. \n4.Apply lotion. \n5.Bandage the burn. \n6.If needed, take a nonprescription pain reliever, such as ibuprofen (Advil, Motrin IB, others), naproxen sodium (Aleve) or acetaminophen (Tylenol, others).")
if classification == "burns":
    print("Here are the first-aid steps: \n1.Cool the burn. \n2.Remove rings or other tight items from the burned area.\n3.Don't break blisters. \n4.Apply lotion. \n5.Bandage the burn. \n6.If needed, take a nonprescription pain reliever, such as ibuprofen (Advil, Motrin IB, others), naproxen sodium (Aleve) or acetaminophen (Tylenol, others).")
if classification == "burn":
    print("Here are the first-aid steps: \n1.Cool the burn. \n2.Remove rings or other tight items from the burned area.\n3.Don't break blisters. \n4.Apply lotion. \n5.Bandage the burn. \n6.If needed, take a nonprescription pain reliever, such as ibuprofen (Advil, Motrin IB, others), naproxen sodium (Aleve) or acetaminophen (Tylenol, others).")
if classification == "bruise":
    print("Here are the first-aid steps: \n1.Elevate the bruised area above heart level, if possible. \n2.Apply an ice pack wrapped in a thin towel. Leave it in place for 20 minutes. \n3.If the bruised area is swelling, put an elastic bandage around it, but not too tight.")
if classification == "bruises":
    print("Here are the first-aid steps: \n1.Elevate the bruised area above heart level, if possible. \n2.Apply an ice pack wrapped in a thin towel. Leave it in place for 20 minutes. \n3.If the bruised area is swelling, put an elastic bandage around it, but not too tight.")
if classification == "Bruise":
    print("Here are the first-aid steps: \n1.Elevate the bruised area above heart level, if possible. \n2.Apply an ice pack wrapped in a thin towel. Leave it in place for 20 minutes. \n3.If the bruised area is swelling, put an elastic bandage around it, but not too tight.")
if classification == "Abrasion":
    print("Here is what to do for an abrasion: \nApply an antiseptic lotion, cream, or petroleum jelly. Cover the area with an adhesive bandage or gauze pad if the area is on the hands or feet, or if it is likely to drain onto clothing. Change the dressing often. Check the area each day and keep it clean and dry.")
if classification == "abrasion":
    print("Here is what to do for an abrasion: \nApply an antiseptic lotion, cream, or petroleum jelly. Cover the area with an adhesive bandage or gauze pad if the area is on the hands or feet, or if it is likely to drain onto clothing. Change the dressing often. Check the area each day and keep it clean and dry.")
if classification == "abrasions":
    print("Here is what to do for an abrasion: \nApply an antiseptic lotion, cream, or petroleum jelly. Cover the area with an adhesive bandage or gauze pad if the area is on the hands or feet, or if it is likely to drain onto clothing. Change the dressing often. Check the area each day and keep it clean and dry.")
