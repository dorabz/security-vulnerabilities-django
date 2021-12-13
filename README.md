# Napredni-razvoj-programske-potpore-za-web---2.projekt


url na Heroku: https://site-with-vulnerabilities.herokuapp.com/  , tehnologije: Python Django

ostvarene ranjivosti: 
- Nesigurna pohrana osjetljivih podataka (Sensitive Data Exposure)
- Loša kontrola pristupa (Broken Access Control)

upute: 
(korisničko sučelje je opremljeno uputama)

Potrebno je registrirati se ili koristiti već napravljen račun: username:password == santa:ilovechristmaspresents3
Home - upute za pokretanje ranjivosti i stranice koja je sigurna
Sensitive Data Exposure - upute za simulaciju ove ranjivosti 
Broken Access Control - upute za simulaciju ove ranjivosti 
logout - odjava sa prijavljenog računa

*za lokalno pokretanje potrebno je imati instaliran pip i aktivirati virtualno okruženje , nakon tog 
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver

-> app dostupna na http://127.0.0.1:8000

napomena: zad je ranjiva stranica, zad-fix je sigurna stranica
