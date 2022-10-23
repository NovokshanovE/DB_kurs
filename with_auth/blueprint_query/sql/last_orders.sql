select * from restaurant.ordering
where order_date > date(curdate() - '$input_data')