# Sales Data Analysis Project

This project focuses on analyzing sales data using Python and Pandas to identify trends, seasonal effects, and product performance.

## Installation

Ensure you have the required dependencies installed:

```sh
pip install kagglehub[pandas-datasets]
```

## Loading the Dataset

Use the following script to load the dataset from Kaggle:

```python
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = ""

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "shantanugarg274/sales-dataset",
  file_path,
  # Provide any additional arguments like
  # sql_query or pandas_kwargs. See the
  # documentation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:", df.head())
```

