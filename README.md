# Credit Score Analysis

[Anton Markov et al (Credit scoring methods: Latest trends and points to consider, 2022)](https://www.sciencedirect.com/science/article/pii/S2405918822000095) suggest that University of California Irvine's datasets are among the most popular public sources for credit score modeling. I have chosen the [UCI (Statlog) German Credit Data](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data) to begin with.

# German Credit Data 

This dataset contains information about 1000 loan applications, including personal and financial data, credit history, and loan characteristics.

# Objective

Train models in order to predict weather a loan is benefitial or not, in other words predict its creditability for the finantial institution.

# Models

## 1. Logistic Regression

![LogRegConfusionMatrix](https://github.com/user-attachments/assets/f7db9635-87d2-498a-9683-e128d0198dc9)
![LogRegClassificationReport](https://github.com/user-attachments/assets/13f612e6-324c-4d53-964d-e466e2e60f12)


Due to some imbalanced columns, the logreg model presents difficulty in predicting "Bad" loans. To overcome this limitation we might consider oversampling the misrepresented categories in these columns.

# Data Science Template

This sample repo contains the recommended structure for a Python data science project. For more information on data science in VS Code, see the [Data Science Overview](https://code.visualstudio.com/docs/datascience/overview) in our docs. In this sample, we use the `pandas` and `matplotlib` libraries to perform data analysis and visualize sample data and the `pytest` library to perform tests.

For a more in-depth tutorial, see our [data science tutorial](https://code.visualstudio.com/docs/datascience/data-science-tutorial).

The code in this repo aims to follow Python style guidelines as outlined in [PEP 8](https://peps.python.org/pep-0008/).

## Running the Sample

To successfully run this example, we recommend the following VS Code extensions:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) 

- Open the template folder in VS Code (**File** > **Open Folder...**)
- Create a Python virtual environment using the **Python: Create Environment** command found in the Command Palette (**View > Command Palette**). Ensure you install dependencies found in the `requirements.txt` file
- Ensure your newly created environment is selected using the **Python: Select Interpreter** command found in the Command Palette
- Run `calculations.py` using the Play Button in the top right corner or by selecting **Python > Python File in Terminal** from the context menu or Command Palette
- Run `revenue_visual.py` using the Play Button in the top right corner or by selecting **Python > Python File in Terminal** from the context menu or Command Palette to generate the bar graph visual
- To test the Python code, install `dev-requirements.txt` into your virtual environment. 
- Navigate to the Test Panel to configure your Python test or by triggering the **Python: Configure Tests** command from the Command Palette
- Run tests in the Test Panel or by clicking the Play Button next to the individual tests in the `test_calculations.py` file

