# [Movie Rating](https://leetcode.com/problems/movie-rating/description/?envType=study-plan-v2&envId=top-sql-50)

### Problem Requirements:

Find the <code>name</code> of the user who has rated the <strong>greatest</strong> number of movies. In case of a tie, return the <strong> lexicographically smaller user name</strong>.

Find the movie <code>name</code> with the <strong>highest average rating in February 2020</strong>. In case of a tie, return the <strong>lexicographically smaller movie name</strong>.

<details>
<summary style="font-size:1.3rem;"> <strong>Hints</strong> </summary>

<details>
      <summary>Hint#1</summary>
      <p>Think of the query as two seperate problems</p>
</details>

<details>
      <summary>Hint#2</summary>
      <p>For the first problem: we want to find something for each user, think about grouping </p>
</details>

<details>
      <summary>Hint#3</summary>
      <p>For the first problem: how would you select the user who rated the most moives ? </p>
</details>

<details>
      <summary>Hint#4</summary>
      <p>For the first problem: use <code>count</code> function, with <code>order by </code> clause </p>
</details>

<details>
      <summary>Hint#5</summary>
      <p>For the second problem: think about gruoping again </p>
</details>

<details>
      <summary>Hint#6</summary>
      <p>For the second problem: to find the desired month and year use SQL <code>EXTRACT(YEAR_MONTH FROM date)=yyyymm</code>  </p>
</details>

<details>
      <summary>Hint#6</summary>
      <p>For the second problem: use <code>AVG</code> function, with <code>order by </code> clause </p>
</details>

<details>
      <summary>Hint#7</summary>
      <p>use sql<code>union all</code> to union the two select statments </p>
</details>

</details>
<details>
<summary style="font-size:1.3rem;"> <strong>Explanation</strong> </summary>

<p> 
To solve this problem we need to think of it as two seperate problems, the first one is to find the user who rated the most movies, and the second one is to find the movie with the highest average rating in February 2020.

for the first one, we need to find the user who rated the most movies, so we need to group by the user_id and count the number of movies for each user, then we need to order by the count in descending order, and if there is a tie we need to return the lexicographically smaller user name, so we need to order by the user name in ascending order.

for the second one, we need to find the movie with the highest average rating in February 2020, so we need to group by the movie_id and calculate the average rating for each movie, then we need to order by the average rating in descending order, and if there is a tie we need to return the lexicographically smaller movie name, so we need to order by the movie name in ascending order.

To join the two select statments we need to use <code>union all</code> to union the two select statments.

Why <code>union all</code> and not <code>union</code> ? because <code>union</code> will remove the duplicate rows, and we don't want that, we want to return the two results in one table.

</p>

</details>
<details>
<summary style="font-size:1.3rem"><strong> SQL Solution</strong> </summary>

```sql
(select Users.name as results from MovieRating
inner join Users on Users.user_id = MovieRating.user_id
group by MovieRating.user_id
order by count(MovieRating.movie_id) desc, Users.name asc
limit 1)
union all
(select Movies.title as results from MovieRating
inner join Movies on MovieRating.movie_id = Movies.movie_id
where extract(YEAR_MONTH FROM MovieRating.created_at) = 202002
group by MovieRating.movie_id
order by avg(MovieRating.rating) desc, Movies.title asc
limit 1);


```

</details>
