# [Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Select the <code>product id, year, quantity, price</code> for the first year of every product sold.

Return the resulting table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>How would you filter the <code>Sales</code> table to only contain the first product sold</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>How would you use the result of the previous filtering to find the answer to the problem?</p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>Think subqueries</p>
</details>

<details>
      <summary>Hint#4</summary>
      <p>Think about <code>WHERE IN</code> clause</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

It is not obvious how would we use subqueries to solve this problem.

The key is to understand that we need to find the first year of every product sold. This means that we need to find the <strong> minimum year for every product</strong>. We can do this by <strong> grouping </strong> the table by <code>product_id</code> and then selecting the minimum year for every product. This will give us the first year of every product sold. Now we can use this result to filter the original table and get the desired result using <code>WHERE IN</code> clause.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
select product_id, year as first_year, quantity, price
from Sales
where (product_id,year) in (
    select product_id,min(year) from Sales
    group by product_id
);
```

</details>
