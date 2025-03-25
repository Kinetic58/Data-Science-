<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Game Sales Data Analysis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2, h3 {
            color: #444;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        a {
            color: #0077cc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<h1>Video Game Sales Data Analysis</h1>

<h2>Project Overview</h2>
<p>
    This project focuses on analyzing video game sales data from 1980 to 2020. The goal is to explore how player preferences have changed over time, which platforms and genres were the most popular, and how sales were distributed across different regions. These insights can be useful for understanding the gaming market and predicting trends.
</p>

<h2>Libraries Used</h2>
<p>
    The following libraries were used for data analysis and visualization:
</p>
<ul>
    <li><strong>Pandas</strong> - for loading, preprocessing, and analyzing data.</li>
    <li><strong>Matplotlib</strong> & <strong>Seaborn</strong> - for creating visualizations.</li>
    <li><strong>OS</strong> - for handling directories and saving charts.</li>
</ul>

<h2>How to Run the Analysis</h2>
<ol>
    <li>
        <strong>Install required libraries</strong>:
        If the libraries are not installed, run the following command:
        <pre><code>pip install pandas matplotlib seaborn</code></pre>
    </li>
    <li>
        <strong>Download the dataset</strong>:
        The dataset can be downloaded from <a href="https://www.kaggle.com/datasets/gregorut/videogamesales" target="_blank">Kaggle</a> or use the <code>vgsales.csv</code> file from the repository.
    </li>
    <li>
        <strong>Run the script</strong>:
        The <code>analysis_script.py</code> contains the code for analyzing data and generating charts. Run it using:
        <pre><code>python analysis_script.py</code></pre>
    </li>
    <li>
        <strong>Results</strong>:
        After execution, the following charts will be saved in the <code>charts</code> folder:
        <ul>
            <li><code>sales_by_year.png</code> - Sales trend over the years.</li>
            <li><code>top_platforms.png</code> - Top 10 gaming platforms by number of games.</li>
            <li><code>sales_by_region.png</code> - Sales distribution by region.</li>
        </ul>
    </li>
</ol>

<h2>Steps in the Analysis</h2>
<ol>
    <li>
        <strong>Data Loading</strong>:
        The dataset is loaded from a CSV file using Pandas.
    </li>
    <li>
        <strong>Data Preprocessing</strong>:
        <ul>
            <li>Removed rows with missing values.</li>
            <li>Converted the <code>Year</code> column to numeric format.</li>
        </ul>
    </li>
    <li>
        <strong>Data Analysis</strong>:
        <ul>
            <li>Calculated total sales per year.</li>
            <li>Identified the top 10 platforms by game count.</li>
            <li>Analyzed sales distribution across regions.</li>
        </ul>
    </li>
    <li>
        <strong>Data Visualization</strong>:
        <ul>
            <li>Created a line chart for sales trends.</li>
            <li>Plotted a bar chart for the top 10 platforms.</li>
            <li>Designed a pie chart for sales distribution by region.</li>
        </ul>
    </li>
</ol>

<h2>Key Findings</h2>
<p>
    The analysis led to the following insights:
</p>
<ul>
    <li>Video game sales peaked in the mid-2000s.</li>
    <li>PS2 and DS were the most popular gaming platforms.</li>
    <li>North America and Europe had the highest sales volume.</li>
</ul>

<h2>References</h2>
<ul>
    <li><a href="https://www.kaggle.com/datasets/gregorut/videogamesales" target="_blank">Dataset on Kaggle</a></li>
    <li><a href="https://pandas.pydata.org/" target="_blank">Pandas Documentation</a></li>
    <li><a href="https://matplotlib.org/" target="_blank">Matplotlib Documentation</a></li>
    <li><a href="https://seaborn.pydata.org/" target="_blank">Seaborn Documentation</a></li>
</ul>

</body>
</html>
