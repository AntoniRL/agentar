# AGENTAR

AGENTAR to lekki, strukturalny język programowania agentowego, oparty na hierarchicznej komunikacji i koncepcji autonomicznych jednostek wykonujących zadania.

## Kluczowe założenia

* Każdy agent ma unikalne, automatycznie nadawane `id` w formacie kropkowym: `.1`, `.1.2`, `.1.2.1`, itd.
* Ułątwiona komunikacja do: **rodzica**, **dzieci** i **braci**.
* Agenci mają cykl życia: `initialize` → pętla działania → `destroy`
* System oparty na komunikatach (wiadomościach) i reaktywnych regułach.
* Dostęp do pól agenta poprzez `self.name`
* Agent matka `mother` (Tworzony jako pierwszy, zarządza działaniem systemu)
* Agent czas `time` (Zarządza czasem- towrzony podczas inicjalizacji systemu, kiedy agent poprosi udostępnia aktualny czas `get_time()`)
* Koniec działania systemu kiedy brak agentów (mother: `kill()`)

---

## Cykl życia agenta

1. `initialize` — konfiguracja i inicjalizacja (np. tworzenie dzieci)
2. Pętla działania:
   - odbiór wiadomości
   - aktualizacja przekonań (`beliefs`)
   - postępowanie zgodnie z regułami (`rules`) 
        - dążenie do osiągnięcia celu `goals`
        - wykonanie akcji (`action`)
3. `destroy` — sprzątanie przed śmiercią

Agent umiera, gdy:
- wywoła `kill()`
- jego rodzic go zlikwiduje

## Struktura agenta

```agentar
agent mother {
    // Agent matka uruchamiany podczas wywołania programu. On uruchamia pozostałych agentów. Struktura jak zwykłego agenta (zarezerwowana nazwa mother)
}

agent <agent_name> {
    fields {
        // Pola wbudowane patrz niżej.
        <type> <name> = <value>;     // np. int counter = 0;
    }

    initialize {
        // Kod uruchamiany przy starcie agenta
        // np. print("Hello!");
    }

    destroy {
        // Kod uruchamiany przy śmierci agenta
        // np. print("Bye!");
    }

    beliefs {
        // Przekonania agenta (opcjonalne)
        // np. b1 = true;
        // np. b2 = 33;
    }

    goals {
        // Cele agenta (opcjonalne)
        // np. g1 = true;
        // np. g2 = "Done";
    }

    rules {
        // Zasady postępowania agenta (opcjonalne)
        when <condition> then {
            <statements>;
        }
    }

    receive <msg_name> {
        // Instrukcje po otrzumaniu wiadomości
        when <pattern> then {
            <statements>;
        }
    }

    action <name>(<args>): <return_type> {
        // Dfinicja akcji, które może podjąc agent (możliwość wywołania z poziomu bytu agenta)
        <statements>;
    }
}
```

# Opis składni

### Słowa kluczowe

| Słowo kluczowe          | Opis                                         |
| ----------------------- | -------------------------------------------- |
| `agent`                 | Definicja agenta |
| `fields`                | Pola - głównie wbudowane ale również można zdefiniować swoje    |
| `initialize`            | Inicjalizacja - część wykonywana podczas inicjalizacji agenta |
| `destroy`               | Zniszczenie - część wykonywana po śmierci agenta |
| `beliefs`               | Przekonania - co agent uważa, że wie o świecie. Pochodzą z wiadomości lub sensorów. Typ danych `map` |
| `goals`                 | Cele - Co agent chce osiągnąć. Kierują działaniem agenta.   |
| `rules`                 | Zasady - Kiedy coś się stanie wykonaj akcję. |
| `receive`               | Otrzymywać - Kroki podjętet po otrzymaniu konkretnej wiadomości |
| `actions`               | Akcja - reprezentuje konkretne dostępne zadania |
| `message`               | Definicja typu wiadomości  |

### Wbudowane pola agenta

| Pole                      | Opis                                         |
| ------------------------- | -------------------------------------------- |
| `self.id`                 | ID agenta np. `.1.2.1`                       |
| `self.parent`             | ID rodzica np. `.1.2`                        |
| `self.children`           | lista ID dzieci np. [`.1.2.1.1`, `.1.2.1.2`] |
| `self.next_child`         | ID następnego dziecka (inkremetowanie automatycznie po `spawn()`) |
| `self.name`               | imie agenta - jak nie zdefiniowane to: `imie-rodzica_1` `imie-rodzica_2` itd. |
| `self.now`                | czas działania systemu według agenta (może się różnić z rzeczywistym gdy brak aktualizacji) |

