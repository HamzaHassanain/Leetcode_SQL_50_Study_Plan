# [Not Boring Movies](https://leetcode.com/problems/not-boring-movies/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Report the movies with an odd-numbered ID and a description that is not <code>"boring"</code>.

Return the result table ordered by <code>rating</code> in <strong> descending order</strong>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>SQL has a <code>MOD(num1, num2)</code> function that returns the value of <code>num1 % num2</code> (with <code>%</code> beging the modulo operator) </p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>SQL has a <code>NOT</code> operator  </p>
</details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

In order to solve this problem we need to use the <code>mod</code> function to get the odd numbered IDs and the <code>not</code> operator to get the movies with description not equal to <code>"boring"</code>.

Then, we can combine the two conditions using the <code>and</code> operator.

Finally, we can order the result by <code>rating</code> in descending order using <code>desc</code> keyword.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
select id, movie, description, rating from Cinema
where mod(id, 2)=1 and not description = "boring"
order by rating desc;
```

</details>
