# Käyttötapaukset ja SQL-kyselyt

### VIERAILIJA, OPISKELIJA, OPETTAJA

Sivulla kävijänä voin listata koulun tarjoamat kurssit ja niiden tarkemmat tiedot. (valmis)

    SELECT Kurssi.id, Kurssi.name, Kurssi.start_date, Kurssi.end_date, Account.name 
    FROM Kurssi, Account
    WHERE Kurssi.account_id = Account.id

### OPISKELIJA

Opiskelijana voin luoda käyttäjätunnuksen nimelläni. (valmis)

    INSERT INTO Account (name, username, password, student, teacher, user_role) VALUES (?, ?, ?, ?, ?, ?)

Opiskelijana voin ilmoittautua kurssille varaamalla paikan. (valmis)

    INSERT INTO enrollments (kurssi_id, account_id) VALUES (?, ?)

Opiskelijana voin listata kaikki kurssit, joille olen ilmoittautunut. (valmis)

    SELECT Kurssi.id, Kurssi.name, Account.name
    FROM Account, Kurssi, enrollments
    WHERE Account.id = enrollments.account_id
    AND Kurssi.id = enrollments.kurssi_id
    ORDER BY Kurssi.name

Opiskelijana voin maksaa kurssin, jolle olen ilmoittautunut. (valmis)

    UPDATE Invoice SET paid=True WHERE id=?

Opiskelijana voin perua kurssi-ilmoittautumiseni. (valmis)

    DELETE FROM enrollments WHERE kurssi_id=?, account_id=?


### OPETTAJA

Opettajana voin lisätä uuden kurssin opetusohjelmaan. (valmis)

    INSERT INTO Kurssi (name, start_date, end_date) VALUES (?, ?, ?)

Opettajana voin muokata kurssini tietoja. (valmis)

    UPDATE Kurssi SET name=?, start_date=?, end_date=? WHERE id=?

Opettajana voin poistaa kurssini opetusohjelmasta. (valmis)

    DELETE FROM Kurssi WHERE id=?

Opettajana voin listata kurssit, joita opetan. (valmis)

    SELECT Kurssi.id, Kurssi.name, Kurssi.account_id
    FROM Kurssi
    LEFT JOIN Account ON Account_id = Account.id

Opettajana voin listata opiskelijani kursseillani. (valmis)

    SELECT Account.name, Kurssi.name, Kurssi.account_id
    FROM Kurssi, Account, enrollments
    WHERE Account.id=enrollments.account_id AND Kurssi.id=enrollments.kurssi_id
    ORDER BY Kurssi.name

Opettajana voin listata kaikki kurssit ja niiden opiskelijamäärät. (valmis)

    SELECT Kurssi.name, COUNT(Account.id)
    FROM Account, Kurssi, enrollments
    WHERE Kurssi.id=enrollments.kurssi_id AND Account.id=enrollments.account_id
    GROUP BY Kurssi.id

Opettajana näen kuinka monelle kurssille kukin opiskelija on ilmoittautunut. (valmis)

    SELECT Account.name, COUNT(Kurssi.id), Account.student
    FROM Account
    LEFT JOIN Enrollments ON Account.id=enrollments.account_id
    LEFT JOIN Kurssi ON Kurssi.id=enrollments.kurssi_id
    GROUP BY Account.id

Opettajana näen ketkä opiskelijoistani ovat maksaneet kurssinsa. (valmis)

    SELECT Invoice.id, Invoice.kurssi_id, Invoice.paid, Invoice.account_id, Account.name
    FROM Invoice, Account
    WHERE Invoice.account_id = Account.id

Opettajana voin muokata opiskelijatilin tietoja. (valmis)

    UPDATE Account SET username=? WHERE id=?

Opettajana voin poistaa opiskelijatilin. (valmis)

    DELETE FROM Account WHERE id=?
