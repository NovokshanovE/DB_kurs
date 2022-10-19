select sum(Order_amount) from restaurant.ordering
where order_date like '$input_data'