-- Webmaster Database Backup Script
-- This script creates a backup of the database

-- Backup command (run from command line):
-- pg_dump -h localhost -U webmaster_user -d webmaster_db > backup_$(date +%Y%m%d_%H%M%S).sql

-- Restore command (run from command line):
-- psql -h localhost -U webmaster_user -d webmaster_db < backup_file.sql

-- Manual backup queries
SELECT 'Starting backup at ' || NOW() as backup_start;

-- Export users data
COPY (
    SELECT id, name, email, phone, created_at, updated_at 
    FROM users 
    ORDER BY created_at
) TO STDOUT WITH CSV HEADER;

-- Export form submissions data
COPY (
    SELECT fs.id, fs.user_id, u.name, u.email, fs.form_type, fs.message, fs.created_at
    FROM form_submissions fs
    JOIN users u ON fs.user_id = u.id
    ORDER BY fs.created_at
) TO STDOUT WITH CSV HEADER;

SELECT 'Backup completed at ' || NOW() as backup_end;




