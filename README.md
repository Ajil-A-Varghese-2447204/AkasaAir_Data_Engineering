# 🚀 Akasa Air – Customer & Order Data Analysis (Python + Power BI)

## 🎯 Objective
This project analyzes **customer** and **order** data received daily from CSV and XML sources.  
Using **Python** for data ingestion, cleaning, and analysis, and **Power BI** for visualization, the goal is to generate actionable business insights such as:

- 🧍‍♂️ Repeat Customers  
- 📅 Monthly Order Trends  
- 🌍 Regional Revenue  
- 💰 Top Customers in the Last 30 Days  

---

## 🧠 Project Overview

| Phase | Tool/Technology | Purpose |
|--------|----------------|----------|
| **Data Processing** | 🐍 Python (Pandas, XML Parsing) | Clean, merge, and analyze raw data |
| **Visualization** | 📊 Power BI Desktop | Build interactive dashboards |
| **Storage (Optional)** | 🗄️ MySQL | For database-based approach |
| **Version Control** | 🧩 GitHub | Code and documentation management |

---

## 🧩 Data Sources

### 🧾 Customers Data (CSV)
| Field | Description |
|--------|-------------|
| customer_id | Unique customer ID |
| customer_name | Full name of the customer |
| mobile_number | Customer’s phone number (used as key) |
| region | Customer region (e.g., North, South) |

### 📦 Orders Data (XML)
| Field | Description |
|--------|-------------|
| order_id | Unique order identifier |
| mobile_number | Foreign key linking to customer |
| order_date_time | Timestamp of the order |
| sku_id | Product code |
| sku_count | Quantity ordered |
| total_amount | Order value in INR |

---

## ⚙️ Python Implementation

### 🧩 Folder Structure
akasa_project/
│
├── data/
│ ├── task_DE_new_customers.csv
│ └── task_DE_new_orders.xml
│
├── output/
│ ├── merged_data.csv
│ ├── repeat_customers.csv
│ ├── monthly_trends.csv
│ ├── regional_revenue.csv
│ └── top_customers.csv
│
├── main.py
├── requirements.txt
└── README.md


---

### 🔹 Steps Performed in Python

1️⃣ **Data Loading**  
   - Loaded CSV (customers) and XML (orders) using `pandas` and `xml.etree.ElementTree`.

2️⃣ **Data Cleaning**  
   - Normalized date formats (`order_date_time`)  
   - Ensured type consistency (e.g., `mobile_number` as string)  
   - Handled missing or invalid data entries  

3️⃣ **Merging Data**  
   - Joined both datasets on `mobile_number`

4️⃣ **KPI Calculations**  
   - **Repeat Customers:** Count of customers with more than one order  
   - **Monthly Order Trends:** Orders grouped by month  
   - **Regional Revenue:** Total amount grouped by region  
   - **Top Customers (Last 30 Days):** Highest spenders within 30 days  

5️⃣ **Export for Power BI**  
   - Saved cleaned and merged dataset as `merged_data.csv`  
   - Also exported KPI results as CSVs inside `output/`
    ![alt text](image-1.png)



---

### ▶️ How to Run the Python Script

#### 1. Create Environment
```bash
python -m venv venv
venv\Scripts\activate   

