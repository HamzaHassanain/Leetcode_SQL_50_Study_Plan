# [Last Person to Fit in the Bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

There is a queue of people waiting to board a bus. <strong>However</strong>, the bus has a weight limit of <code>1000 kilograms</code>, so there may be some people who cannot board.

Find the <code>person_name</code> of the last person that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>Think in reverse? Let us try to find the persons who will not be able to the bus. Who would you do such a thing ? </p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>for each turn we need to find all turns that are less that or equal to it </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

This problem seems simple but it is a bit tricky. We need to find the last person that can fit in the bus. So we need to find the person that has the maximum turn number that can fit in the bus. So we need to find the sum of the weights of all people that have a turn number less than or equal to the current turn number. Then we need to find the maximum turn number that has a sum of weights less than or equal to 1000.

Ok, Think like this. We need to make a nested for loop that works like this:

```bash
for each turn
    for each turn that is less than or equal to the current turn
        find the sum of weights
        if the sum of weights is less than or equal to 1000
            save the turn number as our answer
```

This can be done using a subquery. We can use the subquery to find the sum of weights for each turn that is less than or equal to the current turn. Then we can use the outer query to find the maximum turn number that has a sum of weights less than or equal to 1000.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
select person_name from queue as mainQ
where 1000 >= (
    select sum(weight)
    from queue
    where mainQ.turn >= turn
)
order by turn desc
limit 1;
```

</details>
