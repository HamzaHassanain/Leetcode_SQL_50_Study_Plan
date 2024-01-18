# [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

find the ids of products that are both low fat and recyclable.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong></summary> 
<br>

- <details>
      <summary>Hint#1</summary>
      <p>Use the <strong> AND </strong> operator to combine two conditions.
  </p>
  </details>

</details>

<details>
<summary style="font-size:1.3rem"> <strong> Explanation </strong> </summary> 
<br>

The question is pretty straight forward. We just need to find the ids of products that are both low fat and recyclable.

We can do this by using the <strong> WHERE </strong> clause and the <strong> AND </strong> operator.

The <strong> WHERE </strong> clause will filter out all the products that are not low fat and recyclable. The <strong> AND </strong> operator will make sure that the products are both low fat and recyclable.

The query will return the ids of the products that are both low fat and recyclable.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 
<br>

```sql
select product_id from Products where low_fats="Y" and recyclable= "Y";
```

</details>
