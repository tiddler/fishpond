## Solution Report for LeetCode SQL Parts

### 175. [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)


>**Key point** : the code should return all possible importmation based on `Person` table regardless whether there is a related record in `Address` table. Hence. **Left Join** should be used.


>**Knowledge**:  TableA `OPERATION` TableB
>
>`INNER JOIN`: Subset records of A and B
>`LEFT JOIN`: ALL records in A while related records in B (NULL if none)
>`RIGHT JOIN`: ALL records in B while related records in A (NULL if none)

Code:
``` SQL
SELECT
    FirstName, LastName, City, State
FROM
    Person LEFT JOIN Address
    ON
        Person.PersonId = Address.PersonId
```
-------
### 176.[Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)

>**Key point**: If there is no second highest Salary, the query should return NULL.

>**Knowledge**: 
>``` SQL
>SELECT (
>   SELECT
>       SomeColName
>   FROM
>       SomeTable
>)
>```
>**Notice**: SELECT (SELECT * FROM XXXX) is **NOT** supported.
>The query will return first record of the sub-query and return NULL if there is no expected record.
>The code equals to 
>```SQL
>SELECT IFNULL( (SELECT SomeColNameFROM SomeTable), NULL)
>``` 

Code:
``` SQL
SELECT (
    SELECT DISTINCT
        Salary
    FROM
        Employee
    ORDER BY
        Salary
        DESC
    LIMIT 1, 1
)
```