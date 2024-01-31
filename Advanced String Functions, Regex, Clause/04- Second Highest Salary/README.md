# [Problem name](https://problem-link-on-leetcode.com)

### Problem Requirements:

Problem requirements go here.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 
<details>
      <summary>Hint#1-10</summary>
      <p>hint body goes here</p>
</details>
</details>
<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>
Explanation goes here.
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
