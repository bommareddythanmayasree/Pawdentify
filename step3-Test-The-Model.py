import tensorflow as tf
import os
import numpy as np
import cv2
import json

# Load the trained model
modelFile = r"c:\Users\panig\OneDrive\Desktop\pythonTest\mobilenetv2-dog-breed-model.h5"
model = tf.keras.models.load_model(modelFile)
print(model.summary())

# Image and label setup
inputShape = (160, 160)  # Must match training image size
allLabels = np.load(r"c:\Users\panig\OneDrive\Desktop\pythonTest\DogsLabels.npy")
categories = np.unique(allLabels)

# Load the JSON file that contains breed info
jsonFilePath = r"c:\Users\panig\OneDrive\Desktop\pythonTest\breed_info.json"
with open(jsonFilePath, "r") as f:
    breed_info = json.load(f)

# Prepare image for prediction
def prepare_image(img):
    resized = cv2.resize(img, inputShape, interpolation=cv2.INTER_AREA)
    imgResult = np.expand_dims(resized, axis=0)  # Add batch dimension
    imgResult = imgResult / 255.0  # Normalize to 0-1
    return imgResult

# Path to the image to test
testImagePath = r"C:\Users\panig\OneDrive\Desktop\pythonTest\test\0be4fb2606e70ec63a47250467ca169f.jpg"

# Load and preprocess image
img = cv2.imread(testImagePath)
if img is None:
    print(f"❌ Error: Image not found at path: {testImagePath}")
    exit()

imageForModel = prepare_image(img)

# Predict the breed
resultArray = model.predict(imageForModel, verbose=1)
answers = np.argmax(resultArray, axis=1)
predicted_breed = categories[answers[0]]

# ✅ Get confidence of the predicted class
confidence = np.max(resultArray) * 100

print(f"\n🐶 Predicted Breed: {predicted_breed}")
print(f"🎯 Confidence: {confidence:.2f}%")

# ✅ Get Top 3 predictions
top3_indices = np.argsort(resultArray[0])[-3:][::-1]  # top 3 sorted
print("\n🏆 Top 3 Predictions:")
for i, idx in enumerate(top3_indices):
    breed = categories[idx]
    conf = resultArray[0][idx] * 100
    print(f"{i+1}. {breed} - {conf:.2f}%")

# Fetch breed details from JSON
info = breed_info.get(predicted_breed, None)

if info:
    nature = info.get("nature", "Not available")
    diet = info.get("diet", "Not available")
    healthcare = info.get("healthcare_tips", "Not available")

    print("\n📖 Breed Information:")
    print(f"• Nature: {nature}")
    print(f"• Diet: {diet}")
    print(f"• Healthcare Tips: {healthcare}")
else:
    print("\n⚠️ No additional information found for this breed.")

# Display image with prediction text
font = cv2.FONT_HERSHEY_SIMPLEX
text = f"{predicted_breed} ({confidence:.1f}%)"
cv2.putText(img, text, (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
cv2.imshow("Prediction", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
