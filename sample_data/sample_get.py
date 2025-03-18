#Run this file to clone the sample_data into your local machine and test it
import os
import git

def clone_audio(target_folder="sample_data/audio"):
    """
    Clones the Free Spoken Digit Dataset (FSDD) repository into a specified folder.
    
    Parameters:
    target_folder (str): The directory where the dataset will be cloned.
    """
    repo_url = "https://github.com/Jakobovski/free-spoken-digit-dataset.git"

    # Create target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Clone the repo if it hasn't been cloned already
    if not os.path.exists(os.path.join(target_folder, ".git")):
        print(f"Cloning FSDD into {target_folder}...")
        git.Repo.clone_from(repo_url, target_folder)
        print("✅ Cloning complete!")
    else:
        print("✅ Repository already exists. Skipping cloning.")

def clone_image(target_folder="sample_data/image"):
    """
    Clones the Set14 (Standard Image Processing Dataset) repository into a specified folder.
    
    Parameters:
    target_folder (str): The directory where the dataset will be cloned.
    """
    repo_url = "https://github.com/jbhuang0604/SelfExSR.git"

    # Create target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Clone the repo if it hasn't been cloned already
    if not os.path.exists(os.path.join(target_folder, ".git")):
        print(f"Cloning set14 into {target_folder}...")
        git.Repo.clone_from(repo_url, target_folder)
        print("✅ Cloning complete!")
    else:
        print("✅ Repository already exists. Skipping cloning.")

clone_audio()
clone_image()
