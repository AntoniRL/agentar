# AGENTAR

AGENTAR to lekki, strukturalny język programowania agentowego, oparty na hierarchicznej komunikacji i koncepcji autonomicznych jednostek wykonujących zadania.

## Kluczowe założenia

* Każdy agent ma unikalne, automatycznie nadawane `id` w formacie kropkowym: `.1`, `.1.2`, `.1.2.1`, itd.
* Ułątwiona komunikacja do: **rodzica**, **dzieci** i **braci**.
* Agenci mają cykl życia: `initialize` → pętla działania → `destroy`
* System oparty na komunikatach (wiadomościach) i reaktywnych regułach.
* Dostęp do pól agenta poprzez `self.name`
* Agent matka `mother` (Tworzony jako pierwszy, zarządza działaniem systemu)
* Agent czas `time` `id=.0` (Zarządza czasem- towrzony podczas inicjalizacji systemu, kiedy agent poprosi udostępnia aktualny czas `get_time()`)
* Koniec działania systemu kiedy agent matka wywoła `kill()` LUB minie czas symulacji (parametr podczas uruchomienia)

---

## Cykl życia agenta

1. `initialize` — konfiguracja i inicjalizacja (np. tworzenie dzieci)
2. Pętla działania:
   - aktualizacja przekonań (`beliefs`). Według instrukcji z `sense`
   - odbiór pierwszej wiadomości `receive` (jeżeli jakieś w inbox)
   - sprawdzenie celu (`goles`)
   - jeżeli cel nie osiąfnięty:
        - postępowanie zgodnie z regułami (`rules`) 
3. `destroy` — sprzątanie przed śmiercią

Agent umiera, gdy:
- wywoła `kill()`
- jego rodzic go zlikwiduje
- przy kończeniu działania rodzica wszysy jego potomkowie zostają zabici

## Struktura agenta

Wszystkie pola są obcjonalne. UWAGA: ważna kolejność występowania!!!

```agentar
agent mother {
    // Agent matka uruchamiany podczas wywołania programu. On uruchamia pozostałych agentów. Struktura jak zwykłego agenta (zarezerwowana nazwa mother)
}

agent <agent_name> {
    fields {
        // Pola wbudowane (opcjonalne; tylko jedna instancja)
        <type> <name> = <value>;     // np. int counter = 0;
    }

    initialize {
        // Kod uruchamiany przy starcie agenta (opcjonalne; tylko jedna instancja)
        // np. print("Hello!");
    }

    destroy {
        // Kod uruchamiany przy śmierci agenta (opcjonalne; tylko jedna instancja)
        // np. print("Bye!");
    }

    beliefs {
        // Przekonania agenta o świecie (opcjonalne; tylko jedna instancja)
        // np. bool b1 = false;
        // np. int b2;
    }

    sense {
        // Agent cyklicznie sprawdza świat zgodnie z zapisanymi akcjami (w zależnośći od speocyfiki świata) i atualizuje pola beliefs (opcjonalnie; tylko jedna instancja)
        // np. read_file()....
    }

    goals {
        // Cele agenta (opcjonalne; tylko jedna instancja)
        // np. g1: b.b1 == true || b.b2 < 4;
        // np. g2: b.b2 < 10;
    } marge (g1 && g2) //możliwość połączenia celów w dowolny sposób. Jeżeli brak to AND między celami cząstkowymi.

    rules {
        // Zasady postępowania agenta (opcjonalne; tylko jedna instancja)
        when <condition> then {
            <statements>;
        }
    }

    receive <msg_name> {
        // Instrukcje po otrzumaniu wiadomości typu <msg_name> (opcjonalnie; możliwe wiele instancji)
        when <condition> then {
            <statements>;
        }
    }

    action <name>(<args>): <return_type> {
        // Dfinicja akcji, które może podjąc agent (możliwość wywołania z poziomu bytu agenta) (opcjonalnie; możliwe wiele instancji)
        <statements>;
    }
}
```

# Opis składni

### Sekcje agenta

| Słowo kluczowe          | Opis                                         |
| ----------------------- | -------------------------------------------- |
| `agent`                 | Definicja agenta |
| `fields`                | Pola - głównie wbudowane ale również można zdefiniować swoje    |
| `initialize`            | Inicjalizacja - część wykonywana podczas inicjalizacji agenta |
| `destroy`               | Zniszczenie - część wykonywana po śmierci agenta |
| `beliefs`               | Przekonania - co agent uważa, że wie o świecie. Pochodzą z wiadomości lub sensorów. Typ danych `map` |
| `sense`                 | Definicja w jaki sposób będziemy czytać świat |
| `goals`                 | Cele - Co agent chce osiągnąć. Kierują działaniem agenta.   |
| `rules`                 | Zasady - Kiedy coś się stanie wykonaj akcję. |
| `receive`               | Otrzymywać - Kroki podjętet po otrzymaniu konkretnej wiadomości |
| `actions`               | Akcja - reprezentuje konkretne dostępne zadania |
| `message`               | Definicja typu wiadomości  |


