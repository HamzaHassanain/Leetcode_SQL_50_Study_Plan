# [List the Products Ordered in a Period](https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the names of products that have at least <code>100</code> units ordered in <code>February 2020</code> and their amount.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 
<details>
      <summary>Hint#1</summary>
      <p>We want to get the something for each product, so think about grouping </p>
</details>
<details>
      <summary>Hint#2</summary>
      <p> Use SQL <code>BETWEEN 'yyyy-mm-dd' AND  'yyyy-mm-dd'</code> to filter for a date  </p>
</details>

<details>
      <summary>Hint#3</summary>
      <p> Use SQL <code>BETWEEN 'yyyy-mm-dd' AND  'yyyy-mm-dd'</code> to filter for a date  </p>
</details>

<details>
      <summary>Hint#5</summary>
      <p> Use SQL <code>HAVING</code> clause to filter after using <code>GROUP BY</code>  </p>
</details>

</details>

<details>

<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

We have two tables, so we clearly need to join them.

Now we have to use an Aggregate function to get the sum of the units ordered for each product, so we clearly need to use <code>GROUP BY</code> clause.

Now we have to filter the result to get only the products that have at least <code>100</code> units ordered in <code>February 2020</code>, So first we need to get all the orders between <code>2020-02-1</code> and <code>2020-02-29</code> using <code>BETWEEN</code> clause, then we need to filter the result using <code>HAVING</code> clause. We will use an alias for the sum of the units ordered to make the code more readable, call it <code>uint</code>.

</details>

<details>

<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql

select Products.product_name, sum(Orders. unit) as unit  from Products
join Orders on Orders.product_id=Products.product_id
where Orders.order_date between '2020-02-1' and '2020-02-29'
group by Products.product_id
having unit >= 100;

```

</details>
