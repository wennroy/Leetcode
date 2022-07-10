# UPDATE的使用方法与SET xx = case

UPDATE Salary
SET sex = CASE sex
WHEN 'm' THEN 'f'
ELSE 'm'
END;
