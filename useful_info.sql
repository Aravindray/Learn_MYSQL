SELECT TABLE_SCHEMA, TABLE_NAME, create_time
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'cookbook'
ORDER BY create_time DESC;
