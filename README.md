# Heart Disease Prediction Using PySpark

## Project Overview

This project utilizes Apache Spark's PySpark library to analyze and predict heart disease based on several clinical parameters. The project processes data, builds a logistic regression model, and evaluates its predictive accuracy, focusing on a dataset containing various heart disease indicators.

## Notebook Workflow

### Data Loading and Initial Exploration
- **Install and Import Libraries**: Set up the environment with necessary libraries including PySpark and MLlib.
- **Initialize Spark Session**: Begin a session to process the data using Spark.
- **Data Loading**: Load heart disease data from a CSV file.

### Data Preprocessing
- **Handling Missing Values**: Identify and remove records with missing data represented by "?".
- **Feature Recoding**: Convert categorical data into more readable forms, e.g., changing binary codes to gender identifiers.
- **Feature Engineering**: Create new binary columns to clearly represent clinical data states.

### Descriptive Statistics
- **Summary Statistics**: Provide count, mean, standard deviation, min, and max for each numerical feature.
- **Grouped Statistics**: Calculate and display statistics by categories, such as by disease presence or sex.

### Data Analysis
- **Correlation and Categorical Analysis**: Use cross-tabulation to explore relationships between different features.
- **Aggregation**: Compute averages and other statistics grouped by disease presence.

### Predictive Modeling
- **Data Transformation**: Convert all categorical data into numerical indices.
- **Feature Vector Creation**: Assemble features into a single vector as required by MLlib.
- **Model Training**: Split data into training and test sets, then train a logistic regression model.
- **Model Evaluation**: Predict on the test set and evaluate predictions using accuracy and a confusion matrix.

## Contributing

Contributions to this project are welcome. Please adhere to the following steps for contributing:

1. Fork the repository.
2. Create a new feature branch (git checkout -b new-feature).
3. Commit your changes (git commit -am 'Add some feature').
4. Push the branch (git push origin new-feature).
5. Create a new Pull Request.
