import numpy as np
# My own codes import
import directory



def find(x_new, model):
    
    # Convert the list to a numpy array and reshape it to (-1, 784)
    x_new = np.array(x_new).reshape(-1, 784)
    
    predictions = model.predict(x_new)
    
    number = np.argmax(predictions)
    predictions = predictions.tolist()
    predictions = predictions[0]
    percentages = [round(p * 100, 2) for p in predictions]
    
    return number, percentages
