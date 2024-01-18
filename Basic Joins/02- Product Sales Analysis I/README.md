# [Product Sales Analysis I](https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Report the product_name, year, and price for each sale_id in the Sales table.

Return the resulting table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>Use Inner Join</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>Join the two tables on product_id</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>


We want to form a new table that contains the product_name, year, and price for each sale_id in the Sales table. We can do this by joining the Sales table with the Product table on the product_id column. This will give us a new table that contains the product_name, year, and price for each sale_id in the Sales table.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 

```sql
SELECT Product.product_name, Sales.year, Sales.price
FROM Sales INNER JOIN Product ON Product.product_id = Sales.product_id;
```

</details>
