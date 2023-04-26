# Informatyka projekt 1
___

Program służący do przeliczania współrzędnych w kilku możliwych 
kombinacjach na podstawie kilku możliwych elipsoidach. 
Koncepcja programu opiera się na wzorcu strategii oraz wstrzykiwaniu zależności,
gdzie podczas wywoływania trybu programu program sam będzie wybierał,
z którego algorytmu skorzystać poprzez wybranie klasy.
Poniżej znajdują się, te które są możliwe do wyboru.

* `GRS80`
* `WGS84`
* `Krassowski`

Stworzone na podstawie klasy Ellipse, która pozwala na ustawienie parametrów elipsoidy.

Jeśli chodzi o możliwości przeliczania, to są one następujące:
* BLH -> XYZ
* XYZ -> BLH
* XYZ -> NEU
* BL -> PL2000
* BL -> PL1992

Co definiuje już wzorzec strategii. Jest łatwy do rozszerzenia, ponieważ wystarczy by klasa dziedziczyła i implemenowała 
metody po klasie CoordinatesConverter w którą wstrzykuje się klasę Ellipse z ustawioną już konfiguracją (czyli wyborem konkretnej).

---
## Wymagania

By uruchomić projekt potrzebny jest:
* system Windows lub Linux (Ubuntu):
* Python 3.8
* numpy >= 1.24.2
* pytest >= 7.3.1 (w przypadku testowania programu)

---
## Instalacja
1. Przejdź do katalogu, w którym chcesz umieścić program
2. Pobierz projekt z repozytorium
```
git clone <link do repozytorium>
```

3. Zainstaluj wymagane biblioteki
```bash
$ pip install requirements.txt
```
4. By uruchomić test dodaj projekt do PYTHONPATH
* linux
```bash
$ export PYTHONPATH="${PYTHONPATH}:pwd"
```
  * windows
Polecane rozwiązanie [StackOverflow](https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages/32609129#32609129)
5. Uruchom testy
```bash
$ pytest
```

6. Korzystaj z programu
_Poniżej przedstawienie użytkowania_

---
## Użytkowanie

Program posiada różne argumenty, które są opisane w pomocy programu dostępnej pod komendą `-h`
```
$ python3 transform -h
```
Opisane są tam wymagane zmienne potrzebne do uruchomienia konkertnego trybu programu.

Program posiada 5 trybów. Dostepne pod argumentem `-M` lub `--mode`:
BLH2XYZ, XYZ2BLH, XYZ2NEU, BL1992, BL2000.
Który każdy przyjmuje parametry w radianach lub metrach.

Następnie należy wybrać elpsoidę. Dostępne pod argumentem `-S` lub `--system`:
GRS80, WGS84, krasovsky

### Przykłady użycia:

BLH2XYZ
```
$ python3 -m transform -M BLH2XYZ -S GRS80 -B 1 -L 1 -H 100
(1866405.5962884608, 2906754.4929987877, 5343852.592872608)
```

BL2000
```
$ python3 -m transform -M BL2000 -S krasovsky -B 1 -L 1
(7029453.224954397, 2723782.6716693556)
```

Dla plików tekstowych:
Wejście:
```
XYZ2BLH;GRS80
Nr;B;L;H
1;1;1;1
2;2;2;2
3;3;3;3
```
Program:
```
python3.10 -m transform -M XYZ2BLH -S GRS80 -inp test.csv -out out.csv
```

Wyjście:
```
XYZ2BLH;GRS80
Nr;B;L;H
1;1.565865999699094;0.7853981633974484;-6399591.682536514
2;1.5609698144496085;0.7853981633974484;-6399588.695663288
3;1.5561073086928905;0.7853981633974483;-6399584.686930775
```

Problemy które nie zostały dopracowane:
* Program nie rozróżnia które argumenty do których trybów, zatem może przekazywać błędne
* Program nie sprawdza czy plik wejściowy jest poprawny
* Program nie definiuje jednostek w jakich podajemy dane

