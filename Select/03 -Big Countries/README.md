# [Big Countries](https://leetcode.com/problems/big-countries/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

A country is big if:

- it has an area of at least three million (i.e., 3000000 km2), or

- it has a population of at least twenty-five million (i.e., 25000000).

Find the name, population, and area of the big countries.

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;font-weight:800"> Hints </summary> 
<br>

- <details>
      <summary><strong>Hint#1</strong></summary>
      <p>Use the <span style="color:blue;font-weight:bold"> OR </span> operator to combine two conditions.
  </p>
  </details>

</details>

<details>
<summary style="font-size:1.3rem;font-weight:800"> Explanation </summary> 
<br>

The question is pretty straight forward. We just need to find the name, population, and area of the big countries.

We can do this by using the <span style="color:blue;font-weight:bold"> WHERE </span> clause and the <span style="color:blue;font-weight:bold"> OR </span> operator.

The <span style="color:blue;font-weight:bold"> WHERE </span> clause will filter out all the countries that are not big. The <span style="color:blue;font-weight:bold"> OR </span> operator will make sure that the countries are either big in area or population.

</details>

<details>
<summary style="font-size:1.3rem;font-weight:800"> SQL Solution </summary> 
<br>

```sql
SELECT name,area,population FROM World WHERE area >= 3000000 OR population >= 25000000;
```

</details>
