import streamlit as st
import pandas as pd
import plotly.express as px

# combined_pricing_v1.csv

# Load your data
df = pd.read_csv(r"fragance_it_keepa.csv")
df1 = pd.read_csv(r"combined_pricing_v1.csv")
df.columns = [col.replace("🚚", "").strip() for col in df.columns]

# Add Introduction
st.markdown("""
<h1>Brand and Category Performance Dashboard</h1>
<p>Welcome to the Brand and Category Performance Dashboard. This tool provides an in-depth analysis of brand performance, pricing trends, and category popularity. This data dashboard is based on <b>Italy location.</b> Utilize this dashboard to gain valuable insights and refine your strategy.</p>
""", unsafe_allow_html=True)

# Sidebar header
st.sidebar.title('Table of Contents')

# Table of Contents list
st.sidebar.markdown("""
- **[Overview](#overview)**
- **[Brand Performance](#brand-performance)**
- **[Statistical Summary](#statistical-summary)**
- **[Price Drop Analysis](#price-drop-analysis)**
- **[Category Insights](#category-insights)**
- **[Customer Reviews](#customer-reviews)**
- **[Contact](#contact)**
""")

# Overview
st.markdown("<a id='overview'></a><h2>1. Overview</h2>", unsafe_allow_html=True)
st.markdown("""
<p>This section provides an initial overview of the dataset, including key elements such as product identifiers, sales data, and pricing metrics. Understanding these fundamentals will help guide the subsequent analyses.</p>
""", unsafe_allow_html=True)
# Initial Observations
st.markdown("""
<p>We start by examining the key aspects of the data:</p>
<ul>
    <li><b>Product Identification:</b> Unique identifiers like ASIN, EAN, and PartNumber.</li>
    <li><b>Product Details:</b> Product attributes such as Title, Brand, and Image.</li>
    <li><b>Sales Data:</b> Sales ranks and their changes over time.</li>
    <li><b>Pricing Data:</b> Current Buy Box prices and price changes over various periods.</li>
    <li><b>Category:</b> Main, Sub, and Tree categories.</li>
</ul>
""", unsafe_allow_html=True)



# Data Cleaning
numeric_columns = [
    'Sales Rank: 90 days avg.', 'Sales Rank: 30 days avg.',
    'Buy Box : Current', 'Buy Box : 90 days avg.',
    'Buy Box : 1 day drop %', 'Buy Box : 7 days drop %',
    'Buy Box : 30 days drop %', 'Buy Box : 90 days drop %',
    'Referral Fee %', 'Item: Dimension (cm³)', 'Item: Weight (g)'
]

# Remove non-numeric characters and convert to float
for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col].replace('[^\d.]', '', regex=True), errors='coerce')

data_cleaned = df.dropna(subset=['Brand'])

# Brand Performance
st.markdown("<a id='brand-performance'></a><h2>2. Brand Performance</h2>", unsafe_allow_html=True)

# Top 10 Brands by Average Current Buy Box Price
buy_box_column = 'Buy Box : Current'
if buy_box_column not in data_cleaned.columns:
    st.error(f"Column '{buy_box_column}' not found in the data.")
else:
    average_price_by_brand = data_cleaned.groupby('Brand')[buy_box_column].mean().sort_values(ascending=False).head(10)
    average_price_by_brand_df = average_price_by_brand.reset_index()
    average_price_by_brand_df.columns = ['Brand', 'Average Current Buy Box Price']
    
    st.header('Top 10 Brands by Average Current Buy Box Price')
    fig = px.bar(average_price_by_brand_df, x='Brand', y='Average Current Buy Box Price', 
                 title='Top 10 Brands by Average Current Buy Box Price',
                 labels={'Average Current Buy Box Price': 'Average Current Buy Box Price (€)'})
    st.plotly_chart(fig, use_container_width=True)

# Premium and Luxury Branding
st.subheader("Premium and Luxury Branding")
st.write(
    "**Brands:** La Mer (€239.43), Penhaligon's (€212.29), La Prairie (€144.00)"
)
st.write(
    "**Insight:** These brands have the highest average prices, indicating a strong premium market position. "
    "They cater to customers seeking luxury and exclusivity."
)
st.write(
    "**Strategy:** Maintain premium pricing to reinforce brand prestige. Consider exclusive promotions or limited editions to enhance their luxury appeal."
)

# Competitive Mid-Range Pricing
st.subheader("Competitive Mid-Range Pricing")
st.write(
    "**Brands:** Loewe (€96.51), Tom Ford (€90.83), Helena Rubinstein (€85.90), Guerlain (€74.91)"
)
st.write(
    "**Insight:** These brands are priced in the mid-range, balancing premium features with accessibility. They attract a wide customer base by offering a mix of quality and value."
)
st.write(
    "**Strategy:** Utilize competitive pricing to appeal to a broad audience. Differentiate through superior product quality and brand experience."
)

