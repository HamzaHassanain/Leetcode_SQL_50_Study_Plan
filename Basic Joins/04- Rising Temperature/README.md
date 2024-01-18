# [Rising Temperature](https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary> 
<br>

<details>
      <summary>Hint#1</summary>
      <p>Use Self Join</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>SQL has a function called <strong>DATEDIFF("date1","date2")</strong> to find the diffrence between two dates in days </p>
</details>

<details>
      <summary>Hint#3</summary>
      <p> select the rows where the temperature of the first table is greater than the temperature of second table (using self joins) </p>
</details>


</details>

<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>


The problem asks to find the dates' Id with higher temperatures compared to its previous dates (yesterday). We can do this by joining the Weather table with itself and selecting only the dates form the first table where the temperature of the first table is greater than the temperature of second table. We can use the DATEDIFF("date1","date2") function to find the diffrence between two dates.

</details>

<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary> 

```sql
SELECT Weather1.id as Id
FROM Weather Weather1,Weather Weather2
WHERE Weather1.temperature > Weather2.temperature AND DATEDIFF(Weather1.recordDate, Weather2.recordDate)=1;
```

</details>
