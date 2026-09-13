import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ShopSense Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS - PROFESSIONAL UI
# =========================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f7f9fc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 17px;
        color: #6b7280;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 650;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .insight-box {
        padding: 15px 18px;
        border-radius: 10px;
        margin-bottom: 10px;
        background-color: white;
        border: 1px solid #e5e7eb;
    }

    .validation-box {
        padding: 16px 18px;
        border-radius: 10px;
        margin-bottom: 15px;
        background-color: white;
        border: 1px solid #e5e7eb;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">📊 ShopSense</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Advanced E-Commerce Analytics & Business Intelligence'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ Dashboard Controls")

    st.write(
        "Upload your e-commerce sales data and use the filters "
        "to explore business performance."
    )

    uploaded_file = st.file_uploader(
        "📁 Upload CSV",
        type=["csv"]
    )

    st.divider()

    st.caption(
        "ShopSense automatically cleans and validates uploaded data."
    )


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def money(value):
    return f"${value:,.2f}"


def clean_data(data):

    data = data.copy()

    # Remove completely empty rows
    data = data.dropna(how="all")

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Clean column names
    data.columns = data.columns.str.strip()

    # Required date columns
    if "Order Date" in data.columns:

        data["Order Date"] = pd.to_datetime(
            data["Order Date"],
            errors="coerce"
        )

    if "Ship Date" in data.columns:

        data["Ship Date"] = pd.to_datetime(
            data["Ship Date"],
            errors="coerce"
        )

    # Numeric columns
    numeric_columns = [
        "Sales",
        "Profit",
        "Quantity",
        "Discount",
        "Postal Code"
    ]

    for column in numeric_columns:

        if column in data.columns:

            data[column] = pd.to_numeric(
                data[column],
                errors="coerce"
            )

    # Required business fields
    critical_columns = [
        "Sales",
        "Profit",
        "Order ID",
        "Customer ID"
    ]

    data = data.dropna(
        subset=critical_columns
    )

    # Fill non-critical text columns
    text_columns = data.select_dtypes(
        include=["object"]
    ).columns

    for column in text_columns:

        data[column] = data[column].fillna(
            "Unknown"
        )

    return data


# =========================================================
# MAIN APP - NO FILE
# =========================================================

if uploaded_file is None:

    st.info(
        "👈 Upload a CSV file from the sidebar to start analyzing your data."
    )

    st.markdown(
        """
        ### 🚀 What ShopSense provides

        - 📊 Business performance KPIs
        - 📈 Sales trends
        - 🏷️ Category analysis
        - 🌍 Regional performance
        - 💸 Discount & profitability analysis
        - 👥 Customer segmentation
        - ⚠️ Loss-making product detection
        - 💡 Automatic business recommendations

        ### 📁 Supported Data

        ShopSense is designed for **e-commerce and sales transaction
        datasets** containing fields such as:

        `Order ID`, `Customer ID`, `Order Date`, `Sales`, and `Profit`.
        """
    )

    st.stop()


# =========================================================
# FILE LOADING + ERROR HANDLING
# =========================================================

try:

    df = pd.read_csv(
        uploaded_file,
        encoding="latin1"
    )

except Exception:

    st.error(
        "❌ Unable to read this CSV file."
    )

    st.warning(
        "Please make sure the uploaded file is a valid CSV file."
    )

    st.stop()


# =========================================================
# CLEAN COLUMN NAMES FOR VALIDATION
# =========================================================

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)


# =========================================================
# REQUIRED COLUMN VALIDATION
# =========================================================

required_columns = [
    "Order ID",
    "Customer ID",
    "Order Date",
    "Sales",
    "Profit"
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]


# =========================================================
# COMPATIBILITY CHECK
# =========================================================

