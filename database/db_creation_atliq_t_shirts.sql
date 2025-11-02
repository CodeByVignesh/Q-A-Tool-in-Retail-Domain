-- Create the database
CREATE DATABASE tera_tshirts;
USE tera_tshirts;

-- Create the t_shirts table
CREATE TABLE t_shirts (
    t_shirt_id INT AUTO_INCREMENT PRIMARY KEY,
    brand ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas') NOT NULL,
    color ENUM('Red', 'Blue', 'Black', 'White') NOT NULL,
    size ENUM('XS', 'S', 'M', 'L', 'XL') NOT NULL,
    price INT CHECK (price BETWEEN 10 AND 50),
    stock_quantity INT NOT NULL,
    UNIQUE KEY brand_color_size (brand, color, size)
);

-- Create the discounts table
CREATE TABLE discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    t_shirt_id INT NOT NULL,
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100),
    FOREIGN KEY (t_shirt_id) REFERENCES t_shirts(t_shirt_id)
);
DROP PROCEDURE IF EXISTS PopulateTShirts;
-- Create a stored procedure to populate the t_shirts table
DELIMITER $$

CREATE PROCEDURE PopulateTShirts()
BEGIN
    DECLARE brand_val VARCHAR(20);
    DECLARE color_val VARCHAR(10);
    DECLARE size_val VARCHAR(5);
    DECLARE price_val INT;
    DECLARE stock_val INT;
    DECLARE done INT DEFAULT 0;

    -- Cursor to generate all combinations of brand, color, and size
    DECLARE brand_list CURSOR FOR 
        SELECT b.brand_name, c.color_name, s.size_name
        FROM 
            (SELECT 'Van Huesen' AS brand_name
             UNION SELECT 'Levi'
             UNION SELECT 'Nike'
             UNION SELECT 'Adidas') AS b,
            (SELECT 'Red' AS color_name
             UNION SELECT 'Blue'
             UNION SELECT 'Black'
             UNION SELECT 'White') AS c,
            (SELECT 'XS' AS size_name
             UNION SELECT 'S'
             UNION SELECT 'M'
             UNION SELECT 'L'
             UNION SELECT 'XL') AS s;

    -- Handler to stop the loop when no more rows
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN brand_list;

    read_loop: LOOP
        FETCH brand_list INTO brand_val, color_val, size_val;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Random price between 10 and 50
        SET price_val = FLOOR(10 + RAND() * 41);
        -- Random stock between 10 and 100
        SET stock_val = FLOOR(10 + RAND() * 91);

        INSERT INTO t_shirts (brand, color, size, price, stock_quantity)
        VALUES (brand_val, color_val, size_val, price_val, stock_val);
    END LOOP;

    CLOSE brand_list;
END$$

DELIMITER ;



-- Call the stored procedure to populate the t_shirts table
CALL PopulateTShirts();

-- Insert at least 10 records into the discounts table
INSERT INTO discounts (t_shirt_id, pct_discount)
VALUES
(1, 10.00),
(2, 15.00),
(3, 20.00),
(4, 5.00),
(5, 25.00),
(6, 10.00),
(7, 30.00),
(8, 35.00),
(9, 40.00),
(10, 45.00);