import pandas as pd
import xml.etree.ElementTree as ET
customers_path = "task_DE_new_customers.csv"
customers = pd.read_csv(customers_path)

print(customers.head(), "\n")  # show first few rows


# ---------- STEP 2: READ ORDERS DATA (XML) ----------
xml_path = "data/task_DE_new_orders.xml"
tree = ET.parse(xml_path)
root = tree.getroot()

orders = []
for order in root.findall("order"):
    orders.append({
        "order_id": order.find("order_id").text,
        "mobile_number": order.find("mobile_number").text,
        "order_date_time": order.find("order_date_time").text,
        "sku_id": order.find("sku_id").text,
        "sku_count": int(order.find("sku_count").text),
        "total_amount": float(order.find("total_amount").text)
    })

orders_df = pd.DataFrame(orders)
print("✅ Orders file loaded successfully!")
print(orders_df.head(), "\n")


# ---------- STEP 3: CLEAN & PREPARE DATA ----------
# Convert date strings to datetime objects
orders_df["order_date_time"] = pd.to_datetime(orders_df["order_date_time"], errors="coerce")

# Check for missing values
print("🔍 Checking for missing data:")
print("Customers missing values:\n", customers.isna().sum())
print("\nOrders missing values:\n", orders_df.isna().sum(), "\n")

# Ensure column types
print("📘 Data types after cleaning:")
print(orders_df.dtypes, "\n")

print("✅ Step 2 complete — data loaded and cleaned successfully!")
