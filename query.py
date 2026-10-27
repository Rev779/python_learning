#1
/* Find menu_items priced above 100. */
SELECT * FROM Menu_items
WHERE price > 100;

#2
/*Display today's orders.*/
SELECT * FROM Orders
WHERE DATE(created_at) = CURDATE();

# 3
/*Show customers from Chirala.*/
SELECT * FROM Customers
WHERE city = 'Chirala';

#4
/*Display pending orders.*/
SELECT * FROM Orders
WHERE order_status = 'pending';

#5
/* Display all staff working as Waiter.*/
SELECT * FROM Staff
WHERE role = 'Waiter';

#6
/*Display all Dessert items.*/
SELECT m.*
FROM Menu_items m
JOIN Categories c ON m.category_id = c.id
WHERE c.category_name = 'Desserts';
#7
/* Find the total number of orders.*/
SELECT COUNT(*) AS total_orders
FROM Orders;

#8
 /*Count customers city-wise.*/ 
SELECT city, COUNT(*) AS customer_count 
FROM CUSTOMERS GROUP BY city;

#9
 /*Calculate average menu price.*/
SELECT ROUND(AVG(price)) AS average_price 
FROM MENU_items;

#10
 /*Find the highest menu price.*/ 
SELECT MAX(price) AS highest_price 
FROM MENU_items;

#11
 /*Count orders handled by each waiter.*/
SELECT staff_id, COUNT(*) AS order_count 
FROM ORDERS GROUP BY staff_id; 

#12
/*Count menu items in each category.*/ 
SELECT c.category_name, COUNT(m.id) AS item_count
FROM Categories c
LEFT JOIN Menu_items m ON m.category_id = c.id
GROUP BY c.id, c.category_name
ORDER BY item_count DESC;

#13
/*Find staff earning more than ₹18,000.*/
SELECT * FROM STAFF 
WHERE salary > 18000; 

#14
/*Find total sales by payment method.*/
SELECT payment_mode AS method, SUM(amount) AS total_sales
FROM Payments
GROUP BY payment_mode;

#15
/* Display Customer Name and Order Status.*/
SELECT c.customer_name, o.order_status
FROM Orders o
JOIN Customers c ON o.customer_id = c.id;

#16
/*Find customers who never placed an order.*/
SELECT c.customer_name
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customer_id
WHERE o.id IS NULL;

#17
/*Display top 3 highest bills.*/
SELECT order_id, amount 
FROM PAYMENTS 
ORDER BY amount DESC LIMIT 3;

#18
/* Find average bill amount for each payment method.*/
SELECT payment_mode AS method, AVG(amount) AS average_bill
FROM Payments
GROUP BY payment_mode;

#19
/* . Find orders with no payment yet.*/
SELECT o.id AS order_id, o.order_status
FROM Orders o
LEFT JOIN Payments p ON o.id = p.order_id
WHERE p.id IS NULL;

#20
 Display daily sales report.
SELECT DATE(o.created_at) AS order_date, SUM(p.amount) AS daily_sales
FROM Orders o
JOIN Payments p ON o.id = p.order_id
GROUP BY DATE(o.created_at)
ORDER BY order_date;