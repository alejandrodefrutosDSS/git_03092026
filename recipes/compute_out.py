import dataiku
import pandas as pd

# Create 5 rows
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 30, 35, 40, 45],
    "branch2": ["dev_2_branch"] * 5,
    "branch1": ["dev_1_branch"] * 5,
    "branch3": ["tres"] * 5
})

# Get the output Dataiku dataset
output_dataset = dataiku.Dataset("out")

# Write the DataFrame to the dataset
output_dataset.write_with_schema(df)
