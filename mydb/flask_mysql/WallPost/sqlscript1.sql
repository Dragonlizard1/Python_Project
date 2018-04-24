SELECT *
FROM users
left Join posts on users.idusers = posts.users_id
WHERE users.idusers = 1;



select *
from comments
join users as user2 on comments.idcomments = user2.idusers
