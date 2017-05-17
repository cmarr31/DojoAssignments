use friendsdb;

INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
VALUES ("Jay", "Patel", "Instructor", NOW(), NOW());
INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
VALUES ("Jimmy", "Jun", "Instructor", NOW(), NOW());
INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
VALUES ("Mau", "Rua", "student", NOW(), NOW());

select * from friends;