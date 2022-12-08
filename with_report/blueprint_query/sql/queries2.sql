select sum(dishes_amount) from restaurant.ordering ord
join order_lines ol on ord.id_O = ol.Ordering_id_O
where order_date like '$input_data%'