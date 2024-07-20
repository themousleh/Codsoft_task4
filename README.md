# Sales Prediction Project

## Overview

The Sales Prediction project involves developing a machine learning model to predict sales based on advertising budgets for TV, radio, and newspapers. The model uses a Linear Regression algorithm trained on a dataset of advertising expenditures and corresponding sales. This project includes a GUI application built with Tkinter to interactively input advertising budgets and obtain sales predictions.

## Project Structure

- **Data**: The dataset containing advertising expenditures and sales (`advertising.csv`).
- **Model Training**: Python script (`train_model.py`) to train and save the model.
- **GUI Application**: Python script (`app.py`) that provides a graphical user interface for predicting sales based on user input.
- **Model Files**: Saved model file (`sales_prediction_model.pkl`).

## Objectives

1. [Load and Explore the Dataset](#load-and-explore-the-dataset)
2. [Data Preprocessing](#data-preprocessing)
3. [Train-Test Split](#train-test-split)
4. [Model Training](#model-training)
5. [Model Evaluation](#model-evaluation)
6. [GUI Application](#gui-application)

## Getting Started

### Prerequisites

- Python 3.x
- `pandas`
- `scikit-learn`
- `joblib`
- `tkinter`

You can install the required packages using pip:

```bash
pip install pandas scikit-learn joblib
```

## Training the Model
- Ensure `advertising.csv` is in the project directory.
- Run `train_model.py` to train and save the model:
```bash
python train_model.py
```

## Running the GUI Application
- Ensure `sales_prediction_model.pkl` is in the same directory as `app.py`.
- Run `app.py`:
```bash
python app.py
```
This will open a GUI application where you can input advertising budgets and get a sales prediction.

## Usage
1. Enter the advertising budgets for TV, radio, and newspapers into the GUI.
2. Click "Predict Sales" to see the predicted sales amount.

## Troubleshooting
- **Deprecation Warnings**: Update your packages if you see warnings about deprecated features.
- **Input Issues**: Ensure that you are entering numerical values for the advertising budgets. Invalid input will trigger an error message.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.

## Acknowledgments
This project utilizes a standard dataset for sales prediction and leverages Linear Regression and Tkinter for model training and GUI development.

## Contact
For questions or feedback, please contact [Your Name](mailto:your-email@example.com).
