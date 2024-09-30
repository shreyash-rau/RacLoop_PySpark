# Heart Disease Data Preprocessing and Feature Engineering using Apache Spark

## Background
Cardiovascular diseases are among the leading causes of mortality worldwide. Early
detection and analysis of heart disease risk factors are crucial for effective treatment and prevention
strategies. The availability of large datasets with patient health records presents an opportunity to
develop predictive models that can assist in identifying high-risk individuals. However, before
applying machine learning models, it is essential to preprocess the data and engineer relevant
features to enhance the model's performance.

## Objective
The goal of this project is to preprocess and transform a dataset containing heart disease-
related variables using Apache Spark. The dataset includes attributes such as age, gender, chest pain

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
