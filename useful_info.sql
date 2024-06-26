-- To list all the table name based on creation date

SELECT TABLE_SCHEMA, TABLE_NAME, create_time
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'cookbook' -- change the database name
ORDER BY create_time DESC;

-- To check the tablespace of the table

SELECT NAME, SPACE_TYPE FROM INFORMATION_SCHEMA.INNODB_TABLESPACES
WHERE NAME LIKE 'cookbook/%'; -- add the table name with database