### Wbudowane pola agenta

Dostęp do przekonań (`beliefs`) poprzed odwołanie `bel.<nazwa_pola>`
Wbudowane pola agenta zaczynają się od `_` np. `self._<nazwa pola>`

| Pole                      | Opis                                         |
| ------------------------- | -------------------------------------------- |
| `self._id`                 | ID agenta np. `.1.2.1`                       |
| `self._parent`             | ID rodzica np. `.1.2`                        |
| `self._children`           | lista ID dzieci np. [`.1.2.1.1`, `.1.2.1.2`] |
| `self._name`               | nazwa rodzaju agenta (jedna ze zdefiniowanych przez programistę) |
| `self._isGoalAchieved`     | flaga sprawdzająca czy sel został osiągnięty  aktualizowana co krop agenta |
| `self._now`                | czas działania systemu według agenta (może się różnić z rzeczywistym gdy brak aktualizacji) aktualizacja tylko poprzez `getTime()` |

Zastrzeżone nazwy: `self._agent`, `self._isMother`, `self._next_child`, `self._inbox`, `self._runtime`, `self._return_flag`, `self._break_flag`, `self._fields`, `self._fields_type`, `self._beliefs`, `self._beliefs_type`, `self._sense`, `self._goals`, `self._rules`, `self._receive`, `self._actions`, `self._initialize`, `self._destroy`

TODO: Dać możliwość proframiście zamienić nazwę pola wbudowanego w razie takiej potrzeby. 


## Operacje

| Operacje | Opis | Kontekst |
|----------------|------|----------|
| `when`         | Warunek wyzwolenia | `rules`, `receive` |
| `then`         | Część wykonawcza reguły | `rules`, `receive` |
| `send(...)`    | Wysyłanie wiadomości | dowolnie |
| `do(...)`      | Wywoałanie akcji (zwraca wartość dla innych typów akcji niż `void`) | dowolnie |
| ???`adopt_goal(...)` | Przyjęcie nowego celu | `action`, `receive` |
| ???`drop_goal(...)`  | Porzucenie celu | `action`, `receive` |
| ???`adopt_belief`    | Pezyjęcie nowe przekonanie                         |
| ???`drop_belief`     | Porzucenie przekonanie                                |
| `get_time()`      | Aktualizacja `self.now`. Kiedy przypisania zwraca aktualny czas | `initialize`, `action` |
| `goal_check(<goal_name>)` | Sprawdzenie celu cząstkowego |
| `print(...)`   | Debugowanie | dowolnie |
| `kill()`       | Zakończenie działania agenta | dowolnie |
| `kill(child_id)` | Usunięcie dzieci | dowolnie |
| `kill_children()` | Kończy działanie wszystkich dzieci |
| `kill_children(childen_type_name)` | Kończy działanie wszystkich dzieci o podanym typie|
| `kill_siblings()` | Kończy działanie wszystkich braci |
| `kill_siblings(sibling_type_name)` | Kończy działanie wszystkich braci o podanym typie|
| `spawn(agent_name, [fields_of_agent])`   | Tworzenie dzieci | `initialize`, `action` |
| `sleep(ms)`    | Pauza w wykonaniu | `action`, `receive` |
| `sense()`      | Możaliwość wywołania z dowolnego miejsca w ciele agenta. Wykonuje polecenia z `sense{}` |
| `random(start, end)` | Zwraca losową wartość całkowitą z przedziału [start, end] |


### Kontrola przepływów

| Słowo kluczowe | Opis | Kontekst |
|----------------|------|----------|
| `return`       | Zwracanie wartości | `action` |
| `if`, `else`   | Warunkowe wykonanie | dowolnie |
| `for` | Pętla iteracyjna | dowolnie |
| `while()`      | Pętla warunkowa | dowolnie |
| `break`      | Przerywa pętlę | dowolnie |

Przykład:
```agentar
for (int i; i<10; i=i+1){
    print(i);
}
while (self.counter<5){
    self.counter = self.counter + 1;
}
if msg.text=="text"{
    print("tak");
} else { 
    print("nie");
}
if (msg.text=="text") print("tak"); // dla jednej instrukcji
```

### Typy danych

| Typ      | Opis                              |
|----------|-----------------------------------|
| `int`    | Liczba całkowita                  |
| `float`  | Liczba zmiennoprzecinkowa         |
| `bool`   | Wartość logiczna `true` / `false` |
| `string` | Tekst                             |
| `list`   | Lista wartości                    |
| TODO `dict`   | Słownik (klucz → wartość)         |
| `agentID`| np. `.1.1`         |
| `pointer<type>` | wspaźnik na obiekt. UWAGA! Posczas deklaracji nie da się przypisać |
| `&var_name` | przekazanie referencji do obiektu |


