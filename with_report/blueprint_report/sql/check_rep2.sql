select count(*) from report_waiter
where month = '$in_month' and
       year = '$in_year';