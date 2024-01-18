# [Big Countries](https://leetcode.com/problems/big-countries/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

A country is big if:

- it has an area of at least three million (i.e., 3000000 km2), or

- it has a population of at least twenty-five million (i.e., 25000000).

Find the name, population, and area of the big countries.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 
<br>

<details>
      <summary>Hint#1</summary>
      <p>Use the <strong> OR </strong> operator to combine two conditions.
  </p>
  </details>

</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

<br>

The question is pretty straight forward. We just need to find the name, population, and area of the big countries.

We can do this by using the <strong> WHERE </strong> clause and the <strong> OR </strong> operator.

The <strong> WHERE </strong> clause will filter out all the countries that are not big. The <strong> OR </strong> operator will make sure that the countries are either big in area or population.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 
<br>

```sql
SELECT name,area,population FROM World WHERE area >= 3000000 OR population >= 25000000;
```

</details>
