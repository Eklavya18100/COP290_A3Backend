--1--
CREATE TABLE `customer` (
	`cus_uid` INT(6) NOT NULL,
	`google_id` VARCHAR(255) DEFAULT NULL,
	`facebook_id` VARCHAR(255) DEFAULT NULL,
	`username` TEXT(255) NOT NULL,
	`email` VARCHAR(50) NOT NULL,
	`password` VARCHAR(255) NOT NULL,
	`phone` INT(20) DEFAULT NULL,
	UNIQUE KEY `cus_id` (`cus_uid`) USING BTREE,
	PRIMARY KEY (`cus_uid`)
);

--2--
CREATE TABLE `product_projects` (
	`id` INT(6) NOT NULL,
	`project_img_url` VARCHAR(255) DEFAULT NULL,
	`project_name` VARCHAR(25) NOT NULL,
	`project_address` VARCHAR(255) DEFAULT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`)
);

--3--
CREATE TABLE `product_aboutus` (
	`id` INT(6) NOT NULL,
	`description` TEXT(2000) DEFAULT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`)
);

--4--
CREATE TABLE `product_category` (
	`id` INT(6) NOT NULL,
	`name` TEXT(50) NOT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`)
);

--5--
CREATE TABLE `products` (
	`p_uid` INT(6) NOT NULL,
	`p_category_id` INT(6) NOT NULL,
	`p_location_id` INT(6) DEFAULT NULL,
	UNIQUE KEY `id` (`p_uid`) USING BTREE,
	PRIMARY KEY (`p_uid`)
);

--6--
CREATE TABLE `product_location` (
	`id` INT(6) NOT NULL,
	`name` TEXT(100) NOT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`)
);

--7--
CREATE TABLE `company` (
	`company_uid` INT(6) NOT NULL,
	`name` TEXT(255) NOT NULL,
	`company_img_url` VARCHAR(255) DEFAULT NULL,
	`address` VARCHAR(300) DEFAULT NULL,
	UNIQUE KEY `id` (`company_uid`) USING BTREE,
	PRIMARY KEY (`company_uid`)
);

--8--
CREATE TABLE `product_contractor` (
	`contractor_uid` INT(6) NOT NULL,
	`name` TEXT(255) NOT NULL,
	`email` VARCHAR(255) DEFAULT NULL,
	UNIQUE KEY `id` (`contractor_uid`) USING BTREE,
	PRIMARY KEY (`contractor_uid`)
);

--9--
CREATE TABLE `orders` (
	`id` INT(6) NOT NULL,
	`cus_uid` INT(6) NOT NULL,
	`order_date` VARCHAR(255) DEFAULT NULL,
	`p_uid` INT(6) NOT NULL,
	`payment_status` VARCHAR(255) DEFAULT NULL,
	`message` VARCHAR(500) DEFAULT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`),
    FOREIGN KEY (`cus_uid`) REFERENCES `customer` (`cus_uid`),
    FOREIGN KEY (`p_uid`) REFERENCES `products` (`p_uid`)
);

--10--
CREATE TABLE `bookmarks` (
	`id` INT(6) NOT NULL,
	`cus_uid` INT(6) NOT NULL,
	`p_uid` INT(6) NOT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`),
    FOREIGN KEY (`cus_uid`) REFERENCES `customer` (`cus_uid`),
    FOREIGN KEY (`p_uid`) REFERENCES `products` (`p_uid`)
);

--11--
CREATE TABLE `product_business` (
	`id` INT(6) NOT NULL,
	`contractor_uid` INT(6) NOT NULL,
	`website_link` VARCHAR(255) DEFAULT NULL,
	`followers` INT(12) DEFAULT NULL,
	`address` VARCHAR(255) DEFAULT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`),
    FOREIGN KEY (`contractor_uid`) REFERENCES `product_contractor` (`contractor_uid`)
);

--12--
CREATE TABLE `product_profile` (
	`p_uid` INT(6) NOT NULL,
	`project_id` INT(6) DEFAULT NULL,
	`business_id` INT(6) DEFAULT NULL,
	`aboutus_id` INT(6) DEFAULT NULL,
	UNIQUE KEY `id` (`p_uid`) USING BTREE,
	PRIMARY KEY (`p_uid`),
    FOREIGN KEY (`project_id`) REFERENCES `product_projects` (`id`),
    FOREIGN KEY (`aboutus_id`) REFERENCES `product_aboutus` (`id`)
);

--13--
CREATE TABLE `product_list` (
	`id` INT(6) NOT NULL,
	`p_uid` INT(6) NOT NULL,
	`p_img_url` VARCHAR(255) DEFAULT NULL,
	`p_description` TEXT(500) DEFAULT NULL,
	`company_id` INT(6) DEFAULT NULL,
	`p_contractorid` INT(6) DEFAULT NULL,
	UNIQUE KEY `id` (`id`) USING BTREE,
	PRIMARY KEY (`id`),
    FOREIGN KEY (`p_uid`) REFERENCES `products` (`p_uid`),
    FOREIGN KEY (`company_id`) REFERENCES `company` (`company_uid`)
);