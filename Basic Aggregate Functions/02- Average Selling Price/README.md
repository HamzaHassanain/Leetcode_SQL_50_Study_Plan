# [Average Selling Price](https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the average selling price for each product. <code>average_price</code> should be rounded to 2 decimal places.

Return the result table in any order

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>Use <code>OUTER JOIN</code></p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>JOIN ON <code>product_id </code>AND <code>purchase_date</code></p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>SQL has an aggregation function called <code>SUM(expression)</code> which calculate the sum of values in a set</p>
</details>
<details>
      <summary>Hint#4</summary>
      <p>SQL has a <code>ROUND(number, decimals)</code> function which rounds a number to a specified number of decimal places. </p>
</details>
<details>
      <summary>Hint#5</summary>
      <p>SQL has a <code>COALESCE(val1 , val2 , ....)</code> function which Return the first non-null value in a list </p>
</details>
<details>
      <summary>Hint#6</summary>
      <p>Use <code>GROUP BY</code> clause to group a set of rows into a set of summary rows</p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

To find the average_price for each product we want should calculate the total money paid and the total units bought then divide them as follows


$$
    round(\frac{SUM(price \times units)}{SUM(units)} , 2)
$$

we will <code> JOIN</code> these tables <code> ON</code> <code> product_id </code> and <code> purchase_date</code>. The <code>purchase_date</code> should be between <code>start_date</code> and <code>end_date</code>.
<ul>
      <li>To calculate the total money we can use <code>SUM()</code> function to sum the money of each record. The money of each record equals the <code>price</code>multiplied by <code>units</code>. </li>
      <li>To calculate the total units we also can use <code>SUM()</code> function </li>.
      <li>To calculate the <code>average_price</code> we should divide total money by total units then use <code>ROUND(number , decimals)</code> to round the result. </li>
</ul>
But what if the total units is zero here we will have <code>null</code>. To solve this problem we can use <code>COALESCE()</code> function. This function will return the first non-null value in a list.
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 



```sql
SELECT 
    Prices.product_id, 
    COALESCE(
    ROUND(
      SUM(Prices.price * UnitsSold.units) / SUM(UnitsSold.units), 
      2
    ), 
    0
    ) AS average_price 
FROM 
  Prices
  LEFT OUTER JOIN UnitsSold ON Prices.product_id = UnitsSold.product_id 
  AND UnitsSold.purchase_date >= Prices.start_date 
  AND UnitsSold.purchase_date <= end_date 
GROUP BY 
  product_id
```
</details>