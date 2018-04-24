SELECT users.first_name, users.Last_name, user2.first_name as friend_first_name, user2.Last_name as friend_last_name
FROM users
left JOIN friendships ON users.id = friendships.users_id
left JOIN users as user2 on user2.id = friendships.friend_id1
ORDER BY friend_last_name DESC;

