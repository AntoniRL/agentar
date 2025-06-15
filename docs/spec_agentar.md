# AGENTAR

AGENTAR to lekki, strukturalny język programowania agentowego, oparty na hierarchicznej komunikacji i koncepcji autonomicznych jednostek wykonujących zadania.

## Kluczowe założenia

* Każdy agent ma unikalne, automatycznie nadawane `id` w formacie kropkowym: `.1`, `.1.2`, `.1.2.1`, itd.
* Ułątwiona komunikacja do: **rodzica**, **dzieci** i **braci**.
* Agenci mają cykl życia: `initialize` → pętla działania → `destroy`
* System oparty na komunikatach (wiadomościach) i reaktywnych regułach.
* Dostęp do pól agenta poprzez `self.name`
* Agent matka `mother` (Tworzony jako pierwszy, zarządza działaniem systemu)
* (TODO?) Agent czas `time` `id=.0` (Zarządza czasem- towrzony podczas inicjalizacji systemu, kiedy agent poprosi udostępnia aktualny czas `get_time()`)
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
    }

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

| Pole                      | Opis                                         |
| ------------------------- | -------------------------------------------- |
| `self.id`                 | ID agenta np. `.1.2.1`                       |
| `self.parent`             | ID rodzica np. `.1.2`                        |
| `self.children`           | lista ID dzieci np. [`.1.2.1.1`, `.1.2.1.2`] |
| `self.name`               | nazwa rodzaju agenta (jedna ze zdefiniowanych przez programistę) |
| `self.isGoalAchieved`     | flaga sprawdzająca czy sel został osiągnięty  aktualizowana co krop agenta |
| (TODO?) `self.now`        | czas działania systemu według agenta (może się różnić z rzeczywistym gdy brak aktualizacji) |

Zastrzeżone nazwy: `self.agent`, `self.isMother`, `self.next_child`, `self.inbox`, `self.runtime`, `self.return_flag`, `self.break_flag`, `self.fields`, `self.fields_type`, `self.beliefs`, `self.beliefs_type`, `self.sense`, `self.goals`, `self.rules`, `self.receive`, `self.actions`, `self.initialize`, `self.destroy`


## Operacje

| Operacje | Opis | Kontekst |
|----------------|------|----------|
| `when`         | Warunek wyzwolenia | `rules`, `receive` |
| `then`         | Część wykonawcza reguły | `rules`, `receive` |
| `send(...)`    | Wysyłanie wiadomości | dowolnie |
| ???`adopt_goal(...)` | Przyjęcie nowego celu | `action`, `receive` |
| ???`drop_goal(...)`  | Porzucenie celu | `action`, `receive` |
| ???`adopt_belief`    | Pezyjęcie nowe przekonanie                         |
| ???`drop_belief`     | Porzucenie przekonanie                                |
| ???`get_time()`      | Aktualizacja `self.now` | `initialize`, `action` |
| `goal_check(<goal_name>)` | Sprawdzenie celu cząstkowego |
| `print(...)`   | Debugowanie | dowolnie |
| `kill()`       | Zakończenie działania agenta | dowolnie |
| `kill(child_id)` | Usunięcie dzieci | dowolnie |
| `kill_children()` | Kończy działanie wszystkich dzieci |
| `kill_children(childen_type_name)` | Kończy działanie wszystkich dzieci o podanym typie|
| `spawn(agent_name, [fields_of_agent])`   | Tworzenie dzieci | `initialize`, `action` |
| `sleep(ms)`    | Pauza w wykonaniu | `action`, `receive` |
| `sense()`      | Możaliwość wywołania z dowolnego miejsca w ciele agenta. Wykonuje polecenia z `sense{}` |

### Kontrola przepływów

| Słowo kluczowe | Opis | Kontekst |
|----------------|------|----------|
| `return`       | Zwracanie wartości | `action` |
| `if`, `else`   | Warunkowe wykonanie | dowolnie |
| `for ... in ...` | Pętla iteracyjna | dowolnie |
| `range()`      | range(6) = (0, 1, 2, 3, 4, 5)| dowolnie|
| `while()`      | Pętla warunkowa | dowolnie |

### Typy danych

| Typ      | Opis                              |
|----------|-----------------------------------|
| `int`    | Liczba całkowita                  |
| `float`  | Liczba zmiennoprzecinkowa         |
| `bool`   | Wartość logiczna `true` / `false` |
| `string` | Tekst                             |
| `list`   | Lista wartości                    |
| `dict`   | Słownik (klucz → wartość)         |
| `agentID`| np. `.1.1`         |


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

Deklaracja mapy:
```
dict user = {
    name = "Alice",
    age = 30
};
```

Dostęp do klucza:
`let username = user["name"];`

Modyfikacja wartości:
`user["age"] = 31;`

Dodanie nowej pary:
`user["city"] = "Warsaw";`

Uwagi projektowe:
- Listy są indeksowane od 0.
- Dodanie elementu [] = x to syntactic sugar dla append(x).
- Mapy mają klucze tekstowe. Można je dynamicznie dodawać lub modyfikować.

---

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
| `send2children(content, msg_type='inform')`     | Wysyła wiadomość do wszystkich dzieci |
| `send2parent(content, msg_type='inform')`            | Skrót do komunikacji z rodzicem       |
| `send2siblings(content, msg_type='inform')`          | Wysyła wiadomość do wszystkich braci  |

`msg` jako struktura zawierająca pola:
```
msg {
    sender: ID        // nadawca wiadomości
    receiver: ID      // adresat wiadomości
    type: string      // systemowy typ wiadomości (inform, request ...)
    time: int         // czas wysłania wiadomości
    content: object   // treść wiadomości – instancja klasy zdefiniowanej w message { ... }
}
```

`msg.content` to instancja klasy wiadomości, wygenerowanej na podstawie definicji `message <msg_name> {...}`.
Dostęp do pól odbywa się przez kropkę, np. `msg.task`

W ciele `receive`, agent ma dostęp do struktury `msg`, która zawiera metadane wiadomości oraz jej treść (`content`)

Przykład:
```
receive ping {
    when (
        msg.type == "request" &&
        msg.sender == "mother" &&
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

---



# Przykład

### Ping-pong

TODO: 
