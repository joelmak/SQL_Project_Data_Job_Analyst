/*
what are the top paying jobs for my role? 
what are the skills required for these top paying roles? 
what are the most in-demand skills for my role? 
what are the top skills based on salary for my role? 
what are the most optimal skills to learn? 
*/

SELECT 
    job_id,
    salary_year_avg
FROM job_postings_fact
WHERE salary_year_avg IS NOT NULL
ORDER BY 2 DESC
LIMIT 10; 

SELECT * FROM 

