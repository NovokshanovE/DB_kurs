select name_dishes, dish_count, month_income from report rep
join menu on menu.id_M = rep.id_dish
where `year` = '$in_year' and `month` = '$in_month'