# Value-Oriented Pricing
st.subheader("Value-Oriented Pricing")
st.write(
    "**Brands:** BVLGARI (€72.70), Chanel (€65.90), Tiffany (€63.70)"
)
st.write(
    "**Insight:** Positioned as value-oriented but still aspirational, these brands offer quality at more accessible prices. They target consumers looking for premium features without the highest price tag."
)
st.write(
    "**Strategy:** Highlight the quality and heritage of these brands in marketing. Ensure pricing reflects the value proposition and remains competitive in the market."
)

# Price Range Dynamics
st.subheader("Price Range Dynamics")
st.write(
    "**Range:** €63.70 (Tiffany) to €239.43 (La Mer)"
)
st.write(
    "**Insight:** The broad price range reflects a diverse market with varying customer segments. High-priced brands cater to luxury consumers, while lower-priced brands appeal to those seeking value."
)
st.write(
    "**Strategy:** Develop tailored pricing strategies for different segments. Focus on exclusivity for higher-priced brands and emphasize value for more accessible options."
)

# Summary
st.subheader("Summary")
st.write(
    "1. **Premium Brands:** Reinforce luxury positioning with high prices and exclusive offers."
)
st.write(
    "2. **Mid-Range Brands:** Attract a wider audience with competitive pricing and high quality."
)
st.write(
    "3. **Value Brands:** Offer accessible luxury with a focus on quality and brand heritage."
)
st.write(
    "4. **Overall:** Regularly review and adjust pricing to align with market dynamics and maintain optimal positioning."
)


# Top 10 Brands by Average Sales Rank (90 days avg.)
top_brands_sales_rank = data_cleaned.groupby('Brand')['Sales Rank: 90 days avg.'].mean().sort_values().head(10)
top_brands_sales_rank = top_brands_sales_rank.round(2)
top_brands_sales_rank_df = top_brands_sales_rank.reset_index()
top_brands_sales_rank_df.columns = ['Brand', 'Avg. Sales Rank (90 days avg.)']

st.header('Top 10 Brands by Average Sales Rank (90 days avg.)')
fig = px.bar(top_brands_sales_rank_df, x='Brand', y='Avg. Sales Rank (90 days avg.)', 
             title='Top 10 Brands by Average Sales Rank (90 days avg.)',
             labels={'Avg. Sales Rank (90 days avg.)': 'Average Sales Rank (90 days avg.)'})
st.plotly_chart(fig, use_container_width=True)

# Sales Rank Insights
st.subheader("Sales Rank Insights")

# High Sales Performance
st.write("### High Sales Performance")
st.write(
    "**Top Performers:** BVLGARI (€53,700.50), Valentino (€41,021.50), Prada (€24,965.33)"
)
st.write(
    "**Insight:** These brands have the lowest average sales ranks, indicating they are top performers with strong sales and high customer engagement."
)
st.write(
    "**Strategy:** Maintain and build on successful sales strategies. Explore expanding product lines and increasing marketing efforts to sustain or enhance market dominance."
)

# Mid-Range Sales Performance
st.write("### Mid-Range Sales Performance")
st.write(
    "**Brands:** Guerlain (€76,867.50), GIORGIO ARMANI (€75,474.50), Tiffany (€69,457.00)"
)
st.write(
    "**Insight:** These brands have moderate sales ranks, showing competitive performance but facing more competition."
)
st.write(
    "**Strategy:** Analyze the competitive landscape and identify ways to improve sales ranks. Enhance product differentiation and customer engagement to strengthen market position."
)

# Lower Sales Performance
st.write("### Lower Sales Performance")
st.write(
    "**Brands:** Carolina Herrera (€107,276.00), PETZL (€97,427.50), Versace (€87,774.50), Tom Ford (€86,000.20)"
)
st.write(
    "**Insight:** These brands have higher average sales ranks, suggesting weaker performance compared to others."
)
st.write(
    "**Strategy:** Investigate the causes of lower sales. Implement targeted marketing, improve product offerings, adjust pricing, and consider promotions to boost visibility and sales."
)

# Summary of Recommendations
st.write("### Summary of Recommendations")
st.write(
    "1. **Leverage High Performance:** For top-performing brands, continue optimizing successful strategies and explore expansion opportunities."
)
st.write(
    "2. **Enhance Competitive Positioning:** For mid-range brands, focus on improving strategies and customer engagement to gain a competitive edge."
)
st.write(
    "3. **Address Sales Challenges:** For lower-performing brands, identify areas for improvement and implement targeted actions to enhance sales and visibility. Regularly monitor and adjust strategies as needed."
)

