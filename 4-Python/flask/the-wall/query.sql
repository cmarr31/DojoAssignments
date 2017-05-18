use the_wall_db;
select * from users;
select * from messages where created_at between date_add(NOW(),INTERVAL -30 MINUTE) and NOW();
select * from comments;
DELETE FROM comments WHERE id =1;