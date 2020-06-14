# Asennusohje

### Asentaminen omalle koneelle

Sovellus pyörii python3 ympäristössä.

Kloonaa projekti koneellesi komennolla
    git clone https://github.com/aarekr/Opinahjo.git

Asenna projektin riippuvuudet
    pip install -r requirements.txt

Projekti käynnistyy komennolla
    python run.py

Sovellus käynnistyy osoitteessa
    http://http://localhost:5000/

### Sovelluksen siirto Herokuun

Luo Heroku -sovellus komennolla
    heroku create <sovelluksen nimi>

Lisää Heroku remote paikalliseen git repositorioosi
    git remote add heroku <sovelluksesi osoite>

Lisää vaaditut ympäristömuuttujat Herokuun
    heroku config:set HEROKU=!

Lisää Postgres -tietokanta Herokuun
    heroku addons:add heroku-postgresql:hobby-dev

Commitoi ja pushaa koodi Herokuun
    git add .
    git commit -m "Siirto Herokuun"
    git push heroku master
