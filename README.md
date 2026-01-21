# Object-Oriented Programming in Python - Drink Management System

Ein umfassendes Projekt zur Demonstration von OOP-Konzepten in Python, einschliesslich Klassendefinition, Vererbung, Polymorphismus und Komposition.

---

## Inhaltsverzeichnis

1. [Projektubersicht](#projektubersicht)
2. [Klassenstruktur](#klassenstruktur)
3. [Detaillierte Klassenbeschreibung](#detaillierte-klassenbeschreibung)
4. [Beispiele](#beispiele)
5. [OOP-Konzepte](#oop-konzepte)
6. [Installation und Ausfuhrung](#installation-und-ausfuhrung)

---

## Projektubersicht

Dieses Projekt simuliert ein **Getranke-Management-System** mit Automaten. Es demonstriert die vier Saulen der objektorientierten Programmierung:

- **Kapselung (Encapsulation)**: Daten und Methoden werden in Klassen gebundelt
- **Vererbung (Inheritance)**: Spezialisierte Getrankeklassen erben von der Basisklasse
- **Polymorphismus (Polymorphism)**: Verschiedene Objekte reagieren unterschiedlich auf dieselben Methodenaufrufe
- **Komposition (Composition)**: Der Automat enthalt und verwaltet Getranke-Objekte

---

## Klassenstruktur

```
                           Drink (Basisklasse)
                                  |
            +----------+----------+----------+----------+
            |          |          |          |          |
         Juice    DataCola   EnergyDrink   Water    (weitere...)
            
                    VendingMachine
                          |
              [enthalt Drink-Objekte]
```

### UML-Diagramm

```
+------------------+       +------------------+
|      Drink       |       |  VendingMachine  |
+------------------+       +------------------+
| - volume: int    |       | - content: list  |
| - expiration: int|       | - size: int      |
+------------------+       | - name: str      |
| + next_day()     |       +------------------+
| + is_expired()   |<------| + add()          |
| + __str__()      |       | + remove()       |
+------------------+       | + verify()       |
         ^                 | + next_day()     |
         |                 | + get_inventory()|
    +----+----+            | + find_by_type() |
    |    |    |            | + total_volume() |
+-------++-------+         +------------------+
| Juice || Data  |
|       || Cola  |
+-------++-------+
```

---

## Detaillierte Klassenbeschreibung

### 1. Drink (Basisklasse)

Die Grundlage fur alle Getranketypen.

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `volume` | int | Volumen in Millilitern |
| `expiration` | int | Tage bis zum Ablaufdatum |

| Methode | Ruckgabe | Beschreibung |
|---------|----------|--------------|
| `__init__(volume, expiration)` | None | Konstruktor |
| `next_day()` | None | Reduziert Ablaufdatum um 1 |
| `is_expired()` | bool | Pruft auf Ablauf |
| `__str__()` | str | String-Darstellung |
| `__repr__()` | str | Debug-Darstellung |

```python
class Drink:
    def __init__(self, volume: int, expiration: int):
        self.volume = volume
        self.expiration = expiration
    
    def next_day(self):
        if self.expiration > 0:
            self.expiration -= 1
    
    def is_expired(self) -> bool:
        return self.expiration <= 0
```

---

### 2. Juice (Subklasse)

Fruchtsafte mit festem Ablaufdatum von 7 Tagen.

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `volume` | int | Geerbt von Drink |
| `expiration` | int | Immer 7 Tage |
| `fruit_type` | str | Fruchtsorte |

```python
class Juice(Drink):
    DEFAULT_EXPIRATION = 7
    
    def __init__(self, volume: int, fruit_type: str = "Mixed"):
        super().__init__(volume, self.DEFAULT_EXPIRATION)
        self.fruit_type = fruit_type
```

---

### 3. DataCola (Subklasse)

Cola-Getranke mit containerabhangigen Eigenschaften.

| Container | Volumen | Haltbarkeit |
|-----------|---------|-------------|
| `'can'` | 330mL | 60 Tage |
| `'bottle'` | 500mL | 30 Tage |

```python
class DataCola(Drink):
    CONTAINER_SPECS = {
        'can': {'volume': 330, 'expiration': 60},
        'bottle': {'volume': 500, 'expiration': 30}
    }
    
    def __init__(self, container: str):
        specs = self.CONTAINER_SPECS[container]
        super().__init__(specs['volume'], specs['expiration'])
        self.container = container
```

---

### 4. EnergyDrink (Subklasse)

Energiegetranke mit Koffeingehalt.

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `caffeine_mg` | int | Koffein in mg |
| `sugar_free` | bool | Zuckerfrei? |

```python
class EnergyDrink(Drink):
    def __init__(self, volume: int, expiration: int, 
                 caffeine_mg: int = 80, sugar_free: bool = False):
        super().__init__(volume, expiration)
        self.caffeine_mg = caffeine_mg
        self.sugar_free = sugar_free
```

---

### 5. Water (Subklasse)

Wasser mit langer Haltbarkeit (365 Tage).

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `sparkling` | bool | Mit Kohlensaure? |

```python
class Water(Drink):
    DEFAULT_EXPIRATION = 365
    
    def __init__(self, volume: int, sparkling: bool = False):
        super().__init__(volume, self.DEFAULT_EXPIRATION)
        self.sparkling = sparkling
```

---

### 6. VendingMachine

Verwaltet eine Sammlung von Getranken.

| Methode | Beschreibung |
|---------|--------------|
| `add(drink)` | Fugt Getrank hinzu |
| `remove(i)` | Entfernt Getrank an Index i |
| `verify()` | Entfernt abgelaufene Getranke |
| `next_day()` | Lasst alle Getranke altern |
| `get_inventory()` | Inventarzusammenfassung |
| `find_by_type(type)` | Sucht nach Typ |
| `total_volume()` | Gesamtvolumen |

---

## Beispiele

### Beispiel 1: Grundlegende Verwendung

Erstellen und Manipulieren von Getranke-Objekten.

```python
# Verschiedene Getranke erstellen
basic_drink = Drink(500, 10)
orange_juice = Juice(1000, "Orange")
cola_can = DataCola('can')

# Getranke anzeigen
print(basic_drink)   # Drink: 500mL, expires in 10 days
print(orange_juice)  # Juice (Orange): 1000mL, expires in 7 days
print(cola_can)      # DataCola: 330mL, expires in 60 days, in a can

# Zeit simulieren
basic_drink.next_day()
print(basic_drink)   # Drink: 500mL, expires in 9 days
```

**Ausgabe:**
```
--- Creating Drinks ---
  Drink: 500mL, expires in 10 days
  Juice (Orange): 1000mL, expires in 7 days
  Juice (Apple): 750mL, expires in 7 days
  DataCola: 330mL, expires in 60 days, in a can
  DataCola: 500mL, expires in 30 days, in a bottle

--- Simulating 3 Days Passing ---
Day 1:
  Drink: 500mL, expires in 9 days
  Juice (Orange): 1000mL, expires in 6 days
  ...
```

---

### Beispiel 2: Automaten-Operationen

Vollstandige CRUD-Operationen mit dem VendingMachine.

```python
# Automat erstellen
vm = VendingMachine(6, "Campus Automat")

# Getranke hinzufugen
vm.add(Drink(350, 5))
vm.add(Juice(500, "Grape"))
vm.add(DataCola('can'))
vm.add(EnergyDrink(250, 30, 150, True))
vm.add(Water(500, True))

# Inventar anzeigen
print(vm.get_inventory())  # {'Drink': 1, 'Juice': 1, 'DataCola': 1, ...}

# Woche simulieren und abgelaufene entfernen
for _ in range(7):
    vm.next_day()
vm.verify()  # Entfernt abgelaufene Getranke
```

**Ausgabe:**
```
--- Stocking the Vending Machine ---
Added Drink: 350mL, expires in 5 days to Campus Automat.
Added Juice (Grape): 500mL, expires in 7 days to Campus Automat.
Added DataCola: 330mL, expires in 60 days, in a can to Campus Automat.

--- Inventory Summary ---
  Drink: 1
  Juice: 1
  DataCola: 2
  EnergyDrink: 1
  Water: 1
  Total Volume: 2930mL
```

---

### Beispiel 3: Automaten-Netzwerk

Verwaltung mehrerer Automaten als Netzwerk.

```python
# Netzwerk erstellen
machines = [
    VendingMachine(5, "Bibliothek"),
    VendingMachine(8, "Cafeteria"),
    VendingMachine(4, "Fitnessstudio")
]

# Unterschiedliche Bestuckung
machines[0].add(Water(500))        # Bibliothek: Ruhige Getranke
machines[1].add(DataCola('can'))   # Cafeteria: Vielfalt
machines[2].add(EnergyDrink(250, 60, 200, True))  # Gym: Energie

# Netzwerk-Statistiken
total_drinks = sum(len(m) for m in machines)
total_volume = sum(m.total_volume() for m in machines)
```

**Ausgabe:**
```
--- Network Statistics ---
  Total Machines: 3
  Total Drinks: 14
  Total Capacity: 17
  Utilization: 82.4%
  Total Volume: 6830mL (6.8L)

--- Weekly Maintenance Check ---
Removed 1 expired drink(s) from Cafeteria Machine.
Total expired drinks removed: 1
```

---

### Beispiel 4: Polymorphismus-Demonstration

Zeigt, wie verschiedene Objekte einheitlich behandelt werden.

```python
# Gemischte Sammlung
drinks = [
    Drink(500, 3),
    Juice(750, "Mango"),
    DataCola('can'),
    EnergyDrink(250, 5, 120, True),
    Water(1000, False)
]

# Polymorphes Verhalten
for drink in drinks:
    print(drink)  # Jede Klasse hat eigene __str__ Implementierung
    drink.next_day()  # Gleiche Methode, gleiches Verhalten (geerbt)
```

**Ausgabe:**
```
--- Polymorphic Behavior ---
All drinks respond to the same methods differently:

  Type: Drink           | Drink: 500mL, expires in 3 days
  Type: Juice           | Juice (Mango): 750mL, expires in 7 days
  Type: DataCola        | DataCola: 330mL, expires in 60 days, in a can
  Type: EnergyDrink     | EnergyDrink (Sugar-Free): 250mL, 120mg caffeine
  Type: Water           | Water (Still): 1000mL, expires in 365 days

--- Inheritance Chain ---
  Drink inherits from: object
  Juice inherits from: Drink
  DataCola inherits from: Drink
  EnergyDrink inherits from: Drink
  Water inherits from: Drink
```

---

## OOP-Konzepte

### Zusammenfassung der implementierten Konzepte

| Konzept | Implementierung | Beispiel |
|---------|-----------------|----------|
| **Kapselung** | Attribute und Methoden in Klassen | `Drink.volume`, `Drink.next_day()` |
| **Vererbung** | Subklassen erben von Basisklasse | `Juice(Drink)`, `DataCola(Drink)` |
| **Polymorphismus** | Gleiche Methode, verschiedenes Verhalten | `__str__()` in jeder Klasse |
| **Komposition** | Objekte enthalten andere Objekte | `VendingMachine.content` |
| **Abstraktion** | Komplexitat verstecken | `vm.verify()` versteckt Logik |
| **Klassenkonstanten** | Geteilte Werte | `Juice.DEFAULT_EXPIRATION = 7` |
| **Type Hints** | Typsicherheit | `def add(self, drink: Drink)` |
| **Dunder Methods** | Python Magic Methods | `__str__`, `__repr__`, `__len__` |

---

## Installation und Ausfuhrung

### Voraussetzungen

- Python 3.6 oder hoher

### Ausfuhrung

```bash
# Klone das Repository
git clone https://github.com/DEIN_USERNAME/oop-drink-system.git
cd oop-drink-system

# Fuhre das Programm aus
python drinks.py
```

### Erwartete Ausgabe

```
######################################################################
#                                                                    #
#  OBJECT-ORIENTED PROGRAMMING - DRINK MANAGEMENT SYSTEM             #
#                                                                    #
######################################################################

======================================================================
EXAMPLE 1: Basic Usage - Creating and Managing Drinks
======================================================================
...
```

---

## Programmierbeschreibung

### Entwicklungsansatz

Bei der Entwicklung dieses Projekts wurde ein systematischer Ansatz verfolgt:

1. **Analyse der Anforderungen**: Zuerst wurden die Grundanforderungen (Drink-Klasse mit Attributen und Methoden) identifiziert.

2. **Basisklasse zuerst**: Die `Drink`-Klasse wurde als solide Grundlage mit allen gemeinsamen Eigenschaften implementiert.

3. **Schrittweise Erweiterung**: Subklassen wurden nacheinander hinzugefugt, wobei jede ihre eigene Spezialisierung mitbrachte.

4. **Komposition fur Komplexitat**: Die `VendingMachine`-Klasse zeigt, wie Objekte andere Objekte verwalten konnen.

5. **Dokumentation**: Jede Klasse und Methode wurde mit Docstrings dokumentiert.

### Best Practices

- **Type Hints**: Verbessern die Lesbarkeit und ermoglichen IDE-Unterstutzung
- **Docstrings**: Jede Klasse und Methode ist dokumentiert
- **Klassenkonstanten**: Vermeiden Magic Numbers im Code
- **Fehlerbehandlung**: `ValueError` bei ungualtigen Eingaben
- **Clean Code**: Klare Namensgebung und strukturierter Aufbau

---

## Lizenz

Dieses Projekt wurde im Rahmen einer Einfuhrung in die objektorientierte Programmierung erstellt.

---

## Autor: Bekir Yagan ( Krefeld, NRW, GERMANY)

OOP Exam Project - Introduction to Object-Oriented Programming
