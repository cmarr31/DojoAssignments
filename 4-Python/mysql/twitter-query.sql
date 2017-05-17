use twitter;
SELECT *
FROM users
WHERE first_name LIKE "%e"
ORDER BY birthday DESC;
/*
insert into tweets values(101,'xxx',1,now(),now())
*/
select * from tweets;
/*
concat('Mr. ', firts_name)
concat_ws('Mr.', firts_name)
length()
lower()
hour()
dayname()
month()
now()
date_format()
group_concat(' ', x, y)
count()
*/
update users
set first_name = 'Mau'
where users.id=1;
/*
SET SQL_SAFE_UPDATES = 0;
*/
delete from tweets where id>100;
/* */
SELECT tweets.tweet as kobe_tweets
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 1;
/* Friday March 9th 2012 at 12:30:00 PM */
SELECT DATE_FORMAT('2012-03-09 12:30', '%W %M %D %Y at %r') AS great_time;
/* */
SELECT id, first_name FROM users LIMIT 11,10 ;
/* */
SELECT * FROM users WHERE first_name between 'a' and 'z';