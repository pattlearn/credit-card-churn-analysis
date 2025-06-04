# Credit Card Churn Analysis

<p>
    The background story is that the bank is losing customers over time. It may not be a large number initially, but if the issue is left unresolved by management, it could become more difficult to recover. The objective is to identify the parameters that influence the churn rate so that the bank can develop effective solutions to retain customers.
</p>
<p>
This data is from <a href="https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers/data">Kaggle</a>.
</p>

## Code

<p>
    <ol>
        <li>
            <a href="/src/credit_card.ipynb">credit_card.ipynb</a>: This notebook focuses on the data analytics part, with most of the code dedicated to data transformation and data visualization.
        </li>
        <li>
            <a href="/src/credit_card_prediction.ipynb">credit_card_prediction.ipynb</a>: This notebook uses logistic regression to predict churn rates.
        </li>
    </ol>
</p>

## Installation

<p>
Librarie used
    <ul>
        <li><b>pandas</b>: used for data manipulation and analysis, including cleaning, filtering and transformation data.</li>
        <li><b>matplotlib</b>: A library for creating chart, graph and visualize distruibution and trends in the data.</li>
        <li><b>seaborn</b>: A visualization library built on top of Matplotlib for aesthetic and comprehensive data visualization.</li>
        <li><b>sklearn</b>: A ready-to-use machine learning library that provides tool for model building, evaluating and data processing.</li>
    </ul>
</p>

```batch
pip install pandas matplotlib seaborn sklearn
```

## Summary Presentation

If you're looking for a summary of the findings, insights, and analysis, you may refer to the presentation slides. The presentation is divided into two main parts:
<a href="https://docs.google.com/presentation/d/1z8VOXR8o1OScPQxC-3AWKz9u9brPKDSnegfeVpiMrp4/edit?usp=sharing">Please click here to view the slide.</a>

#### Exploratory Data Analysis (EDA):

This section focuses on understanding the dataset through visualizations and descriptive statistics. It includes the identification of trends, patterns, and potential factors influencing churn. This part spans pages 1 to 10.

#### Churn Prediction:

This section applies logistic regression to predict customer churn based on selected features. Four candidate models are compared, and the most viable model is highlighted based on performance metrics. This part is covered on pages 11 to 13.