if missing_columns:

    st.error(
        "❌ This dataset is not compatible with ShopSense."
    )

    st.markdown(
        """
        <div class="validation-box">

        <b>ShopSense is designed for e-commerce sales datasets.</b>

        <br><br>

        The uploaded CSV does not contain all required business fields.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("⚠️ Missing Required Fields")

    for column in missing_columns:

        st.write(f"❌ {column}")

    st.divider()

    st.subheader("📋 Required Dataset Structure")

    required_table = pd.DataFrame(
        {
            "Required Field": required_columns,
            "Purpose": [
                "Identify each order",
                "Identify customers",
                "Analyze sales trends",
                "Calculate revenue",
                "Calculate profitability"
            ]
        }
    )

    st.dataframe(
        required_table,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "💡 Please upload a compatible e-commerce sales CSV "
        "containing the required fields above."
    )

    st.stop()


# =========================================================
# COMPATIBILITY SUCCESS
# =========================================================

st.success(
    "✅ Dataset validated successfully — compatible with ShopSense."
)

validation_col1, validation_col2 = st.columns(2)

validation_col1.metric(
    "Required Fields Found",
    f"{len(required_columns)}/{len(required_columns)}"
)

validation_col2.metric(
    "Uploaded Columns",
    f"{len(df.columns)}"
)


# =========================================================
# AUTOMATIC DATA CLEANING
# =========================================================

original_rows = len(df)

df = clean_data(df)

cleaned_rows = len(df)

removed_rows = original_rows - cleaned_rows


# =========================================================
# CLEANING STATUS
# =========================================================

with st.expander("🧹 Data Cleaning & Validation Status"):

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Original Rows",
        f"{original_rows:,}"
    )

    col2.metric(
        "Clean Rows",
        f"{cleaned_rows:,}"
    )

    col3.metric(
        "Rows Removed",
        f"{removed_rows:,}"
    )

    if removed_rows > 0:

        st.warning(
            f"{removed_rows:,} rows were removed during automatic cleaning."
        )

    else:

        st.success(
            "Dataset passed automatic cleaning checks. ✅"
        )


# =========================================================
# FILTER SIDEBAR
# =========================================================

with st.sidebar:

    st.divider()

    st.header("🔎 Filters")

    # Date filter
    min_date = df["Order Date"].min()
    max_date = df["Order Date"].max()

    if pd.isna(min_date) or pd.isna(max_date):

        st.error(
            "❌ Valid Order Date values were not found."
        )

        st.stop()

    date_range = st.date_input(
        "📅 Order Date",
        value=(min_date.date(), max_date.date()),
        min_value=min_date.date(),
        max_value=max_date.date()
    )

    # Region filter
    if "Region" in df.columns:

        regions = sorted(
            df["Region"]
            .dropna()
            .unique()
            .tolist()
        )

        selected_regions = st.multiselect(
            "🌍 Region",
            regions,
            default=regions
        )

    else:

        selected_regions = []

    # Category filter
    if "Category" in df.columns:

        categories = sorted(
            df["Category"]
            .dropna()
            .unique()
            .tolist()
        )

        selected_categories = st.multiselect(
            "🏷️ Category",
            categories,
            default=categories
        )

    else:

        selected_categories = []

    # Segment filter
    if "Segment" in df.columns:

        segments = sorted(
            df["Segment"]
            .dropna()
            .unique()
            .tolist()
        )

        selected_segments = st.multiselect(
            "👥 Customer Segment",
            segments,
            default=segments
        )

    else:

        selected_segments = []


# =========================================================
# APPLY FILTERS
# =========================================================

filtered_df = df.copy()


# Date filter
if len(date_range) == 2:

    start_date = pd.Timestamp(
        date_range[0]
    )

    end_date = (
        pd.Timestamp(date_range[1])
        + pd.Timedelta(days=1)
    )

    filtered_df = filtered_df[
        (filtered_df["Order Date"] >= start_date)
        &
        (filtered_df["Order Date"] < end_date)
    ]


# Region filter
if "Region" in filtered_df.columns:

    if selected_regions:

        filtered_df = filtered_df[
            filtered_df["Region"].isin(
                selected_regions
            )
        ]

    else:

        filtered_df = filtered_df.iloc[0:0]


# Category filter
if "Category" in filtered_df.columns:

    if selected_categories:

        filtered_df = filtered_df[
            filtered_df["Category"].isin(
                selected_categories
            )
        ]

    else:

        filtered_df = filtered_df.iloc[0:0]


# Segment filter
if "Segment" in filtered_df.columns:

    if selected_segments:

        filtered_df = filtered_df[
            filtered_df["Segment"].isin(
                selected_segments
            )
        ]

    else:

        filtered_df = filtered_df.iloc[0:0]


# =========================================================
# FILTER RESULT
# =========================================================

if filtered_df.empty:

    st.warning(
        "⚠️ No data matches the selected filters."
    )

    st.info(
        "Try selecting a wider date range or more filter options."
    )

    st.stop()


# =========================================================
# KPI CALCULATIONS
# =========================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = filtered_df["Order ID"].nunique()

total_customers = filtered_df["Customer ID"].nunique()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0
    else 0
)


# =========================================================
# BUSINESS OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">📊 Business Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "💰 Sales",
    money(total_sales)
)

col2.metric(
    "📈 Profit",
    money(total_profit)
)

col3.metric(
    "🛒 Orders",
    f"{total_orders:,}"
)

col4.metric(
    "👥 Customers",
    f"{total_customers:,}"
)

col5.metric(
    "📊 Margin",
    f"{profit_margin:.2f}%"
)


# =========================================================
# DATA PREVIEW
# =========================================================

with st.expander("👀 View Filtered Data"):

    st.dataframe(
        filtered_df.head(100),
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# MONTHLY SALES TREND
# =========================================================

st.divider()

st.subheader("📈 Monthly Sales Trend")

monthly_sales = (
    filtered_df
    .set_index("Order Date")
    .resample("ME")["Sales"]
    .sum()
    .reset_index()
)

fig_monthly = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

fig_monthly.update_traces(
    hovertemplate=
    "<b>%{x|%b %Y}</b><br>"
    "Sales: $%{y:,.2f}"
    "<extra></extra>"
)

fig_monthly.update_layout(
    xaxis_title="Month",
    yaxis_title="Sales",
    hovermode="x unified"
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)


# =========================================================
# CATEGORY ANALYSIS
# =========================================================

st.divider()

st.subheader("🏷️ Category Sales vs Profit")

category_analysis = (
    filtered_df
    .groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)

category_chart_data = category_analysis.melt(
    id_vars="Category",
    value_vars=["Sales", "Profit"],
    var_name="Metric",
    value_name="Amount"
)

fig_category = px.bar(
    category_chart_data,
    x="Category",
    y="Amount",
    color="Metric",
    barmode="group",
    title="Category Sales vs Profit"
)

fig_category.update_traces(
    hovertemplate=
    "<b>%{x}</b><br>"
    "%{fullData.name}: $%{y:,.2f}"
    "<extra></extra>"
)

st.plotly_chart(
    fig_category,
    use_container_width=True
)


# =========================================================
# REGIONAL PERFORMANCE
# =========================================================

st.divider()

st.subheader("🌍 Regional Performance")

if "Region" in filtered_df.columns:

    region_analysis = (
        filtered_df
        .groupby("Region")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
        .reset_index()
    )

    region_chart_data = region_analysis.melt(
        id_vars="Region",
        value_vars=["Sales", "Profit"],
        var_name="Metric",
        value_name="Amount"
    )

    fig_region = px.bar(
        region_chart_data,
        x="Region",
        y="Amount",
        color="Metric",
        barmode="group",
        title="Regional Sales vs Profit"
    )

    fig_region.update_traces(
        hovertemplate=
        "<b>%{x}</b><br>"
        "%{fullData.name}: $%{y:,.2f}"
        "<extra></extra>"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )


# =========================================================
# DISCOUNT ANALYSIS
# =========================================================

st.divider()

st.subheader("💸 Discount vs Profit Margin")

discount_analysis = (
    filtered_df
    .groupby("Discount")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)

discount_analysis["Profit Margin"] = (
    discount_analysis["Profit"]
    / discount_analysis["Sales"]
    * 100
)

fig_discount = px.line(
    discount_analysis,
    x="Discount",
    y="Profit Margin",
    markers=True,
    title="Discount vs Profit Margin"
)

fig_discount.update_traces(
    hovertemplate=
    "<b>Discount: %{x:.0%}</b><br>"
    "Profit Margin: %{y:.2f}%"
    "<extra></extra>"
)

fig_discount.add_hline(
    y=0,
    line_dash="dash"
)

fig_discount.update_layout(
    xaxis_title="Discount",
    yaxis_title="Profit Margin (%)",
    hovermode="x unified"
)

st.plotly_chart(
    fig_discount,
    use_container_width=True
)


# =========================================================
# CUSTOMER SEGMENTATION
# =========================================================

st.divider()

st.subheader("👥 Customer Segmentation")

customer_analysis = (
    filtered_df
    .groupby("Customer ID")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)

sales_75 = customer_analysis["Sales"].quantile(0.75)

sales_25 = customer_analysis["Sales"].quantile(0.25)

customer_analysis["Customer Value"] = np.where(
    customer_analysis["Sales"] >= sales_75,
    "High Value",
    np.where(
        customer_analysis["Sales"] <= sales_25,
        "Low Value",
        "Regular Value"
    )
)

segment_analysis = (
    customer_analysis
    .groupby("Customer Value")
    .agg(
        Customers=("Customer ID", "count"),
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Orders", "sum")
    )
    .reset_index()
)

segment_analysis["Profit Margin"] = (
    segment_analysis["Profit"]
    / segment_analysis["Sales"]
    * 100
)

fig_segment = px.bar(
    segment_analysis,
    x="Customer Value",
    y="Sales",
    text="Customers",
    title="Sales by Customer Value Segment"
)

fig_segment.update_traces(
    hovertemplate=
    "<b>%{x}</b><br>"
    "Sales: $%{y:,.2f}<br>"
    "Customers: %{text:,}"
    "<extra></extra>"
)

st.plotly_chart(
    fig_segment,
    use_container_width=True
)


# =========================================================
# LOSS-MAKING PRODUCTS
# =========================================================

st.divider()

st.subheader("⚠️ Loss-Making Products")

loss_products = (
    filtered_df
    .groupby("Product Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)

loss_products = (
    loss_products[
        loss_products["Profit"] < 0
    ]
    .sort_values(
        "Profit",
        ascending=True
    )
    .head(10)
)

if not loss_products.empty:

    fig_loss = px.bar(
        loss_products,
        x="Profit",
        y="Product Name",
        orientation="h",
        title="Top 10 Loss-Making Products",
        custom_data=["Sales", "Quantity"]
    )

    fig_loss.update_traces(
        hovertemplate=
        "<b>%{y}</b><br>"
        "Loss: $%{x:,.2f}<br>"
        "Sales: $%{customdata[0]:,.2f}<br>"
        "Quantity: %{customdata[1]:,}"
        "<extra></extra>"
    )

    st.plotly_chart(
        fig_loss,
        use_container_width=True
    )

else:

    st.success(
        "🎉 No loss-making products found for the selected filters."
    )


# =========================================================
# AUTOMATIC BUSINESS RECOMMENDATIONS
# =========================================================

st.divider()

st.subheader("💡 Automatic Business Recommendations")

recommendations = []


# Category recommendation
category_analysis["Profit Margin"] = (
    category_analysis["Profit"]
    / category_analysis["Sales"]
    * 100
)

lowest_margin_category = (
    category_analysis
    .sort_values("Profit Margin")
    .iloc[0]
)

recommendations.append(
    f"🏷️ Review {lowest_margin_category['Category']} "
    f"category profitability. Its current profit margin is "
    f"{lowest_margin_category['Profit Margin']:.2f}%."
)


# Discount recommendation
high_discount_loss = discount_analysis[
    (discount_analysis["Discount"] >= 0.30) &
    (discount_analysis["Profit"] < 0)
]

if not high_discount_loss.empty:

    recommendations.append(
        "💸 High discounts are creating profit risk. "
        "Discount levels of 30% or above are associated "
        "with negative profit in the filtered data."
    )


# Loss product recommendation
total_loss_products = (
    filtered_df
    .groupby("Product Name")["Profit"]
    .sum()
    .lt(0)
    .sum()
)

if total_loss_products > 0:

    recommendations.append(
        f"⚠️ {total_loss_products} products are generating "
        f"negative profit. Review their pricing, discounts, "
        f"and product costs."
    )


# Customer recommendation
high_value_customers = (
    customer_analysis[
        customer_analysis["Customer Value"] == "High Value"
    ]
    .shape[0]
)

recommendations.append(
    f"👥 Focus on retaining High Value customers "
    f"({high_value_customers} customers) and use "
    f"upselling/cross-selling strategies for Regular Value customers."
)


# Display recommendations
for recommendation in recommendations:

    st.markdown(
        f'<div class="insight-box">{recommendation}</div>',
        unsafe_allow_html=True
    )


# =========================================================
# FINAL BUSINESS SUMMARY
# =========================================================

st.divider()

st.subheader("🎯 Business Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Overall Profit Margin",
    f"{profit_margin:.2f}%"
)

col2.metric(
    "Loss-Making Products",
    f"{total_loss_products:,}"
)

col3.metric(
    "High Value Customers",
    f"{high_value_customers:,}"
)

st.divider()

st.success(
    "🚀 ShopSense converts raw e-commerce data into "
    "actionable business decisions."
)

st.caption(
    f"Showing {len(filtered_df):,} filtered records from "
    f"{len(df):,} cleaned records."
)