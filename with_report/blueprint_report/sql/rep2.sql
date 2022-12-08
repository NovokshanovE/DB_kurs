select name, surname, summa from report_waiter rw
join waiter w on w.id_W = rw.Waiter_id_W
where `year` = '$in_year' and `month` = '$in_month'