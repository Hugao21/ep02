SELECT *
FROM posts_post
ORDER BY pub_date DESC;

SELECT *
FROM posts_comment
WHERE post_id = 1;

SELECT c.id, c.author_id, c.text, c.date, p.title, p.pub_date AS post_date
FROM posts_comment AS c
INNER JOIN posts_post AS p ON c.post_id = p.id
WHERE c.post_id = 1;

SELECT cat.*, p.*
FROM posts_category AS cat
INNER JOIN posts_category_posts AS cp ON cp.category_id = cat.id
INNER JOIN posts_post AS p ON cp.post_id = p.id
WHERE cat.id = 1;

SELECT cat.*, COUNT(cp.post_id) AS num_posts
FROM posts_category AS cat
INNER JOIN posts_category_posts AS cp ON cp.category_id = cat.id
GROUP BY cat.id
HAVING COUNT(cp.post_id) >= 2;
