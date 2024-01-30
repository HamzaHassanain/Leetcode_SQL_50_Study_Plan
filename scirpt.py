import os
dirs = ["01- Employees Whose Manager Left the Company", "03- Movie Rating", "05- Friend Requests II: Who Has the Most Friends" , "07- Department Top Three Salaries"]

temp = """
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
    SQL code goes here
```
</details>
"""
basedir = "Subqueries"
for dir in dirs:
    os.mkdir(os.path.join(basedir, dir))
    with open(os.path.join(basedir, dir, "README.md"), "w") as f:
        f.write(temp)