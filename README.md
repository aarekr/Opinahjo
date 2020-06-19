# Kurssikeskus Opinahjo
Tsohan harjoitustyö, alkukesä 2020

--------

### Linkit

Heroku: [Opinahjo](https://opinahjo-105a.herokuapp.com/)

[Tietokantakaavio](https://github.com/aarekr/Opinahjo/blob/master/documentation/Tietokantakaavio.PNG)

[User storyt](https://github.com/aarekr/Opinahjo/blob/master/documentation/UserStoryt.md)

[Asennusohje](https://github.com/aarekr/Opinahjo/blob/master/documentation/Asennusohje.md)

[Käyttöohje](https://github.com/aarekr/Opinahjo/blob/master/documentation/Opinahjon%20k%C3%A4ytt%C3%B6ohje.pdf)

[CREATE TABLE -lauseet](https://github.com/aarekr/Opinahjo/blob/master/documentation/CREATE%20TABLE%20-lauseet.md)

--------

### Aihekuvaus
Kurssikeskus järjestää maksullisia (100 euroa/kpl) ohjelmoinnin kursseja. Jokaisen ohjelmointikielen kursseja on vuoden aikana useampia. Opiskelijat voivat ilmoittautua kursseille eikä esitietovaatimuksia ole. Koulun opetusohjelmasivulla on ilmoitettu tarjottavat kurssit, niiden opettajat ja ajat. Opiskelijan täytyy luoda lasku ja maksaa se osallistuakseen kurssille.


### Sovelluksen toiminnot
1. Kurssitarjonnan katselu ja kurssi-ilmoittautuminen
2. Käyttäjätilin rekisteröinti (vain opiskelija) ja kirjautuminen
3. Kurssin lisääminen opetusohjelmaan ja sen muokkaus (vain opettaja)
4. Omien kurssien (opiskelija) ja opetuksen (opettaja) tarkastelu
5. Ilmoittautuneiden ja kurssin maksaneiden opiskelijoiden luettelo (opettaja)
6. Kurssin peruutus ja opiskelijatilin poisto kurssikeskuksen toimesta
7. Ilmoittautumisen maksaminen ja peruutus opiskelijan toimesta


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
3. Kurssin ominaisuuksiin voisi lisätä opetuspaikan, tarkemman kuvauksen ja muita vastaavia tarpeen mukaan.
4. Osa auth-kansion models-tiedoston toiminnoista voisi siirtää kurssit-kansioon.
5. Oikean yläkulman Kirjaudu sisään / Rekisteröidy on toteutettu yhtenä linkkinä mutta sen voi halutessaan toteuttaa erillisinä.
5. Käyttäjän tietoihin voisi lisätä sähköpostiosoitteen ja muita tietoja.
6. Kursseja ja opiskelijoita poistettaessa opettajalta tulisi vielä varmistaa, että hän haluaa poistaa ko. tiedon.
7. Laskun maksu on sovelluksessa toteutettu klikkaamalla Maksa lasku-nappia. Tämän voisi muuttaa nettipankkiin kirjautumiseksi, korttitietojen kyselyksi ja muiksi maksuvaihtoehdoiksi.
8. Opiskelija voi luoda samasta kurssista useamman laskun. Tämä tulisi estää.
9. Autorisointia tulisi tarkentaa. Tällä hetkellä käyttäjillä pääsy joihinkin toimintoihin, joita ei ole tarkoitettu heille.
