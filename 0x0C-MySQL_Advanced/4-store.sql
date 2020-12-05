-- Buy buy buy
-- creates a trigger that decreases the quantity of an item
CREATE TRIGGER buy_trigger BEFORE INSERT ON orders
FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
