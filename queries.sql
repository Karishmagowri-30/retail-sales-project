-- 1. Total sales by Region
SELECT Region, SUM(Total_Sales) AS Total_Revenue
FROM sales
GROUP BY Region
ORDER BY Total_Revenue DESC;

-- 2. Total sales by Category
SELECT Category, SUM(Total_Sales) AS Total_Revenue
FROM sales
GROUP BY Category
ORDER BY Total_Revenue DESC;

-- 3. Monthly sales trend
SELECT MONTH(Date) AS Month, 
YEAR(Date) AS Year,
SUM(Total_Sales) AS Monthly_Revenue
FROM sales
GROUP BY YEAR(Date), MONTH(Date)
ORDER BY Year, Month;

-- 4. Top 5 best selling products
SELECT Product, 
SUM(Quantity) AS Total_Quantity,
SUM(Total_Sales) AS Total_Revenue
FROM sales
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 5;

-- 5. Sales by Customer Segment
SELECT Customer_Segment,
COUNT(*) AS Total_Transactions,
SUM(Total_Sales) AS Total_Revenue
FROM sales
GROUP BY Customer_Segment
ORDER BY Total_Revenue DESC;