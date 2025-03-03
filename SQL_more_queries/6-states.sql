-- creates the database hbtn_0d_usa and the table states
CREATE database IF NOT EXISTS hbtn_0d_usa
use hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT primary key,
	name VARCHAR(256) NOT NULL
)
