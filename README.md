📊 ShopSense – Advanced E-Commerce Analytics

ShopSense is a portfolio-grade e-commerce analytics application that converts raw sales data into actionable business insights.

Users can upload a CSV file and automatically perform data cleaning, KPI analysis, sales trend analysis, customer segmentation, profitability analysis, loss-making product detection, and business recommendations without writing Python code.

---

## 🚀 Project Overview

Businesses often have large amounts of sales data but struggle to convert that data into useful decisions.

ShopSense solves this problem by transforming raw e-commerce transaction data into an interactive analytics dashboard.

### Business Flow

Raw CSV Data  
↓  
Automatic Data Cleaning  
↓  
Data Validation  
↓  
Business KPIs  
↓  
Sales & Profit Analysis  
↓  
Customer Segmentation  
↓  
Loss-Making Product Detection  
↓  
Business Recommendations

---

## ✨ Key Features

### 📁 CSV Data Upload

Users can upload their own e-commerce sales CSV file directly through the dashboard.

### 🧹 Automatic Data Cleaning

ShopSense automatically handles:

- Duplicate rows
- Empty rows
- Invalid dates
- Numeric data conversion
- Missing critical values
- Missing text values
- Required-column validation

### 📊 Business KPIs

The dashboard provides:

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Overall Profit Margin

### 📈 Monthly Sales Trend

Analyze sales performance over time and identify:

- Growth periods
- Seasonal trends
- High-performing months
- Low-performing months

### 🏷️ Category Analysis

Compare sales and profit across product categories to identify profitable and low-margin categories.

### 🌍 Regional Performance

Analyze sales and profitability across different regions.

### 💸 Discount & Profitability Analysis

Understand the relationship between discount levels and profit margins.

This helps identify discount levels that may create profitability risks.

### 👥 Customer Segmentation

Customers are automatically divided into:

- High Value
- Regular Value
- Low Value

The segmentation is based on customer sales performance.

### ⚠️ Loss-Making Products

ShopSense identifies products generating negative profit and highlights the top loss-making products.

### 💡 Automatic Business Recommendations

The application converts analytics into actionable recommendations.

Examples:

- Review low-margin categories and evaluate their pricing strategy.
- High discounts are associated with negative profit and should be reviewed.
- Loss-making products should be evaluated for pricing, discounting, and cost issues.
- High-value customers should be prioritized for retention and cross-selling.

### 🔎 Interactive Filters

Users can dynamically filter the dashboard by:

- Date
- Region
- Category
- Customer Segment

All major KPIs and visualizations update according to the selected filters.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analytics |
| Pandas | Data cleaning and analysis |
| NumPy | Numerical operations |
| Plotly | Interactive visualizations |
| Streamlit | Interactive dashboard |
| Matplotlib | Data visualization |
| Jupyter Notebook | Analysis and development |
| GitHub | Version control and project hosting |

---

## 📂 Project Structure

```text
ShopSense-Analytics/
│
├── data/
│   ├── raw/
│   │   └── Sample - Superstore.csv
│   │
│   └── processed/
│
├── notebooks/
│   └── ShopSense_Analytics.ipynb
│
├── dashboard/
│   └── app.py
│
├── sql/
│
├── image/
│
├── README.md
│
└── requirements.txt
📊 Dataset

The project uses the Sample Superstore dataset containing e-commerce transaction information such as:

Order Date
Ship Date
Customer
Region
Category
Sub-Category
Product
Sales
Quantity
Discount
Profit

The dataset contains approximately 10,000 transaction records.

📌 Key Business Insights
1. Furniture Has a Low Profit Margin

Furniture generates significant sales but has a much lower profit margin compared with Technology and Office Supplies.

This indicates a potential pricing, discount, or cost-management issue.

2. High Discounts Create Profit Risk

Higher discount levels are associated with negative profit margins in the dataset.

Therefore, businesses should carefully evaluate large discounts before applying them broadly.

Note: This analysis identifies an association between discount and profitability; it does not prove that discounts alone cause losses.

3. Loss-Making Products Need Attention

A significant number of products generate negative aggregate profit.

These products should be reviewed for:

Pricing
Discounts
Product costs
Shipping costs
Sales strategy
4. High-Value Customers Drive Revenue

A relatively small group of high-value customers contributes a substantial portion of overall sales.

Businesses can focus on:

Customer retention
Personalized offers
Cross-selling
Upselling
🎯 Business Value

ShopSense is designed to answer practical business questions such as:

How much revenue are we generating?
How profitable are our sales?
Which categories perform best?
Which regions are strongest?
Are discounts hurting profitability?
Which customers are most valuable?
Which products are generating losses?
What actions should the business consider?

The goal is not simply to display charts.

ShopSense turns raw e-commerce data into actionable business decisions.

▶️ How to Run the Project
1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Open the Project
cd ShopSense-Analytics
3. Install Dependencies
pip install -r requirements.txt
4. Run the Dashboard
cd dashboard
streamlit run app.py
5. Open the Application

Streamlit will provide a local URL similar to:

http://localhost:8501

Open it in your browser.

6. Upload Your CSV

Upload a compatible e-commerce sales CSV and start exploring the dashboard.

📷 Dashboard Preview

Screenshots of the ShopSense dashboard will be added here.

Business Overview

Add dashboard screenshot here.

Sales & Profit Analysis

Add dashboard screenshot here.

Customer Segmentation

Add dashboard screenshot here.

Business Recommendations

Add dashboard screenshot here.

🔮 Future Improvements

Planned improvements include:

Advanced RFM customer segmentation
Product-level profitability analysis
Sales forecasting
Automated report generation
Downloadable business reports
More advanced dashboard filters
Machine learning-based customer insights
Deployment using Streamlit Cloud
Database integration
👨‍💻 Project Purpose

This project was developed as a practical Data Analytics portfolio project to demonstrate skills in:

Data Cleaning
Exploratory Data Analysis
Business Analytics
Data Visualization
Customer Segmentation
Profitability Analysis
Python
SQL
Streamlit
Business Intelligence
⭐ Project Highlight

ShopSense – Advanced E-Commerce Analytics

Upload data → Automatically clean it → Analyze performance → Identify business problems → Generate actionable recommendations.

📜 License

This project is created for educational and portfolio purposes.