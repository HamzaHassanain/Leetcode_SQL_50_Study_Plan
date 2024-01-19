# [Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

If the customer's <strong> preferred delivery date </strong> is the same as the <strong>order date</strong>, then the order is called <strong>immediate</strong>; otherwise, it is called scheduled.

The first order of a customer is the order with the <strong>earliest order date</strong> that the customer made. It is <strong>guaranteed</strong> that a customer has precisely one first order.

Find the <strong>percentage of immediate orders in the first orders of all customers</strong>, rounded to <strong>2</strong> decimal places.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>Immediate order occurres when <code>order_date = customer_pref_delivery_date</code></p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>Use <code>CASE</code> Expression and the <code>SUM</code> function to find the number of Immediate orders.
      What will the whole sample sapce of orders be ?</p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>The sample space is the number of all orders in the table we can get it using <code>COUNT(*)</code> </p>
</details>

<details>
      <summary>Hint#4</summary>
      <p>How would you find the <code>MIN</code> <strong>order_date</strong> for each customer ?  </p>
</details>

<details>
      <summary>Hint#5</summary>
      <p>Use <code>WHERE IN</code> clause (subquering) </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

This problem is somewhat tough, we need to calculate the percentage of immediate orders in the first orders of all customers.

First we need to find a way to find the immediate orders. But, before that we must also find a way to find the first order of each customer.

To find the first order of each customer we will be using <code>WHERE IN</code> clause.

The <code>WHERE IN</code> clause is used to filter the result of a subquery. It extracts the rows from the outer query and then compares it with the result of the subquery. It looks like this:

```sql
WHERE (col1,col2) IN (
    SELECT SOME_FUNCTION(col1), SOME_FUNCTION(col2)
    FROM tableX
    WHERE condition
);
```

Now we need to find the number of immediate orders, we can do that using <code>CASE</code> expression and <code>SUM</code> function.

Since we did filter the Delivery table to have only the <code>customer_id</code> with the <strong>first order made </strong> we can now check the use <code>SUM</code> funtion on the <code>CASE</code> condition to find the number of <code>order_date = customer_pref_delivery_date</code> inside the <code>CASE</code> expression to find the count of immediate orders.

We can divide the Summetion by the <code>COUNT(\*)</code> then multiply by <code>100</code> to get the percentage. Of course do not forget to <strong>round</strong> to <strong>2</strong> decimal places.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
SELECT ROUND(100 * SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(*), 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id,order_date) IN (
    SELECT customer_id, MIN(order_date) AS od
    FROM Delivery
    GROUP BY customer_id
);
```

</details>
