# Proiect Baze de date
### _UPB ACS 2023_

Proiectul realizat la baze date, fiind implementata o interfata grafica ce este conectata la o baza de date in MySQL. 

Interfata are scop gestionarea masinilor clientilor dintr-un service auto. 

Proiectul se ruleaza folosind comanda:
``python MainPageGUI.py``

## Functii

- Baza de date este formata din 10 tabele, cu diverse tipuri de legaturi _(many-to-many, one-to-one, one-to-many )_
- Posibilitatea de a manipula datele a 3 tabele folosind modelul *CRUD* _(Create, Read, Update, Delete)_
- Interfata are 4 pagini ce interogheaza baza de date cu un set de query-uri complexe


## Prerequisites

- Python 3.x
- MySQL Connector pentru Python
- Tkinter
>**_NOTA:_** Librariile pot fi instalate ruland utilitarul pip fisierul _requirements.txt_
>``pip install -r requirements.txt``