# Statistical Summary
st.markdown("<a id='statistical-summary'></a><h2>4. Statistical Summary</h2>", unsafe_allow_html=True)

# Calculate Summary Statistics
def calculate_summary_statistics(series):
    return {
        'Min': series.min(),
        'Q1': series.quantile(0.25),
        'Median': series.median(),
        'Q3': series.quantile(0.75),
        'Max': series.max(),
        'Mean': series.mean(),
        'Mode': series.mode()[0] if not series.mode().empty else None,
        'Variance': series.var(),
        'Standard Deviation': series.std()
    }

# Apply the calculation for each column
summary_stats = {}
for col in numeric_columns:
    if col in data_cleaned.columns:
        summary_stats[col] = calculate_summary_statistics(data_cleaned[col].dropna())

# Create DataFrame for summary stats
stats_df = pd.DataFrame(summary_stats).T
stats_df.columns = ['Min', 'Q1', 'Median', 'Q3', 'Max', 'Mean', 'Mode', 'Variance', 'Standard Deviation']

# Display the statistical summary
st.write("### Detailed Statistical Summary of Key Metrics:")
# st.dataframe(stats_df)

# # Optional: Format numbers for better readability
# st.write("### Formatted Statistical Summary:")
stats_df_formatted = stats_df.applymap(lambda x: f"{x:,.2f}" if isinstance(x, (int, float)) else x)
st.dataframe(stats_df_formatted)

# Business Insights
st.markdown("<h2>Business Insights</h2>", unsafe_allow_html=True)

# Section: Buy Box Price Drops
# Sales Insights
st.header("Sales Insights")

# 1. Buy Box Price Drops
st.subheader("1. Buy Box Price Drops")
st.write(
    "**Short-Term Drops:** Median percentage drops are 0.00% for 1 day, 7 days, and 30 days, rising to 3.00% for 90 days. Maximum recorded drop is 26.00%."
)
st.write(
    "**Implication:** Minor daily or weekly fluctuations are typical, but substantial drops over longer periods may indicate seasonal sales or inventory clearances. Regular monitoring and price adjustments can help optimize profitability and stay competitive."
)

# 2. Referral Fee %
st.subheader("2. Referral Fee %")
st.write(
    "**Consistency:** Median referral fee percentage is 15.45%, with a maximum of 15.46%."
)
st.write(
    "**Implication:** The stable referral fee allows for predictable cost planning. Ensure product pricing accounts for this fee while staying competitive."
)

# 3. Buy Box Prices
st.subheader("3. Buy Box Prices")
st.write(
    "**Current Prices:** Median Buy Box price is €47.63, ranging up to €299.00."
)
st.write(
    "**Historical Trends:** Prices have remained stable over 30 and 90 days, indicating steady pricing trends."
)
st.write(
    "**Implication:** Compare current prices to historical averages to guide pricing adjustments. Competitive pricing enhances visibility and sales."
)

# 4. Sales Rank
st.subheader("4. Sales Rank")
st.write(
    "**Trends:** Median sales rank is 85,315 for 30 days and 132,678 for 90 days, with significant variability."
)
st.write(
    "**Implication:** Target products with improving sales ranks for promotional strategies. For products with lower ranks, analyze performance factors and adjust marketing strategies."
)

# Summary of Recommendations
st.subheader("Summary of Recommendations")
st.write(
    "1. **Price Management:** Regularly review and adjust pricing based on observed drops and historical trends."
)
st.write(
    "2. **Cost Management:** Factor in the stable referral fee percentage to ensure costs are covered while maintaining competitiveness."
)
st.write(
    "3. **Performance Monitoring:** Use sales rank data to identify and promote high-performing products. Adjust strategies for products with lower sales ranks."
)
st.write(
    "4. **Logistics Optimization:** Adapt logistics and inventory management to efficiently handle diverse product dimensions and weights."
)




# Price Drop Analysis
st.markdown("<a id='price-drop-analysis'></a><h2>5. Price Drop Analysis</h2>", unsafe_allow_html=True)

top_brands_price_drop = data_cleaned.groupby('Brand')['Buy Box : 30 days drop %'].mean().sort_values(ascending=False)
top_brands_price_drop = top_brands_price_drop.round(2)
top_brands_price_drop_df = top_brands_price_drop.reset_index()
top_brands_price_drop_df.columns = ['Brand', 'Average Price Drop (30 days)']

st.subheader('Top 10 Brands by Average Price Drop (30 days)')
fig = px.bar(top_brands_price_drop_df, x='Brand', y='Average Price Drop (30 days)', 
             title='Top 10 Brands by Average Price Drop (30 days)',
             labels={'Average Price Drop (30 days)': 'Average Price Drop (30 days) (%)'})
st.plotly_chart(fig, use_container_width=True)

