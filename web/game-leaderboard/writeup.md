### Game-leaderboard no logins or anything. Allows you to make queries to the database. Get profile_id through sqli -> idor for flag

This one is real quick. We are presented with a simple leaderboard that has a form to make a query.

![](./screenshots/page.png)

Lets send a query & catch it in burp

![](./screenshots/repeated.png)

Checking the source code we see a few points that stick out

![](./screenshots/vulnerableQuery.png)
