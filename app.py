#Importing necessary libraries
import gradio as gr
#import scikit-learn as sklearn
#from fastai.vision.all import *
from sklearn.metrics import roc_auc_score

#Define dependent functions
def get_x(row): return Path(str(path/f"{row['rootname']}_small"/f"{row['ID']}") + ".png")
def get_y(row): return row["LABEL"]

def auroc_score(input, target):
    input, target = input.cpu().numpy()[:,1], target.cpu().numpy()
    return roc_auc_score(target, input)

#Load the model
learn = load_learner("export.pkl")

#Identify labels from the dataloaders class
labels = ["Negative", "Positive"]

#Define function for making prediction
def predict(img):
    img = PILImage.create(img)
    pred, idx, probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

#Customizing the gradio interface
title = "Classifying x-ray scans as either positive or negative Tuberculosis(TB)"

description = """Catching TB early can be life altering.
Among various techniques used for detecting Tuberculosis, image scanning can be aided with computer vision.
This dataset was obtained from Zindi with link below. 
Note: This model and classification is mainly for educational purpose and any user uses it at their own discretion"""

article="<p style='text-align: center'><a href='https://zindi.africa/competitions/runmila-ai-institute-minohealth-ai-labs-tuberculosis-classification-via-x-rays-challenge' target='_blank'>Link to Zindi competition</a></p>"

examples = ['patient1.png', 'patient2.png', 'patient3.png']

enable_queue=True


#Launching the gradio application
gr.Interface(fn=predict,inputs=gr.inputs.Image(shape=(800, 800)),
             outputs=gr.outputs.Label(num_top_classes=1),
             title=title,
             description=description,article=article,
             examples=examples,
             enable_queue=enable_queue).launch(share=True, )