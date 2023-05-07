import sqlite3
import pandas as pd

conn = sqlite3.connect('test.db')


select_dates = ('''
        WITH RECURSIVE dates(date) AS (
          VALUES(DATE('now'))
          UNION ALL
          SELECT date(date, '+' || FLOOR(ABS(RANDOM()) % 6 + 2) || ' days')
          FROM dates
          WHERE date <= date('now', '+2 year')
          LIMIT 100
        )
        SELECT date
        FROM dates;
    ''')


select_sales = ('''
        SELECT employee.name, COUNT(sales.id) as sales_c, SUM(sales.price) as sales_s,
        DENSE_RANK() OVER (ORDER BY COUNT(sales.id) ASC) AS sales_rank_c,
        DENSE_RANK() OVER (ORDER BY SUM(sales.price) ASC) AS sales_rank_s 
        FROM
            employee
        LEFT JOIN
            sales ON employee.id = employee_id
        GROUP BY
            employee.id
        ORDER BY
            sales_rank_s DESC,
            sales_rank_c DESC;
    ''')


select_balance = ('''
       WITH transfer_dates AS (
    SELECT from_acc as acc, -amount as amount, strftime('%Y-%m-%d', substr(tdate, 7, 4) || '-' || substr(tdate, 4, 2) || '-' || substr(tdate, 1, 2)) as tdate
    FROM transfers
    UNION ALL
    SELECT to_acc as acc, amount as amount, strftime('%Y-%m-%d', substr(tdate, 7, 4) || '-' || substr(tdate, 4, 2) || '-' || substr(tdate, 1, 2)) as tdate
    FROM transfers
    ORDER BY acc, tdate ASC
)
SELECT t1.acc, SUM(t2.amount) AS balance, strftime('%d.%m.%Y', t1.tdate) AS dt_from, (
        LEAD(strftime('%d.%m.%Y', t1.tdate) , 1, "01.01.3000") OVER (PARTITION BY t1.acc ORDER BY t1.acc, t1.tdate)
    ) AS dt_to
FROM transfer_dates t1
INNER JOIN transfer_dates t2
  ON t1.acc = t2.acc
  AND t1.tdate >= t2.tdate
GROUP BY t1.acc, t1.tdate
ORDER BY t1.acc, t1.tdate ASC;
''')


if __name__ == '__main__':
    print("Задача 1")
    print(pd.read_sql_query(select_dates, conn))
    print("Задача 2")
    print(pd.read_sql_query(select_sales, conn))
    print("Задача 3")
    print(pd.read_sql_query(select_balance, conn))
    conn.close()
