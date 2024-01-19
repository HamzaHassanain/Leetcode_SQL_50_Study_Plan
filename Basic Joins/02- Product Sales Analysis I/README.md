# [Product Sales Analysis I](https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Report the <code>product_name, year</code>, and <code>price</code> for each <code>sale_id</code> in the <code>Sales</code> table.

Return the resulting table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>Use Inner Join</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>Join the two tables on <code>product_id</code></p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

We want to form a new table that contains the <code>product_name, year</code>, and <code>price</code> for each <code>sale_id</code> in the <code>Sales</code> table. We can do this by joining the Sales table with the Product table on the <code>product_id</code> column. This will give us the new desired table.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
SELECT Product.product_name, Sales.year, Sales.price
FROM Sales INNER JOIN Product ON Product.product_id = Sales.product_id;
```

</details>
