
<p align="center">
  <a href="https://quera.org/"><img src="handwrite-digit-predict-tool/files/github image
/1.jpg" width="100" title="کوئرا - حل سوالات برنامه نویسی"></a>
</p>
***
# Hand write alphabet prediction ✅
### This project is a machine learning model designed to predict handwritten alphabet in english and persian. The model is trained on the MNIST dataset (english alphabet MNIST), which consists of 360,000 images and, Personal collected database for persian alphabet, which consists of 12,000 images of handwritten alphabet. The project includes a user interface built with Tkinter for easy interaction and visualization.

# Features
* Alphabet Prediction: Predicts the handwritten alphabet with over 95% accuracy
* User Interface: A simple and intuitive UI built with Tkinter for drawing alphabet and viewing predictions.
* Model: Utilizes a neural network model trained on the both dataset.
* Visualization: Displays the drawn alphabet and the predicted result.
  
***
# Installation
### Clone the Repository:
```git
git clone https://github.com/mr-mahmood/handwritten-digit-prediction.git
cd handwritten-digit-prediction
```

### Create a Virtual Environment:
```python
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

***
# Usage
* Run the Application:
```python
python main.py
```

* Draw a Digit: Use the Tkinter interface to draw a digit.
* Predict: Click the “Predict” button to see the predicted digit.

***

# Model Training
### The model is trained using a neural network with the following architecture:

## English alphabet
```python
model = keras.Sequential([
    keras.Input(shape=(784,)),
    
    Dense(units=300, activation='relu'),
    Dropout(0.2),  # Add dropout layer with a rate of 0.2 (20%)
    
    Dense(units=200, activation='relu'),
    Dropout(0.2),  # Add dropout layer with a rate of 0.2 (20%)
    
    Dense(units=26, activation='softmax'),
])

early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=4,          # Number of epochs with no improvement to wait before stopping
    restore_best_weights=True  # Restore model weights from the epoch with the best validation loss
)

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=2000, epochs=20, validation_split=0.1, callbacks=[early_stopping], shuffle=True)
```

## Persian alphabet
```python
model = keras.Sequential([
    keras.Input(shape=(784,)),
    
    Dense(units=300, activation='relu'),
    Dropout(0.2),  # Add dropout layer with a rate of 0.2 (20%)
    
    Dense(units=200, activation='relu'),
    Dropout(0.2),  # Add dropout layer with a rate of 0.2 (20%)
    
    Dense(units=32, activation='softmax'),
])

early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=4,          # Number of epochs with no improvement to wait before stopping
    restore_best_weights=True  # Restore model weights from the epoch with the best validation loss
)

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=100, epochs=20, validation_split=0.1, callbacks=[early_stopping], shuffle=True)
```
***
# Attention⚠️
* ### The training scripts and dataset are not included in the repository because of file size Limitation in github.
* ### Contributions are welcome! Please fork the repository and submit a pull request.
