# [Product Price at a Given Date](https://leetcode.com/problems/product-price-at-a-given-date/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the prices of all products on <code>2019-08-16</code>. Assume the price of all products before any change is <code>10</code>.

Return the result table in <strong>any order</strong>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 

<details>
      <summary>Hint#1</summary>
      <p>
        What is the answer for a product that does not have any <code>change_date</code> on or before <code>'2019-08-16'</code> ?
      </p>
</details>
<details>
      <summary>Hint#2</summary>
      <p>
        What is the answer for a product that has at least one<code>change_date</code> on or before <code>'2019-08-16'</code> ?
      </p>
</details>
<details>
      <summary>Hint#3</summary>
      <p>
        Use the <code>EXISTS</code> operator to check whether there is a record with specific properties
      </p>
</details>
<details>
      <summary>Hint#4</summary>
        <p>
            MySQL <code>UNION</code> operator allows you to combine two or more result sets of queries into a single result set 
        </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

Certainly, the answer is <code>10</code> for any product without a <code>change_date</code> on or before <code>'2019-08-16'</code>. To ensure this, we can utilize the <code>NOT</code> and <code>EXISTS</code> operators to confirm that there is no record associated with the product and having a <code>change_date</code> on or before <code>'2019-08-16'</code>.

If a product has at least one record with a <code>change_date</code> on or before <code>'2019-08-16'</code>, we need to retrieve the last <code>changed_date</code> to obtain the <code>last_changed_price</code>.

We can dot this by using <code>EXISTS</code> operator as follows:
- The <code>change_date</code> of the current record should be on or before <code>'2019-08-16'</code>
- There is no record associated with the product on or before <code>'2019-08-16'</code> has a <code>change_date</code> greater than the <code>change_date</code> of the current record 

We can combine these results by using <code>UNION ALL</code>.

We used <code>UNION ALL</code> instead of <code>UNION</code> because there are no duplicate records between both results and to improve the performance of our query.
</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 


```sql
SELECT 
    a.product_id, 
    a.new_price as price 
FROM 
    Products a 
WHERE 
    a.change_date <= '2019-08-16' 
    AND NOT EXISTS (
    SELECT 
        b.product_id 
    FROM 
        Products b 
    WHERE 
        b.change_date <= '2019-08-16' 
        AND b.product_id = a.product_id 
        AND a.change_date < b.change_date
    )

UNION --###########################################

SELECT 
    a.product_id, 
    10 as price 
FROM 
    Products a 
WHERE 
    NOT EXISTS(
    SELECT 
        b.product_id 
    FROM 
        Products b 
    WHERE 
        a.product_id = b.product_id AND b.change_date <= '2019-08-16'
    )
```

</details>