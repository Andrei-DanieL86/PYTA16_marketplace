# Sesiunea 24 - Django PART 2

## 📝 Obiective
- Creare modelelor
- Creare si aplicare migrari de baza de date
- Creare rutelor
- Interactiunea cu panoul de admin
- Renderizarea template-urilor HTML
- Stilizarea template-urilor HTML cu CSS si Bootstrap
- Jinja


## 📌 Partea practica sesiunea 24
- In cadrul acestei sesiuni, vom continua marketplace-ul
inceput in sesiunea 23:
  - vom crea modelul pentru products
  - vom crea si aplica migrari de baza de date
  - vom crea, actualiza, sterge produse din panoul de admin
  - vom crea rutele de acces lista produse, produs individual
  - vom renderiza template-uri HTML stilizate cu CSS si Bootstrap
  - vom vedea cum functioneaza Jinja

## 📌 Crearea modelelor
- Pentru a crea modele in baza de date, se vor actualiza fisierele
```models.py``` aflate in interiorul aplicatiilor disponibile
in proiectul Django.

- Fiecare model se defineste ca o clasa, care mosteneste din
clasa ```Models``` disponibila in ```django.db.models```.
- Campurile asociate fiecarui model reprezinta atribute de clasa
care sunt instante ale claselor de tip Field (CharField, ImageField, DecimalField etc.)

## 📌 Activarea modelelor
- Pentru ca modelele dintr-o aplicatie sa fie incluse
in proiectul Django, trebuie sa adaugam o referinta catre clasa de configurare
a aplicatiei respective in constanta ```INSTALLED_APPS``` din ```settings.py``` de la nivelul proiectului Django.
- Aceasta clasa de configurare se gaseste in fisierul ```apps.py``` de la nivelul
aplicatiei create

## 📌 Migrari baza de date
- Generarea actualizarilor/migrarilor:
```python manage.py makemigrations marketplaceapp```
- Vizualizarea migrarii:
```python manage.py sqlmigrate marketplaceapp 0001```
- Aplicarea migrarilor:
```python manage.py migrate```

## 📌 Creare user admin + accesare si explorare panou admin
- In Django, avem acces la un panou de admin, in care
putem interactiona cu modelele noastre din baza de date.
- Din acest panou, ca admin, vom putea sa adaugam, stergem, actualizam
diferite modele.
- Pentru a accesa panoul de admin, avem nevoie sa configuram
un user de admin: ```python manage.py createsuperuser``` (seteaza un username, adresa de mail si parola)
- Porneste aplicatia: ```python manage.py runserver```
- Acceseaza ruta/admin si logheaza-te.

- Pentru a putea edita/gestiona un model din panoul de admin, trebuie sa actualizam
fisierul ```admin.py```, inregistrand modelul dorit.

## 📌 Crearea view-urilor si renderizare template-uri
- https://docs.djangoproject.com/en/4.2/intro/tutorial03/#write-views-that-actually-do-something

## 📌 Stilizare templates
- https://docs.djangoproject.com/en/4.2/intro/tutorial06/#customize-your-app-s-look-and-feel

