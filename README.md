# Kurssikeskus Opinahjo
Tsohan harjoitustyö, alkukesä 2020

--------

### Linkit

Heroku: [Opinahjo](https://opinahjo-105a.herokuapp.com/)

[Tietokantakaavio](https://github.com/aarekr/Opinahjo/blob/master/documentation/Tietokantakaavio.pdf)

[User storyt](https://github.com/aarekr/Opinahjo/blob/master/documentation/UserStoryt.md)

[Käyttöohje](https://github.com/aarekr/Opinahjo/blob/master/documentation/Opinahjon%20k%C3%A4ytt%C3%B6ohje.pdf)

[CREATE TABLE -lauseet](https://github.com/aarekr/Opinahjo/blob/master/documentation/CREATE%20TABLE%20-lauseet.md)

--------

### Aihekuvaus
Kurssikeskus järjestää maksullisia ohjelmoinnin kursseja. Jokaisen ohjelmointikielen kursseja on vuoden aikana useampia. Joidenkin kurssien osallistumismäärä on rajoitettu 20 opiskelijaan, toisilla rajoituksia ei ole. Kursseista on laadittu esitteet, joista selviävät ajat ja opettajat. Kuka tahansa voi ilmoittautua kursseille. Ilmoittautuneiden täytyy maksaa varausmaksu. Tarkemmat maksutiedot lähetetään ilmoittautumisen jälkeen. Ilmoittautunut saa halutessaan laskun.

### Sovelluksen toiminnot
1. Kurssitarjonnan katselu ja kurssipaikan varaaminen
2. Käyttäjätilin rekisteröinti (vain opiskelija) ja kirjautuminen
3. Kurssin syöttö ja muokkaus (vain opettaja)
4. Omien kurssien (opiskelija) ja opetuksen (opettaja) tarkastelu
5. Ilmoittautuneiden luettelo (opettaja)
6. Varauksen peruutus kurssikeskuksen toimesta, jos maksua ei ole maksettu
7. Ilmoittautumisen peruutus opiskelijan toimesta
8. Kurssin peruutus


### Testitunnukset
Luo aluksi 2 opettajatunnusta ja lisää kursseja opetusohjelmaan.
Luo tämän jälkeen haluamasi määrä opiskelijoita.

Huom! Opettajatilin voi luoda tästä: https://opinahjo-105a.herokuapp.com/teacher (linkkiä ei tarkoituksella löydy sovelluksesta)
      Opiskelijatilin voi luoda rekisteröidy-linkin kautta.

1. opettaja-tunnukset: opettaja 1 ja opettaja 2, salasana: sala
2. opiskelija-tunnukset: opisk 1, opisk 2 ja opisk 3, salasana: ak


### Jatkokehitysideat ja puuttuvat ominaisuudet
1. Yhtenä merkittävänä puutteena on suomen ja englannin sekakäyttö nimeämisissä. Tämä tulisi yhtenäistää vaikka muutos on joissakin kohdissa työläs.
2. Nimi ja käyttäjätunnus käsitellään sovelluksessa samana mutta ne voisi eriyttää ts. kysyä käyttäjätilin rekisteröinnin yhteydessä molempia.
3. Kurssin ominaisuuksiin voisi lisätä opetuspaikan, hinnan, tarkemman kuvauksen ja muita vastaavia tarpeen mukaan.
4. Osa auth-kansion models-tiedoston toiminnoista voisi siirtää kurssit-kansioon
5. Oikean yläkulman Kirjaudu sisään / Rekisteröidy on toteutettu yhtenä linkkinä mutta sen voi halutessaan toteuttaa kahtena eri linkkinä.
5. Käyttäjän tietoihin voisi lisätä sähköpostiosoitteen ja muita tietoja.
