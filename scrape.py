# import os
# import pandas as pd
# import requests
# from urllib.parse import urlparse
# from PIL import Image
# import google.generativeai as genai
# import re

# # Configure the Gemini API
# API_KEY = 'AIzaSyDA1AX3VVLFXuZ7XBzQjraapE1ZW5pqa98'  # Set your actual API key here
# genai.configure(api_key=API_KEY)

# # Initialize the model
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Load the Excel file
# df = pd.read_excel('C:/Users/Haseeb/Desktop/scraping/Glasses_f.xlsx')

# # Extract and process image URLs
# image_urls = df['Product Images'].apply(lambda x: x.split(',')).tolist()
# image_urls = [url.strip() for sublist in image_urls for url in sublist]

# # Limiting the number of URLs for testing
# image_urls = image_urls[:20]
# print(f"Number of image URLs: {len(image_urls)}")

# # Directory to save downloaded images
# save_dir = 'C:/Users/Haseeb/Desktop/scraping/images'
# os.makedirs(save_dir, exist_ok=True)

# # Function to download images
# def download_image(url):
#     try:
#         parsed_url = urlparse(url)
#         image_name = os.path.basename(parsed_url.path)
#         image_path = os.path.join(save_dir, image_name)
        
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()

#         with open(image_path, 'wb') as f:
#             f.write(response.content)
#         print(f"Image downloaded: {image_path}")
#         return image_path
#     except requests.exceptions.RequestException as e:
#         print(f"Failed to download {url}: {e}")
#         return None

# # Download all images
# image_paths = [download_image(url) for url in image_urls if url]

# # Add columns for Title, Description, and Features
# df['Generated Title'] = ''
# df['Generated Description'] = ''
# df['Generated Features'] = ''

# # Function to generate product details using the Gemini API and save them to the Excel file
# def generate_product_details(image_path, row_index):
#     try:
#         # Open the image file
#         image = Image.open(image_path)
        
#         # Generate content using the Gemini API
#         response = model.generate_content([
#             "Generate title, description, and features for this product.",
#             image
#         ])
        
#         # Extract the generated details from the response
#         generated_text = response.text.strip()
        
#         # Improved parsing logic based on the response format
#         title_match = re.search(r"^## (.+)", generated_text)
#         description_match = re.search(r"\*\*Description:\*\*\n\n(.*?)(?=\n\n\*\*Features:\*\*)", generated_text, re.DOTALL)
#         features_match = re.search(r"\*\*Features:\*\*\n\n(.*)", generated_text, re.DOTALL)
        
#         title = title_match.group(1).strip() if title_match else 'Default Title'
#         description = description_match.group(1).strip() if description_match else 'Default Description'
#         features = features_match.group(1).strip() if features_match else 'Default Features'

#         # Save the generated details to the DataFrame
#         df.at[row_index, 'Generated Title'] = title
#         df.at[row_index, 'Generated Description'] = description
#         df.at[row_index, 'Generated Features'] = features

#         print(f"Processed: {image_path} with generated details.")
#     except Exception as e:
#         print(f"Failed to generate details for {image_path}: {e}")

# # Iterate over each image and generate the product details
# for idx, image_path in enumerate(image_paths):
#     if image_path:
#         generate_product_details(image_path, idx)

# # Save the DataFrame back to Excel
# df.to_excel('C:/Users/Haseeb/Desktop/scraping/product_details.xlsx', index=False)

###########################################################################################


# import os
# import pandas as pd
# import requests
# from urllib.parse import urlparse
# from PIL import Image
# import google.generativeai as genai
# import re
# import uuid

# # Configure the Gemini API
# API_KEY = 'AIzaSyDA1AX3VVLFXuZ7XBzQjraapE1ZW5pqa98'  # Set your actual API key here
# genai.configure(api_key=API_KEY)

# # Initialize the model
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Load the Excel file
# df = pd.read_excel('C:/Users/Haseeb/Desktop/scraping/Glasses_f.xlsx')

# # Extract and process image URLs
# image_urls = df['Product Images'].apply(lambda x: x.split(',')).tolist()
# image_urls = [url.strip() for sublist in image_urls for url in sublist]

# # Limiting the number of URLs for testing
# image_urls = image_urls[:20]
# print(f"Number of image URLs: {len(image_urls)}")

# # Directory to save downloaded images
# save_dir = 'C:/Users/Haseeb/Desktop/scraping/images'
# os.makedirs(save_dir, exist_ok=True)

# # Function to download images
# def download_image(url):
#     try:
#         parsed_url = urlparse(url)
#         image_name = os.path.basename(parsed_url.path)
#         image_path = os.path.join(save_dir, image_name)
        
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()

#         with open(image_path, 'wb') as f:
#             f.write(response.content)
#         print(f"Image downloaded: {image_path}")
#         return image_path
#     except requests.exceptions.RequestException as e:
#         print(f"Failed to download {url}: {e}")
#         return None

# # Download all images
# image_paths = [download_image(url) for url in image_urls if url]

# # Add columns for Title, Description, and Features
# df['Generated Title'] = ''
# df['Generated Description'] = ''
# df['Generated Features'] = ''