### Obsługa list i map

W AGENTAR listy i mapy (słowniki) są podstawowymi strukturami danych. Wersja języka prototypowego obsługuje je prostą składnią.

Deklaracja listy:
`list myList = [1, 2, 3];`

Odwołanie do elementu:
`first = myList[0];  // wartość: 1`

Dodanie na koniec:
`myList[] = 4;  // teraz myList = [1, 2, 3, 4]`

Aktualizacja elementu:
`myList[1] = 10;  // teraz myList = [1, 10, 3, 4]`

Wybrór kawałka listy:
`myList[2:-1]`

TODO: obsługa map

??? Deklaracja mapy:
```
??? dict user = {
    name = "Alice",
    age = 30
};
```

Dostęp do kluczy:
`keys_list = user.keys()`    (DictKeysExpr)

dostęp do wartości:
`values_list = user.values()`   (DictValuesExpr)

Dostęp do wartości o podanym kluczu (IndexExpr)
`user["name"];`    Zwraca wartość  
`username = user["name"];` 

Modyfikacja wartości:  (IndexAssign)
`user["age"] = 31;`

Dodanie nowej pary:  (IndexAssign)
`user["city"] = "Warsaw";`

Usunoęcie element  (dictDelStmt)
del user["city"];

Uwagi projektowe:
- Listy są indeksowane od 0.
- Dodanie elementu [] = x to syntactic sugar dla append(x).
- Nie można nadawać wartości początkowych w polu fields dla list i dict... 



# Komunikacja
- Każdy agent działa niesekwencyjnie i ma własną kolejkę wiadomości.
- Wiadomości są kolejkowane FIFO (first-in, first-out).
- W ciągu jednej pętli agenta agent przetwarza jedną wiadomość z kolejki

### Struktura wiadomości
Każda wiadomość w systemie może zostać zdefiniowana.
```
message <msg_name>  {
    // pola wiadomości
    // np. string task; 
}
```
---

| Funkcja                          | Opis                                  |
| -------------------------------- | ------------------------------------- |
| `send(to_id, content, msg_type='inform')` | Wysyła wiadomość do wskazanego agenta (ID). Wiadomość jest dodawana na koniec kolejki odbiorcy i zostanie przetworzona asynchronicznie w jego kolejnej pętli.|
| `send2parent(content, msg_type='inform')`            | Skrót do komunikacji z rodzicem       |
| `send2children(_/<agent_type>, content, msg_type='inform')`     | Wysyła wiadomość do wszystkich dzieci (`_`) lub tylko konkretnego typu|
| `send2siblings(_/<agent_type>, content, msg_type='inform')`          | Wysyła wiadomość do wszystkich braci (`_`) lub tylko konkretnego typu |

`msg` jako struktura zawierająca pola:
```
msg {
    _sender: ID        // nadawca wiadomości
    _receiver: ID      // adresat wiadomości
    _type: string      // systemowy typ wiadomości (inform, request ...)
    _sending_time: int         // czas wysłania wiadomości
    <Pola wiadomości>   // treść wiadomości – instancja klasy zdefiniowanej w message { ... }
}
```

Dostęp do pól odbywa się przez kropkę, np. `msg.task`

W ciele `receive`, agent ma dostęp do struktury `msg`, która zawiera metadane wiadomości oraz jej treść

Przykład:
```
receive ping {
    when (
        msg._type == request &&
        msg._sender == "mother" &&
        msg.text == "hello"
    ) then {
        print("Received hello from mother");
    }
}
```

### Rodzaje wiadomości

Rodzaj wiadomości umożliwiają programiście rozszerzyć warunki komunikacji.

| Rodzaj                           | Opis                                  |
| -------------------------------- | ------------------------------------- |
| `inform` (defoult)               | Prośba o informację                   |
| `ask`                            | Zapytanie (oczekuje odpowiedzi)       |
| `request `                       | Prośba o zrealizowanie czegoś (musi podjąć próbę lub odmówić)|
| `confirm`                        | Potiwerdzenie np. wykonania celu      |
| `deny `                          | Zaprzeczenie np. wykonania celu       |

---


## Struktura ID agenta

* Automatycznie nadawane przez interpreter
* Format: `.1`, `.1.1`, `.1.2.1`, itp.
* ID jest unikalne w czasie działania systemu
* Agenci **nie mogą recyklingować ID** po zabiciu dzieci


## Świat i środowisko
* Śwat w tej wersji języka jest symulowany poprzez pola w agencie marce (np. `self.WORLD in mother`)
* Inni agenci mogą przechwywać wskaźniki do tych pól i w sekcji `sense{}` czytać lub pisać do świata. Jest to widoczne dla każdego agenta
* Takie podejście daje możliwość działąnia agentów w jednym  środowisku 

---



# Przykłady

Przykłądy znajdują się w folderze `examples/`
