SELECT * FROM users 
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON user2.id = friendships.friend_id
order by user2.last_name;