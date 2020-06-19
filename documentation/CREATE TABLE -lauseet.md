# CREATE TABLE -lauseet

### User / Account
    CREATE TABLE account (
	    id INTEGER NOT NULL, 
	    date_created DATETIME, 
	    date_modified DATETIME, 
	    name VARCHAR(144) NOT NULL, 
	    username VARCHAR(144) NOT NULL, 
	    password VARCHAR(144) NOT NULL, 
	    student BOOLEAN NOT NULL, 
	    teacher BOOLEAN NOT NULL, 
	    user_role VARCHAR(80), 
	    PRIMARY KEY (id), 
	    CHECK (student IN (0, 1)), 
	    CHECK (teacher IN (0, 1))
    )

### Lasku
     CREATE TABLE invoice (
	    id INTEGER NOT NULL, 
	    date_created DATETIME, 
	    date_modified DATETIME, 
            kurssi_id INTEGER NOT NULL, 
	    paid BOOLEAN NOT NULL, 
	    account_id INTEGER NOT NULL, 
	    PRIMARY KEY (id), 
	    CHECK (paid IN (0, 1)), 
	    FOREIGN KEY(account_id) REFERENCES account (id)
    )

### Kurssi
    CREATE TABLE kurssi (
	    id INTEGER NOT NULL, 
	    date_created DATETIME, 
	    date_modified DATETIME, 
	    name VARCHAR(144) NOT NULL, 
	    start_date DATE NOT NULL, 
	    end_date DATE NOT NULL, 
	    account_id INTEGER NOT NULL, 
	    PRIMARY KEY (id), 
	    FOREIGN KEY(account_id) REFERENCES account (id)
    )

### Enrollments
    CREATE TABLE enrollments (
	    kurssi_id INTEGER NOT NULL, 
	    account_id INTEGER NOT NULL, 
	    PRIMARY KEY (kurssi_id, account_id), 
	    FOREIGN KEY(kurssi_id) REFERENCES kurssi (id), 
	    FOREIGN KEY(account_id) REFERENCES account (id)
    )

### Userinvoice
(tätä ei ole toteutettu sovelluksessa)
CREATE TABLE userinvoices (
	    invoice_id INTEGER NOT NULL, 
	    account_id INTEGER NOT NULL, 
	    PRIMARY KEY (invoice_id, account_id), 
	    FOREIGN KEY(invoice_id) REFERENCES invoice (id), 
	    FOREIGN KEY(account_id) REFERENCES account (id)
)
