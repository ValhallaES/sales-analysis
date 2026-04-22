# analyze sales data from csv file and calculate total sales, category-wise sales, top product and region-wise distribution

import pandas as pd
import sys
try:
    # Load the CSV file
    df = pd.read_csv('sales_data.csv')
    
    # Validate that required columns exist
    required_columns = ['Quantity', 'Price', 'Category', 'Product', 'Region', 'OrderID', 'Customer']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
    # Calculate total sales
    df['Sales'] = df['Quantity'] * df['Price']
    total_sales = df['Sales'].sum()

    print("=" * 70)
    print("SALES DATA ANALYSIS".center(70))
    print("=" * 70)

    # 1. Total Sales
    print(f"\n1. TOTAL SALES: ${total_sales:,.2f}")

    # 2. Category-wise Sales
    print("\n2. CATEGORY-WISE SALES:")
    category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    for category, sales in category_sales.items():
        percentage = (sales / total_sales) * 100
        print(f"   • {category:.<20} ${sales:>10,.2f} ({percentage:>5.1f}%)")

    # 3. Top Product (by total sales amount)
    print("\n3. TOP PRODUCT (by sales amount):")
    top_product = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
    best_product = top_product.index[0]
    best_sales = top_product.iloc[0]
    print(f"   • {best_product}: ${best_sales:,.2f} in sales")

    # 4. Region-wise Distribution (by sales amount)
    print("\n4. REGION-WISE DISTRIBUTION:")
    region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    for region, sales in region_sales.items():
        percentage = (sales / total_sales) * 100
        print(f"   • {region:.<20} ${sales:>10,.2f} ({percentage:>5.1f}%)")

    # 5. Orders with sales > $200
    print("\n5. ORDERS WITH SALES > $200:")
    high_sales_orders = df[df['Sales'] > 200][['OrderID', 'Customer', 'Product', 'Category', 'Quantity', 'Price', 'Sales']]
    if len(high_sales_orders) > 0:
        print(high_sales_orders.to_string(index=False))
    else:
        print("   No orders found with sales > $200")

    print("\n" + "=" * 70)
    print(f"Analysis Complete - Total Records Analyzed: {len(df)}")
    print("=" * 70)
    
except FileNotFoundError:
    print("ERROR: sales_data.csv file not found. Please ensure the file exists in the current directory.")
    sys.exit(1)
except ValueError as e:
    print(f"ERROR: {e}")
    sys.exit(1)
except Exception as e:
    print(f"ERROR: An unexpected error occurred: {e}")
    sys.exit(1)