### Operacje

| Operacje | Opis | Kontekst |
|----------------|------|----------|
| `when`         | Warunek wyzwolenia | `rules`, `receive` |
| `then`         | Część wykonawcza reguły | `rules`, `receive` |
| `send(...)`    | Wysyłanie wiadomości | dowolnie |
| `belief(...)`  | Sprawdzenie przekonania | w `when` |
| `goal(...)`    | Sprawdzenie celu | w `when` |
| `adopt_goal(...)` | Przyjęcie nowego celu | `action`, `receive` |
| `drop_goal(...)`  | Porzucenie celu | `action`, `receive` |
| `adopt_belief`    | Pezyjęcie nowe przekonanie                         |
| `drop_belief`     | Porzucenie przekonanie                                |
| `get_time()`   | Aktualizacja `self.now` | `initialize`, `action` |
| `print(...)`   | Debugowanie | dowolnie |
| `kill()`       | Zakończenie działania agenta | dowolnie |
| `kill_child(child_id)` | Usunięcie dzieci | dowolnie |
| `spawn(agent_name, personal_name, fields_of_agent)`   | Tworzenie dzieci | `initialize`, `action` |
| `sleep(ms)`    | Pauza w wykonaniu | `action`, `receive` |

### Kontrola przepływów

| Słowo kluczowe | Opis | Kontekst |
|----------------|------|----------|
| `let`          | Zmienna lokalna | `action`, `receive` |
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
`list myList = {1, 2, 3};`

Odwołanie do elementu:
`let first = myList[0];  // wartość: 1`

Dodanie na koniec:
`myList[] = 4;  // teraz myList = {1, 2, 3, 4}`

Aktualizacja elementu:
`myList[1] = 10;  // teraz myList = {1, 10, 3, 4}`

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
| `send(to_id or name, content, msg_type='inform')` | Wysyła wiadomość do wskazanego agenta (po nazwie lub ID). Wiadomość jest dodawana na koniec kolejki odbiorcy i zostanie przetworzona asynchronicznie w jego kolejnej pętli.|
| `send_to_children(content, msg_type='inform')`     | Wysyła wiadomość do wszystkich dzieci |
| `send_to_parent(content, msg_type='inform')`            | Skrót do komunikacji z rodzicem       |
| `send_to_siblings(content, msg_type='inform')`          | Wysyła wiadomość do wszystkich braci  |

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
Dostęp do pól odbywa się przez kropkę, np. `msg.content.task`

W ciele `receive`, agent ma dostęp do struktury `msg`, która zawiera metadane wiadomości oraz jej treść (`content`)

Przykład:
```
receive ping {
    when (
        msg.type == "request" &&
        msg.sender == "mother" &&
        msg.content.text == "hello"
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

```agentar
message ping {
    string content;
}

message pong {
    string response;
}

agent responder {
    receive ping {
        when (msg.type == "request") then {
            print("Received ping: " + msg.content.content);
            send_to_parent(pong{response = "pong!"});       // msg_type="inform" niepotrzebne (domyślna wartość)
        }
    }
}

agent mother {
    initialize {
        print("Starting ping-pong demo");
        spawn(responder, "child");
        let mes_ping = ping{content = "ping!"};
        send("child", mes+ping, msg_type="request");
    }

    receive pong {
        print("Got pong: " + msg.content.response);
        kill(); // Kończy system
    }
}
```

### beliefs, rules, goals

```agentar
message clean_room {
    string task;
}

message task_done {
    string status;
}

agent cleaner {
    beliefs {
        dirty = true;
    }

    goals {
        clean_room = true;
    }

    rules {
        when (
            belief("dirty") && 
            goal("clean_room")
        ) then {
            clean();
        }
    }

    action clean(): void {
        print("Cleaning room...");
        beliefs("dirty") = false;
        drop_goal("clean_room");
        let done = task_done{status = "done"};
        send_to_parent(done, msg_type="confirm");
    }

    receive clean_room {
        when (
            msg.type == "request" &&
            msg.content.task == "clean"
        ) then {
            beliefs("dirty") = true;
            adopt_goal("clean_room");
        }
    }
}

agent mother {
    initialize {
        spawn(cleaner, "room_bot");
        let msg = clean_room{task = "clean"};
        send("room_bot", msg, msg_type="request");
    }

    receive task_done {
        when (
            msg.type == "confirm" &&
            msg.content.status == "done"
        ) then {
            print("Cleaner completed task.");
            kill();
        }
    }
}
```


### Rozwój 
`sense()` możliwość czytania ze świata (world)
