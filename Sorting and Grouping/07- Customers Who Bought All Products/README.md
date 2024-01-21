# [Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Report the customer ids from the Customer table that bought all the products in the Product table.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>How can we get all ids of products bought by a customer ? </p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>Group the customers table by <code>customer_id</code> </p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>How can we select all distinct <strong>product keys</strong> ? </p>
</details>

<details>
      <summary>Hint#4</summary>
      <p>We can use a simple <code>SELECT</code> statment with <code>COUNT</code> function </p>
</details>

<details>
      <summary>Hint#5</summary>
      <p>We can we filter the customer that bought all products? </p>
</details>

<details>
      <summary>Hint#6</summary>
      <p>Use subqueries with <code>HAVING</code> clause, how can we combine both? </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

This is a simple grouping problem but but you have to familiar with the concpet of <code>Subqueries</code>.

Let's break down the solution into steps:

- First, we need to get all the customers grouped by their ids to be able to count the number of products they bought.
- Second, we need a way to find the number of products in the Product table, this can be done with a simple subquery using <code>SELECT</code>, we can use <code>COUNT</code> function to get the number of products.

- Finally, we need to filter the customers that bought all products, this can be done with <code>HAVING</code> clause, we can use <code>HAVING</code> clause with <code>COUNT</code> function to count the number of products bought by each customer and compare it with the number of products in the Product table (got by the subquery described in the second point).
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
select customer_id from Customer
group by customer_id
having count(distinct product_key) = (select count(product_key) from Product);
```

</details>
