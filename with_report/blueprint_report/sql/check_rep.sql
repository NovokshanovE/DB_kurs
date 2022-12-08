select count(*) from report
where month = '$in_month' and
       year = '$in_year';