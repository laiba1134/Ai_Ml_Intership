-------------------------------------------------------------------------Task Objective--------------------------------------------------------------------------
The objective of this project is to perform "Exploratory Data Analysis (EDA)" on the Iris dataset.
This includes understanding the structure of the dataset, generating summary statistics, and visualizing relationships between features using plots.

-------------------------------------------------------------------------Dataset Used----------------------------------------------------------------------------
Dataset Name:Iris Dataset
Format: CSV ('Iris.csv')
Total Records:150
----------------------------------------------------------------------------Features-----------------------------------------------------------------------------
1) SepalLengthCm
2) SepalWidthCm
3) PetalLengthCm
4) PetalWidthCm
5) Species (Target Variable)
  
-------------------------------------------------------------------------Additional Column-----------------------------------------------------------------------
Id (removed during preprocessing not neccessary)
--------------------------------------------------------------------------Models Applied-------------------------------------------------------------------------
No machine learning models were applied in this task.
The focus of this project is strictly on "data exploration and visualization".
--------------------------------------------------------------------------Data Overview--------------------------------------------------------------------------
1) Dataset contains "150 samples" with no missing values
2) Features are numerical except for the categorical target variable ("Species")
3) Data is clean and well-structured

------------------------------------------------------------------------ Scatter Plot ---------------------------------------------------------------------------

- Clear separation observed between species based on petal dimensions
- Petal length and petal width are highly correlated

-----------------------------------------------------------------------Histograms--------------------------------------------------------------------------------
- Most features show a "normal or slightly skewed distribution"
- Petal measurements show clearer grouping compared to sepal features
-----------------------------------------------------------------------Box Plots---------------------------------------------------------------------------------
- Some minor outliers detected in sepal width
- Petal features show less variability and clearer clustering
-----------------------------------------------------------------------Conclusion--------------------------------------------------------------------------------
1) The Iris dataset is well-balanced and clean, making it ideal for analysis.
2) Feature relationships, especially petal dimensions, play a significant role in distinguishing between species.
3) This dataset is highly suitable for classification tasks, though model training was beyond the scope of this assignment.
---------------------------------------------------------------------Tools & Libraries Used----------------------------------------------------------------------
- Python
- Pandas
- Matplotlib
- Seaborn