# Average Price Drop Insights (30 Days)
st.header("Average Price Drop Insights (30 Days)")

# No Price Drop
st.subheader("No Price Drop")
st.write(
    "**Brands:** La Prairie, GIORGIO ARMANI, La Mer, ON"
)
st.write(
    "**Insight:** These brands have not experienced any average price drop in the past 30 days, reflecting stable pricing strategies and strong market positioning."
)
st.write(
    "**Actionable Strategy:** Continue maintaining stable prices to uphold brand value and customer trust. Stay vigilant for any market changes that might require price adjustments."
)

# Low Price Drop
st.subheader("Low Price Drop")
st.write(
    "**Brands:** Prada (0.33%), Valentino (0.75%), Tiffany (1.00%), Penhaligon's (1.00%), Loewe (1.00%)"
)
st.write(
    "**Insight:** These brands show minimal price drops, indicating cautious pricing adjustments and stable market positioning."
)
st.write(
    "**Actionable Strategy:** Monitor market trends and competitive pricing closely. Implement incremental price adjustments if necessary to remain competitive while preserving brand value."
)

# Moderate Price Drop
st.subheader("Moderate Price Drop")
st.write(
    "**Brands:** Dior (1.33%), Chanel (1.90%), PETZL (2.00%), ZWILLING (2.00%), Helena Rubinstein (2.00%), Guerlain (2.00%), Biotherm (2.00%)"
)
st.write(
    "**Insight:** These brands have experienced moderate price drops, possibly in response to market pressures or inventory management."
)
st.write(
    "**Actionable Strategy:** Investigate the reasons for these moderate drops and adjust pricing strategies to balance competitiveness with profitability. Address any market dynamics affecting pricing."
)

# Significant Price Drop
st.subheader("Significant Price Drop")
st.write(
    "**Brands:** Carolina Herrera (3.00%), Tom Ford (5.20%), Versace (7.50%), BVLGARI (8.50%)"
)
st.write(
    "**Insight:** Significant price drops may indicate aggressive pricing strategies, inventory clearance, or competitive responses."
)
st.write(
    "**Actionable Strategy:** Review pricing strategies to understand the causes of substantial drops. Evaluate inventory levels, market competition, and consumer demand to optimize pricing effectively."
)

# Summary of Recommendations
st.subheader("Summary of Recommendations")
st.write(
    "1. **Maintain Stability:** For brands with no price drop, continue to monitor the market to ensure prices align with market conditions and brand positioning."
)
st.write(
    "2. **Monitor and Adjust Incrementally:** For brands with low price drops, make small adjustments as needed while focusing on maintaining brand value and competitive positioning."
)
st.write(
    "3. **Analyze and Adapt Moderately:** For brands with moderate price drops, analyze market trends and adjust pricing strategies to ensure competitiveness while managing profitability."
)
st.write(
    "4. **Strategic Review for Significant Drops:** For brands with significant price drops, conduct a thorough review of pricing strategies and market dynamics to address underlying issues and optimize pricing."
)



# Category Insights
st.markdown("<a id='category-insights'></a><h2>6. Category Insights</h2>", unsafe_allow_html=True)

# Pie chart for Root Categories
popular_categories_root = data_cleaned['Categories: Root'].value_counts().head(10)
popular_categories_root_df = popular_categories_root.reset_index()
popular_categories_root_df.columns = ['Category', 'Count']

fig_root = px.pie(popular_categories_root_df, names='Category', values='Count', title='Top 10 Popular Root Categories')
st.plotly_chart(fig_root, use_container_width=True)

# Pie chart for Subcategories
popular_categories_sub = data_cleaned['Categories: Sub'].value_counts().head(10)
popular_categories_sub_df = popular_categories_sub.reset_index()
popular_categories_sub_df.columns = ['Subcategory', 'Count']

fig_sub = px.pie(popular_categories_sub_df, names='Subcategory', values='Count', title='Top 10 Popular Subcategories')
st.plotly_chart(fig_sub, use_container_width=True)

# Calculate category-wise sales performance
category_sales_performance = data_cleaned.groupby('Categories: Root')['Sales Rank: 90 days avg.'].mean().sort_values(ascending=False)

# Round to two decimal places and format as currency
category_sales_performance = category_sales_performance.round(2).apply(lambda x: f'€{x:.2f}')

# Convert Series to DataFrame
category_sales_performance_df = category_sales_performance.reset_index()
category_sales_performance_df.columns = ['Main Category', 'Avg. Sales Rank (90 days avg.)']

# Streamlit app
st.title('Category-Wise Sales Performance')

# Display the data frame
# st.write("### Average Sales Rank by Category")
# st.dataframe(category_sales_performance_df)

