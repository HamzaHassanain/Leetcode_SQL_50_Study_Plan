# [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the second highest salary from the <code>Employee</code> table. If there is no second highest salary, return <code>null (return None in Pandas)</code>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>Think about  subqueries </p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>Think about how would you get the second highest salary without a subquery </p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>The only purpose of the subquery is to handel the idea that the second highest may not exist </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

To solve this problem, we need first to find the second highest salary, this is easy we need to sort the salaries in descending order and get the second one. But what if there is no second highest salary? In this case, we need to return <code>null</code>. To solve this problem we can use a subquery to get the second highest salary, and if it doesn't exist, we will get <code>null</code> as a result.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql

select
(select distinct Salary
from Employee order by salary desc
limit 1 offset 1)
as SecondHighestSalary;


```

</details>
