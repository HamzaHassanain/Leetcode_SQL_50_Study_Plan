# [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

find the ids of products that are both low fat and recyclable.

Return the result table in any order.

### SQL Solution

```sql
select product_id from Products where low_fats="Y" and recyclable= "Y";
```

### Explanation

The question is pretty straight forward. We just need to find the ids of products that are both low fat and recyclable.

We can do this by using the <span style="color:blue;font-weight:bold"> WHERE </span> clause and the <span style="color:blue;font-weight:bold"> AND </span> operator.

The <span style="color:blue;font-weight:bold"> WHERE </span> clause will filter out all the products that are not low fat and recyclable. The <span style="color:blue;font-weight:bold"> AND </span> operator will make sure that the products are both low fat and recyclable.

The query will return the ids of the products that are both low fat and recyclable.