# Plotly chart
fig = px.bar(
    category_sales_performance_df,
    x='Main Category',
    y='Avg. Sales Rank (90 days avg.)',
    title='Average Sales Rank by Category',
    labels={'Avg. Sales Rank (90 days avg.)': 'Average Sales Rank (€)'},
    text='Avg. Sales Rank (90 days avg.)',
    color='Avg. Sales Rank (90 days avg.)',
    color_continuous_scale=px.colors.sequential.Plasma
)

fig.update_layout(
    xaxis_title='Main Category',
    yaxis_title='Average Sales Rank (€)',
    xaxis_tickangle=-45,
    width=800,
    height=600
)

# Display the plot
st.plotly_chart(fig, use_container_width=True)

# High Sales Volume Categories
st.header("Sales Insights by Category")

st.subheader("High Sales Volume Categories")

# Casa e Cucina
st.write(
    "**Casa e Cucina (€453,215.00)**"
)
st.write(
    "**Insight:** This category exhibits the highest average sales volume, reflecting significant consumer demand and market success in home and kitchen products. The substantial revenue indicates that products in this category are performing exceptionally well."
)
st.write(
    "**Actionable Strategy:** To capitalize on this strong performance, focus on amplifying marketing efforts and increasing inventory in this category. Explore opportunities to introduce new or premium products to sustain and further enhance sales."
)

# Giochi e Giocattoli
st.write(
    "**Giochi e Giocattoli (€422,243.00)**"
)
st.write(
    "**Insight:** Toys and games also show a high sales volume, indicating robust consumer interest and a substantial revenue contribution. The strong performance suggests that this category is a major revenue driver."
)
st.write(
    "**Actionable Strategy:** Leverage seasonal trends with targeted promotions and marketing campaigns. Stay updated with the latest trends in toys and games to maintain a competitive edge and maximize revenue."
)

st.subheader("Moderate Sales Volume Categories")

# Moda
st.write(
    "**Moda (€105,114.50)**"
)
st.write(
    "**Insight:** Fashion products show a moderate sales volume, indicating steady performance but not as strong as the top categories. This suggests consistent consumer interest but with potential for growth."
)
st.write(
    "**Actionable Strategy:** Enhance sales through collaborations with fashion influencers and by offering limited-time promotions. Focus on popular and trending fashion items to boost market presence."
)

# Bellezza
st.write(
    "**Bellezza (€90,656.90)**"
)
st.write(
    "**Insight:** Beauty products have a solid sales volume, indicating healthy demand, though not as high as the leading categories. This reflects a steady but not dominant position in the market."
)
st.write(
    "**Actionable Strategy:** Increase marketing efforts and expand the product line to include new trends in beauty. Develop customer loyalty programs and encourage product reviews to drive additional sales."
)

# Salute e Cura della Persona
st.write(
    "**Salute e Cura della Persona (€88,738.00)**"
)
st.write(
    "**Insight:** Health and personal care products have a good sales volume, showing strong consumer interest in health-related items. This suggests that the category is performing well but could benefit from further strategic focus."
)
st.write(
    "**Actionable Strategy:** Strengthen partnerships with health influencers and focus on educating consumers about the benefits of the products. Consider bundling items or creating special offers to attract more customers."
)

# Sport e Tempo Libero
st.write(
    "**Sport e Tempo Libero (€64,951.67)**"
)
st.write(
    "**Insight:** Sports and leisure products demonstrate a moderate sales volume, indicating steady performance but lower compared to top categories. This suggests a stable market presence with room for growth."
)
st.write(
    "**Actionable Strategy:** Capitalize on seasonal trends and major sports events to promote products. Enhance visibility through targeted promotions to boost sales in this category."
)

st.subheader("Low Sales Volume Categories")

# Alimentari e Cura della Casa
st.write(
    "**Alimentari e Cura della Casa (€0.00)**"
)
st.write(
    "**Insight:** This category shows zero sales, which could indicate a lack of market presence or insufficient consumer interest. The absence of sales suggests a significant issue that needs addressing."
)
st.write(
    "**Actionable Strategy:** Investigate the underlying reasons for zero sales. Consider introducing new products or revising the marketing strategy. Analyze consumer demand and adjust the product offerings to better meet market needs."
)

# Cancelleria e Prodotti per Ufficio
st.write(
    "**Cancelleria e Prodotti per Ufficio (€0.00)**"
)
st.write(
    "**Insight:** Similar to the food and home care category, this category also reports zero sales, potentially due to market fit issues or inadequate product availability."
)
st.write(
    "**Actionable Strategy:** Review the current product lineup and assess market needs. Explore new product options or improve the visibility and accessibility of office supplies to increase sales."
)


