# [Find Customer Referee]([ProblemURL](https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan-v2&envId=top-sql-50))

## Problem Requirements:
Find the <b>names</b> of the customer that are <strong>not referred by</strong> the customer with <code>id = 2</code>.
<br>
<strong>Note:</strong> You can print the result in any order.

<details>
    <summary style="font-size:1.3rem;font-weight:800"> Hints </summary> 
    <div class="hints" style="padding-left:30px">
        <details >
            <summary style="font-size:1.3rem;font-weight:800"> Hint#1 </summary>
            <p> Use <strong>OR</strong> operator to combine more than one condition. </p> 
        </details>
    </div>
</details>

<details>
    <summary style="font-size:1.3rem;font-weight:800"> Explanation </summary> 
    <p>
        Let's split the problem into two sub problems
        <ul>
            <li>Retrieve all the names using<code>SELECT</code> statement </li>
            <li>Filtering the retrieved data using <code>WHERE</code> clause and <code>OPERATORS</code>  </li>
        </ul>
        <p>
            First retrieve the names using <code>select</code> statement then use <code>where</code> clause to filter all the names that does not have <code>id = 2</code> in the corresponding row.
        </p>
        <p>
            But what if the referee_id is <code>NULL</code> , here we can use 
            <code>IS NULL</code> operator to filter it.
        </p>
        <p>
            Finally combine both conditions using <code>OR</code> operator to make sure that if one of the conditions is satisfied the  corresponding  name will be retrieved.
        </p>
    </p>
</details>

<details>
    <summary style="font-size:1.3rem;font-weight:800"> SQL Solution </summary> 
    <br>

```sql
    SELECT name 
    FROM customer 
    WHERE referee_id IS NULL OR referee_id <>2;
```
</details>
