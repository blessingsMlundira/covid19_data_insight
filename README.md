# COVID-19 Data Analysis with Python Flask and MongoDB

This project is a web application built with Python Flask that reads COVID-19 data, stores it in a MongoDB database, and performs data analysis to generate insights. The application also provides visualizations for the analyzed data.


## Features

- Read COVID-19 data from various sources.
- Store the data in a MongoDB database.
- Perform data analysis to generate insights.
- Provide visualizations for the analyzed data.
- Expose a REST API for interacting with the data.

## Requirements

- Python 3.8+
- Flask 2.0+
- MongoDB
- Git
- [GitHub CLI](https://cli.github.com/) (for repository management)
- Additional Python libraries:
  - pandas
  - pymongo
  - matplotlib
  - seaborn
  - dnspython

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/blessingsMlundira/covid19_data_insight.git
    cd <repository-name>
    ```

2. **Create a virtual environment and activate it**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up MongoDB**:

    - Ensure MongoDB is installed and running.
    - Create a MongoDB database and collection for storing COVID-19 data.

5. **Configure your connection to MongoDB**:

    Update the `config.py` file with your MongoDB connection details.

## Usage

1. **Run the Flask application**:

    ```sh
    flask run
    ```

2. **Access the application**:

    Open your web browser and go to `http://127.0.0.1:5000`.


## Data Analysis

The application performs various analyses on the COVID-19 data, including:

- Basic statistics (mean, median, mode, etc.).
- Distribution of test results.
- Hospitalization and recovery rates.
- Age distribution of patients.
- Correlation analysis between different features.

## Visualization

The application provides visualizations for the analyzed data, including:

- Age distribution histogram.
- Test results distribution pie chart.
- Time series analysis of positive cases.
- Correlation matrix heatmap.
- Hospitalization and recovery rates by gender bar charts.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.


## Contact

For any questions or inquiries, please contact:

- **Name**: Blessings Mlundira
- **Email**: blessingsmlundira@gmail.com
- **Website**: [tinyurl.com/B-Mlundira](https://tinyurl.com/B-Mlundira)


