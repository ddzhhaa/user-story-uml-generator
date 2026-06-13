# História promptov

## Verzia 1 – Základný prompt

### Prompt

Convert these user stories into a UML use case diagram in PlantUML format.

### Dôvod

Na začiatku projektu som chcel overiť, či dokáže jazykový model vytvoriť UML use case diagram iba na základe používateľských požiadaviek (user stories).

### Výsledok

Model vytvoril základné diagramy, avšak:

* diagramy boli veľmi jednoduché,
* nevytvárali sa vzťahy include alebo extend,
* model nevykonával hlbšiu analýzu požiadaviek.

### Záver

Bolo potrebné vytvoriť štruktúrovanejší prompt.

---

## Verzia 2 – Použitie frameworku ROSES

### Zmeny

Prompt bol prepracovaný podľa frameworku ROSES.

Boli pridané časti:

* Role
* Objective
* Scenario
* Expected Output
* Steps

### Dôvod

Vedúci práce odporučil používať štruktúrovaný prompt a framework ROSES.

### Výsledok

Model začal generovať komplexnejšie diagramy a pokúšal sa identifikovať vzťahy medzi jednotlivými use cases.

### Problém

Model niekedy vytváral dedičnosť (inheritance) medzi use cases, čo nebolo požadované.

### Záver

Bolo potrebné spresniť pravidlá pre generovanie diagramov.

---

## Verzia 3 – Obmedzenie dedičnosti a definovanie syntaxe include

### Zmeny

Do promptu boli pridané pravidlá:

* nepoužívať dedičnosť medzi use cases,
* používať vzťah include iba vo forme:

MainUseCase .> IncludedUseCase : <<include>>

### Dôvod

Model generoval neplatnú syntax PlantUML alebo nevhodné vzťahy medzi use cases.

### Výsledok

Diagramy boli syntakticky správnejšie.

### Problém

Model začal vytvárať nové use cases zo sekcie „so that“.

Príklad:

As a software developer, I want to integrate third-party authentication so that users can log in using Google or Facebook.

Model vytvoril use cases:

* Log In Using Google
* Log In Using Facebook

Aj keď tieto činnosti nevykonáva aktér Software Developer.

### Záver

Bolo potrebné lepšie definovať spôsob identifikácie aktérov a use cases.

---

## Verzia 4 – Presnejšia interpretácia aktérov

### Zmeny

Do promptu boli pridané pravidlá:

* aktér sa určuje podľa časti „As a ...“,
* hlavný use case sa určuje podľa časti „I want to ...“,
* nevytvárať nové use cases z časti „so that“, pokiaľ nejde o akciu toho istého aktéra,
* používať aliasy pre všetky use cases.

Príklad:

usecase "Refactor Legacy Code" as UC1

Actor --> UC1

### Dôvod

Model vytváral:

* duplicitných aktérov,
* neplatnú syntax PlantUML,
* use cases, ktoré nesúviseli s daným aktérom.

### Výsledok

Generované diagramy sa stali:

* syntakticky korektné,
* jednoduchšie,
* bližšie pôvodným user stories.

### Súčasný stav

Verzia 4 je aktuálne používaná v projekte, pretože poskytuje najstabilnejšie a najpresnejšie výsledky pri generovaní UML use case diagramov.

## Verzia 5 – Zlučovanie podobných aktérov a kontrola include vzťahov

### Problém

Pri testovaní promptu na doméne Food Delivery App model vytvoril viacero veľmi podobných aktérov:

- User
- Customer
- Signed-up User
- Returning Customer
- Shopper

Títo aktéri mali v danej doméne podobný význam, preto diagram pôsobil zbytočne komplikovane.

### Zmena

Do promptu bolo pridané pravidlo, aby model zlučoval podobných aktérov do všeobecnejšieho aktéra.

Príklad:

User, Customer, Signed-up User, Returning Customer a Shopper môžu byť v doméne Food Delivery App reprezentovaní ako jeden aktér Customer.

### Výsledok

Po úprave promptu model vytvoril jednoduchší diagram s jedným hlavným aktérom Customer. Diagram bol prehľadnejší a lepšie čitateľný.

### Dodatočné overenie

Upravený prompt bol následne manuálne otestovaný aj na ďalších doménach:

- Security
- Web Application
- Analytics & Reporting
- Testing & QA
- Onboarding & Training
- Functionality Features

Pri týchto doménach neboli zistené nové závažné problémy.

V doméne Functionality Features model správne vytvoril include vzťah medzi use cases Reset Password a Reset Password via Email, čo považujem za rozumné použitie include vzťahu.

### Záver

Verzia 5 je aktuálne najlepšia verzia promptu, pretože vytvára čitateľné diagramy, zlučuje podobných aktérov a používa include vzťahy iba v prípadoch, kde sú logicky odôvodnené.