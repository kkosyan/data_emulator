CREATE TABLE IF NOT EXISTS users
(
    user_id    BIGINT,
    country    VARCHAR(40),
    gender     VARCHAR(20),
    age        BIGINT,
);

CREATE USER test_user WITH PASSWORD 'postgres';
GRANT ALL ON DATABASE test_postgres TO test_user;

INSERT INTO users(user_id, country, gender, age) VALUES
    (0, 'US', 'M', 31),
    (1, 'UK', 'F', 45),
    (2, 'DE', NULL, 55),
    (3, 'BG', 'M', 87),
    (4, 'US', 'F', 17),
    (5, 'UK', 'M', 22),
    (6, 'US', 'M', 27),
    (7, 'BG', 'F', 32),
    (8, 'ES', 'M', 44),
    (9, 'FR', NULL, 54),
    (10, 'US', 'M', 66)
;