# # Define the business insights
# insights = {
#     "High Sales Volume Categories": {
#         "Casa e Cucina (€453,215.00)": {
#             "Insight": "This category has the highest average sales rank, indicating it generates the most significant sales volume among the categories. This suggests a strong market demand for home and kitchen products.",
#             "Actionable Strategy": "Focus marketing efforts and inventory investment in this category. Explore opportunities to introduce new products or premium options to leverage the high sales volume."
#         },
#         "Giochi e Giocattoli (€422,243.00)": {
#             "Insight": "Toys and games also show a high average sales rank, reflecting robust consumer interest. The high sales rank suggests a significant portion of revenue comes from this category.",
#             "Actionable Strategy": "Consider seasonal promotions and targeted marketing campaigns to capitalize on trends and maximize revenue from this category. Evaluate popular trends in toys and games to stay competitive."
#         }
#     },
#     "Moderate Sales Volume Categories": {
#         "Moda (€105,114.50)": {
#             "Insight": "The fashion category shows a moderate average sales rank, indicating a steady but not exceptional sales volume compared to the top categories.",
#             "Actionable Strategy": "Develop strategies to boost sales, such as collaborations with influencers or limited-time offers. Enhance product selection and focus on trending fashion items."
#         },
#         "Bellezza (€90,656.90)": {
#             "Insight": "Beauty products have a solid average sales rank, indicating a healthy demand. This category is important but not as dominant as the top two categories.",
#             "Actionable Strategy": "Increase marketing efforts and consider expanding the product line to include new beauty trends. Focus on customer loyalty programs and product reviews to drive sales."
#         },
#         "Salute e Cura della Persona (€88,738.00)": {
#             "Insight": "Health and personal care products show a good sales rank, reflecting consumer interest in health-related products.",
#             "Actionable Strategy": "Strengthen partnerships with health influencers and focus on product education. Consider bundling products or creating special offers to attract more customers."
#         },
#         "Sport e Tempo Libero (€64,951.67)": {
#             "Insight": "Sports and leisure products have a moderate sales rank, suggesting steady but lower sales compared to the top categories.",
#             "Actionable Strategy": "Leverage seasonal trends and promote products around major sports events or recreational activities. Enhance product visibility and consider promotions to boost sales."
#         }
#     },
#     "Low Sales Volume Categories": {
#         "Alimentari e Cura della Casa (€0.00)": {
#             "Insight": "This category shows zero sales, which could indicate a lack of product presence or low consumer demand.",
#             "Actionable Strategy": "Investigate the reasons for the lack of sales. Consider introducing new products or enhancing the marketing strategy for this category. Evaluate consumer demand and adjust product offerings accordingly."
#         },
#         "Cancelleria e Prodotti per Ufficio (€0.00)": {
#             "Insight": "Similar to the food and home care category, this category also has zero sales, indicating potential issues with market fit or product availability.",
#             "Actionable Strategy": "Assess the current product lineup and market needs. Consider exploring new product options or improving the visibility and accessibility of office supplies."
#         }
#     }
# }

# # Create a Streamlit app
# st.title('Business Insights Based on Sales Performance')

# # Display insights
# for category, details in insights.items():
#     st.subheader(category)
#     for item, info in details.items():
#         st.write(f"**{item}**")
#         st.write(f"**Insight:** {info['Insight']}")
#         st.write(f"**Actionable Strategy:** {info['Actionable Strategy']}")
#         st.write("")  # Add a blank line for readability


# Customer Reviews
st.markdown("<a id='customer-reviews'></a><h2>6. Customer Reviews and Price Impact</h2>", unsafe_allow_html=True)
# st.write("Content for Customer Reviews and Price Impact Analysis goes here.")
# Customer Reviews Analysis
# st.title('Customer reviews Analysis and Price Impact Analysis')

# Header
st.header('Product Price Analysis by Rating')

# Ensure price and rating columns are cleaned and converted to numeric
df1['price'] = df1['price'].astype(str).str.replace('[€,$,]', '', regex=True).replace('nan', pd.NA)
df1['rating'] = pd.to_numeric(df1['rating'], errors='coerce')
df1['price'] = pd.to_numeric(df1['price'], errors='coerce')

# Plotting
price_distribution_by_rating = px.box(
    df1,
    x='rating',
    y='price',
    title='Price Distribution by Rating',
    labels={'price': 'Price (€)', 'rating': 'Rating'}
)

# Increase figure size for better readability
price_distribution_by_rating.update_layout(
    width=1000,  # Width in pixels
    height=600   # Height in pixels
)

# Display the plot in Streamlit
st.plotly_chart(price_distribution_by_rating)

# Detailed Breakdown
st.header('Detailed Breakdown:')

