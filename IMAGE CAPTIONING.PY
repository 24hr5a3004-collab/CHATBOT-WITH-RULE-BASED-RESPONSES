from transformers import pipeline
from PIL import Image

# Load image captioning model
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# Open image
image = Image.open("IMAGE1.jpg")

# Generate caption
result = captioner(image)

print("Caption:", result[0]['generated_text'])