# # Function to generate product details using the Gemini API
# def generate_product_details(image_path, row_index):
#     try:
#         # Open the image file
#         image = Image.open(image_path)
        
#         # Generate content using the Gemini API
#         response = model.generate_content([
#             "Generate title, description, and features for this product.",
#             image
#         ])
        
#         # Extract the generated details from the response
#         generated_text = response.text.strip()
        
#         # Improved parsing logic based on the response format
#         title_match = re.search(r"^## (.+)", generated_text)
#         description_match = re.search(r"\*\*Description:\*\*\n\n(.*?)(?=\n\n\*\*Features:\*\*)", generated_text, re.DOTALL)
#         features_match = re.search(r"\*\*Features:\*\*\n\n(.*)", generated_text, re.DOTALL)
        
#         # Handle missing or duplicate data
#         title = title_match.group(1).strip() if title_match else generate_unique_title()
#         description = description_match.group(1).strip() if description_match else 'Default Description'
#         features = features_match.group(1).strip() if features_match else 'Default Features'
        
#         # Save the generated details to the DataFrame
#         df.at[row_index, 'Generated Title'] = title
#         df.at[row_index, 'Generated Description'] = description
#         df.at[row_index, 'Generated Features'] = features

#         print(f"Processed: {image_path} with generated details.")
#     except Exception as e:
#         print(f"Failed to generate details for {image_path}: {e}")

# def generate_unique_title():
#     # Generate a unique title using UUID
#     return f"Unique Product Title {uuid.uuid4().hex[:8]}"

# def reprocess_default_entries():
#     # Iterate over the DataFrame and reprocess default entries
#     for idx, row in df.iterrows():
#         if row['Generated Description'] == 'Default Description':
#             # Download image if not already downloaded
#             image_path = download_image(row['Product Images'].split(',')[0].strip())
#             if image_path:
#                 generate_product_details(image_path, idx)
                
# # Initial processing
# for idx, image_path in enumerate(image_paths):
#     if image_path:
#         generate_product_details(image_path, idx)

# # Reprocess any default entries
# reprocess_default_entries()

# # Save the DataFrame back to Excel
# df.to_excel('C:/Users/Haseeb/Desktop/scraping/product_details.xlsx', index=False)

#######################################################################################


import os
import pandas as pd
import requests
from urllib.parse import urlparse
from PIL import Image
import google.generativeai as genai
import re
import uuid

# Configure the Gemini API
API_KEY = 'AIzaSyDA1AX3VVLFXuZ7XBzQjraapE1ZW5pqa98'  # Set your actual API key here
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Load the Excel file
df = pd.read_excel('C:/Users/Haseeb/Desktop/scraping/Glasses_f.xlsx')

# Extract and process image URLs
image_urls = df['Product Images'].apply(lambda x: x.split(',')).tolist()
image_urls = [url.strip() for sublist in image_urls for url in sublist]

# Limiting the number of URLs for testing
image_urls = image_urls[:20]
print(f"Number of image URLs: {len(image_urls)}")

# Directory to save downloaded images
save_dir = 'C:/Users/Haseeb/Desktop/scraping/images'
os.makedirs(save_dir, exist_ok=True)

# Function to download images
def download_image(url):
    try:
        parsed_url = urlparse(url)
        image_name = os.path.basename(parsed_url.path)
        image_path = os.path.join(save_dir, image_name)
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded: {image_path}")
        return image_path
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return None

# Download all images
image_paths = [download_image(url) for url in image_urls if url]

# Add columns for Title, Description, and Features
df['Generated Title'] = ''
df['Generated Description'] = ''
df['Generated Features'] = ''

# Function to generate product details using the Gemini API
def generate_product_details(image_path, row_index):
    try:
        # Open the image file
        image = Image.open(image_path)
        
        # Generate content using the Gemini API
        response = model.generate_content([
            "Generate a unique title, a detailed long description, and 5-8 key features for this product.",
            image
        ])
        
        # Extract the generated details from the response
        generated_text = response.text.strip()
        
        # Parsing logic based on the response format
        title_match = re.search(r"^## (.+)", generated_text)
        description_match = re.search(r"\*\*Description:\*\*\n\n(.*?)(?=\n\n\*\*Features:\*\*)", generated_text, re.DOTALL)
        features_match = re.search(r"\*\*Features:\*\*\n\n(.*)", generated_text, re.DOTALL)
        
        # Extracting the content generated by the model
        title = title_match.group(1).strip() if title_match else ''
        description = description_match.group(1).strip() if description_match else ''
        features = features_match.group(1).strip().split('\n') if features_match else []
        
        # Limit the features to a maximum of 5-8
        features = features[:8]
        
        # Save the generated details to the DataFrame
        df.at[row_index, 'Generated Title'] = title
        df.at[row_index, 'Generated Description'] = description
        df.at[row_index, 'Generated Features'] = '\n'.join(features)

        print(f"Processed: {image_path} with generated details.")
    except Exception as e:
        print(f"Failed to generate details for {image_path}: {e}")

# Initial processing
for idx, image_path in enumerate(image_paths):
    if image_path:
        generate_product_details(image_path, idx)

# Save the DataFrame back to Excel
df.to_excel('C:/Users/Haseeb/Desktop/scraping/product_details.xlsx', index=False)