# Rating 3.5
st.subheader('Rating 3.5:')
st.markdown("""
- **Count**: 45 products
- **Mean Price**: $58.99
- **Median Price**: $56.90
- **Standard Deviation**: $13.84
- **Min Price**: $34.50
- **Max Price**: $90.99
- **Q1 (25th Percentile)**: $49.20
- **Q3 (75th Percentile)**: $66.60

**Interpretation**: Products with a rating of 3.5 are less expensive with a narrower price range and lower variability compared to higher ratings.
""")

# Rating 4.0
st.subheader('Rating 4.0:')
st.markdown("""
- **Count**: 433 products
- **Mean Price**: $74.81
- **Median Price**: $47.90
- **Standard Deviation**: $62.75
- **Min Price**: $11.85
- **Max Price**: $386.37
- **Q1 (25th Percentile)**: $38.40
- **Q3 (75th Percentile)**: $85.99

**Interpretation**: For a rating of 4.0, prices have a wide range and high variability. The median is lower, indicating a significant number of lower-priced products despite the higher mean price.
""")

# Rating 4.5
st.subheader('Rating 4.5:')
st.markdown("""
- **Count**: 32,659 products
- **Mean Price**: $81.68
- **Median Price**: $71.00
- **Standard Deviation**: $53.12
- **Min Price**: $0.90
- **Max Price**: $1076.14
- **Q1 (25th Percentile)**: $48.40
- **Q3 (75th Percentile)**: $99.46

**Interpretation**: Products with a rating of 4.5 are the most numerous and have a broad price range. The median and quartiles are high, indicating a shift to higher prices, with significant variability.
""")

# Rating 5.0
st.subheader('Rating 5.0:')
st.markdown("""
- **Count**: 8,440 products
- **Mean Price**: $98.58
- **Median Price**: $79.51
- **Standard Deviation**: $74.14
- **Min Price**: $8.93
- **Max Price**: $907.50
- **Q1 (25th Percentile)**: $54.05
- **Q3 (75th Percentile)**: $114.99

**Interpretation**: Products with a perfect rating of 5.0 have the highest mean and median prices. The price range is extensive with the highest variability, showing that while these products are expensive on average, there is considerable variability in prices.
""")

# Summary
st.header('Summary:')
st.markdown("""
- **Higher Ratings**: Generally correspond with higher average and median prices, with a wider range and increased variability.
- **Price Range**: Expands with higher ratings, indicating that high-rated products can vary significantly in price.
- **Quartiles**: Both the first and third quartiles increase with ratings, indicating that higher-rated products are more likely to have higher prices.
""")


# Calculate the correlation between price and rating
correlation_price_rating = df1['price'].corr(df1['rating'])

# Display the results
st.title('Correlation Analysis')

# Display Correlation Result
st.write("Correlation Between Price and Rating:", correlation_price_rating)

# Display Interpretation
st.markdown("""
### Interpretation:

0.117 indicates a weak positive correlation between price and rating. This means that as the price increases, the rating tends to slightly increase as well. However, since the value is close to 0, the relationship is very weak and might not be practically significant. In other words, price does not have a strong impact on the ratings of the products in your dataset.
""")



# Calculate the correlation between the number of reviews and rating
correlation_reviews_rating = df1['number_of_reviews'].corr(df1['rating'])

# Display the results
# st.title('Correlation Analysis')

# Display Correlation Result
st.write("Correlation Between Number of Reviews and Rating:", correlation_reviews_rating)

# Display Interpretation
st.markdown("""
### Interpretation:

-0.128 indicates a weak negative correlation between the number of reviews and rating. This means that as the number of reviews increases, the rating tends to slightly decrease. Again, since the value is close to 0, this relationship is very weak and might not be practically significant. This suggests that the number of reviews is not strongly related to the ratings, but there is a slight tendency for products with more reviews to have slightly lower ratings.
""")

st.header('Source Analysis')

st.write(
    "The source of the data represents the website or platform from which the data was collected. "
    "Here, `es` stands for Spanish and `fr` stands for French."
)

# Calculate price variation by source
price_variation_by_source = px.box(
    df1,
    x='source',
    y='price',
    title='Price Variation by Source',
    labels={'price': 'Price ($)', 'source': 'Source'}
)

# Streamlit title and plot
st.header('Price Variation Analysis Across Different Sources')
st.plotly_chart(price_variation_by_source)

