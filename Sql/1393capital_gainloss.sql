# IF 的使用
SELECT stock_name, SUM(IF(operation = 'Buy', -price, price)) capital_gain_loss FROM Stocks
GROUP BY stock_name;

# CASE col WHEN val THEN col ELSE col END
SELECT stock_name, SUM(CASE operation WHEN 'Buy' THEN -price ELSE price END) capital_gain_loss FROM Stocks
GROUP BY stock_name;