# Interpretation
st.markdown("""
### Interpretation:

#### 1. Average Price:
- **es**: The average price of products from the es source is $80.44.
- **fr**: The average price of products from the fr source is higher at $90.28.

**Implication:** On average, products from the fr source are more expensive than those from the es source.

#### 2. Minimum Price:
- **es**: The minimum price of a product from the es source is $6.34.
- **fr**: The minimum price of a product from the fr source is significantly lower at $0.90.

**Implication:** The fr source offers some products at very low prices, indicating a wider range of product prices compared to the es source.

#### 3. Maximum Price:
- **es**: The maximum price of a product from the es source is $1065.86.
- **fr**: The maximum price of a product from the fr source is slightly higher at $1076.14.

**Implication:** Both sources offer high-priced items, but the fr source has a slightly higher maximum price, reinforcing the observation that fr has a broader price range.

#### 4. Average Rating:
- **es**: The average rating of products from the es source is 4.594725.
- **fr**: The average rating of products from the fr source is very close, at 4.595767.

**Implication:** Both sources have very high average ratings, indicating that customers are generally very satisfied with products from both sources. The difference in average ratings is negligible.

#### 5. Total Number of Reviews:
- **es**: Products from the es source have a total of 69,282,983 reviews.
- **fr**: Products from the fr source have a total of 61,063,745 reviews.

**Implication:** The es source has received more reviews overall compared to the fr source. This could indicate higher sales volume or a larger customer base for the es source.

### Overall Implications:
- **Pricing:** The fr source has a broader price range, offering both very low-priced and high-priced products, while the es source has a narrower range with slightly lower average prices.
- **Customer Satisfaction:** Both sources have very high and similar average ratings, suggesting high customer satisfaction across the board.
- **Review Volume:** The es source has a higher total number of reviews, which might reflect higher engagement or a larger market presence compared to the fr source.
""")

# Calculate rating comparison by source
rating_comparison_by_source = px.box(
    df1,
    x='source',
    y='rating',
    title='Rating Comparison by Source',
    labels={'rating': 'Rating', 'source': 'Source'}
)

# Streamlit title and plot
st.header('Rating Comparison Analysis Across Different Sources')
st.plotly_chart(rating_comparison_by_source)

# Interpretation
st.markdown("""
### Interpretation:

#### 1. Average Rating:
- **es**: The average rating of products from the es source is 4.594725.
- **fr**: The average rating of products from the fr source is slightly higher at 4.595767.

**Implication:** Both sources have very high average ratings, indicating that customers are generally very satisfied with products from both sources. The difference in average ratings is negligible.

#### 2. Minimum Rating:
- **es**: The minimum rating of a product from the es source is 3.5.
- **fr**: The minimum rating of a product from the fr source is also 3.5.

**Implication:** Both sources have products that are rated at least 3.5, which indicates a relatively high baseline for product quality.

#### 3. Maximum Rating:
- **es**: The maximum rating of a product from the es source is 5.0.
- **fr**: The maximum rating of a product from the fr source is also 5.0.

**Implication:** Both sources have products that are rated the highest possible rating of 5.0, indicating top-rated products are present in both sources.

#### 4. Standard Deviation of Ratings:
- **es**: The standard deviation of ratings for the es source is 0.211010.
- **fr**: The standard deviation of ratings for the fr source is slightly higher at 0.215286.

**Implication:** The standard deviation measures the amount of variation or dispersion in the ratings. Both sources have low standard deviations, suggesting that the ratings are tightly clustered around the average. The slightly higher standard deviation for the fr source indicates a marginally wider spread in ratings, but the difference is minimal.

### Overall Implications:
- **Customer Satisfaction:** Both sources have very high average ratings, indicating strong customer satisfaction. The difference in average ratings is negligible, suggesting similar levels of customer satisfaction for products from both sources.
- **Rating Consistency:** The minimum and maximum ratings are the same for both sources, indicating that the range of product ratings is similar. The low standard deviations indicate that most products are rated close to the average, with the fr source having a slightly wider variation in ratings.
- **Quality Assurance:** Products from both sources maintain a high standard, with all products rated at least 3.5 and some achieving the perfect rating of 5.0. The consistency in high ratings reflects positively on the quality and reliability of products offered by both sources.
""")





# st.subheader('Overall Summary')
# st.write(
#     """
#     - **Focus on High Performers**: Prioritize marketing and inventory strategies for categories with high sales ranks (Casa e Cucina and Giochi e Giocattoli) to maximize revenue.
#     - **Enhance Moderate Categories**: Develop strategies to increase sales in moderate-performing categories (Moda, Bellezza, Salute e Cura della Persona, and Sport e Tempo Libero).
#     - **Revise Low Performers**: Investigate and address the reasons for zero sales in Alimentari e Cura della Casa and Cancelleria e Prodotti per Ufficio. Adjust strategies to improve performance in these categories.
#     """
# )


# Contact
st.markdown("<a id='contact'></a><h2>8. Contact</h2>", unsafe_allow_html=True)
st.markdown("""
<p>If you have any questions or require further analysis, please do not hesitate to reach out.</p>
<p>Contact us at: <a href="mailto:muthu@wissend.com">muthu@wissend.com</a></p>
""", unsafe_allow_html=True)


