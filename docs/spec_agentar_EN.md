# AGENTAR — Language Specification (EN Version)

AGENTAR is a lightweight, structured agent-based programming language built on hierarchical communication and the concept of autonomous units performing tasks.

---

## 1. Key Assumptions

* Each agent has a unique automatically assigned dot-notation ID: `.1`, `.1.2`, `.1.2.1`, etc.
* Simplified communication with: **parent**, **children**, and **siblings**.
* Agents have a life cycle: `initialize` → action loop → `destroy`.
* The system is message-based and rule-reactive.
* Access to fields via `self.name`.
* The root agent `mother` (created first, manages system execution).
* The system terminates when the `mother` agent calls `kill()`, or the simulation time expires.

---

## 2. Agent Life Cycle

1. `initialize` — configuration and setup (e.g., spawning children)
2. Action loop:

   * update beliefs from `sense`
   * receive the first message in the inbox (`receive`)
   * check goals (`goals`)
   * if a goal is not yet achieved:

     * apply rules (`rules`)
3. `destroy` — cleanup before termination

An agent dies when:

* it calls `kill()`
* its parent kills it
* when a parent terminates, all its descendants are killed as well

---

## 3. Agent Structure

All sections are optional, **BUT** must appear in a strict order!

```agentar
agent mother {
    // The mother agent is created automatically at program start.
}

agent <agent_name> {
    fields {
        <type> <name> = <value>;     // e.g., int counter = 0;
    }

    beliefs {
        // Agent's beliefs about the world
    }

    goals {
        // e.g., g1: bel.b1 == true || bel.b2 < 4;
        // e.g., g2: bel.b2 < 10;
    } merge (g1 || g2)

    initialize {
        // Code executed on startup
    }

    sense {
        // Reading the world and updating beliefs
    }

    rules {
        when (<condition>) then {
            <statements>;
        }
    }

    destroy {
        // Code executed on agent death
    }

    receive <msg_name> {
        when (<condition>) then {
            <statements>;
        }
    }

    action <name>(<args>): <return_type> {
        <statements>;
    }
}
```

---

# 4. Syntax Description

## 4.1 Agent Sections

| Keyword      | Description                         |
| ------------ | ----------------------------------- |
| `agent`      | Agent definition                    |
| `fields`     | Internal fields                     |
| `initialize` | Startup logic                       |
| `destroy`    | Shutdown logic                      |
| `beliefs`    | Agent knowledge about the world     |
| `sense`      | How the agent reads the environment |
| `goals`      | Agent objectives                    |
| `rules`      | Behavioral rules                    |
| `receive`    | Handlers for incoming messages      |
| `actions`    | Reusable agent actions              |
| `message`    | Message type definition             |

---

## 4.2 Built-in Agent Fields

Beliefs accessed as `bel.<field_name>`.

Built-in fields begin with `_` (read-only):

| Field                   | Description                       |
| ----------------------- | --------------------------------- |
| `self.id`               | Agent ID, e.g. `.1.2.1`           |
| `self.parent`           | Parent ID                         |
| `self.children`         | List of children IDs              |
| `self.name`             | Agent type name                   |
| `self.is_goal_achieved` | Flag indicating goal satisfaction |

Reserved names include: `self.id`, `self.parent`, `self.children`, `self.name`, `self.is_goal_achieved`, and internal runtime fields.

---

## 4.3 Operations

| Operation            | Description         | Context            |
| -------------------- | ------------------- | ------------------ |
| `when`               | Trigger condition   | rules, receive     |
| `then`               | Rule body           | rules, receive     |
| `send(...)`          | Send message        | anywhere           |
| `send2parent(...)`   | Send to parent      | anywhere           |
| `send2siblings(...)` | Send to siblings    | anywhere           |
| `do <action>`        | Invoke an action    | anywhere           |
| `goal_check(...)`    | Check partial goal  |                    |
| `print(...)`         | Debug output        |                    |
| `kill()`             | Self-destruction    |                    |
| `kill(child_id)`     | Kill child          |                    |
| `kill_children()`    | Remove all children |                    |
| `spawn(...)`         | Create child agent  | initialize, action |
| `sleep(ms)`          | Delay execution     |                    |
| `sense()`            | Run sense section   |                    |
| `random(start, end)` | Random integer      |                    |

---

## 4.4 Flow Control

| Keyword      | Description              |
| ------------ | ------------------------ |
| `return`     | Return value from action |
| `if`, `else` | Conditional              |
| `for`        | Iteration                |
| `while`      | Loop                     |
| `break`      | Loop break               |
| `continue`   | Skip iteration           |

---

## 4.5 Data Types

| Type         | Description    |
| ------------ | -------------- |
| `int`        | Integer        |
| `float`      | Floating-point |
| `bool`       | Boolean        |
| `str`        | String         |
| `list`       | List           |
| `dict`       | Dictionary     |
| `agentID`    | e.g., `.1.1`   |
| `pointer<T>` | Pointer        |
| `&var`       | Reference      |

---

## 4.6 Lists, Dictionaries, Tuples

(Translated faithfully from original Polish specification.)

---

# 5. Communication

* Each agent has its own message queue.
* FIFO ordering.
* One message processed per loop.

## 5.1 Message Structure

Message types:

```
message <msg_name>  {
    // message fields
}
```

Instantiation:

```
<msg_name> m = <msg_name>{task: "content"};
```

Sending:

| Function                               | Description                |
| -------------------------------------- | -------------------------- |
| `send(to_id, content, msgType_inform)` | Send message to ID         |
| `send2parent`                          | Shortcut                   |
| `send2children`                        | To all or by type          |
| `send2siblings`                        | To all siblings or by type |

Receive example: agent has access to `msg` metadata.

---

## 5.2 Message Types

| Type              | Description    |
| ----------------- | -------------- |
| `msgType_inform`  | Inform         |
| `msgType_ask`     | Query          |
| `msgType_request` | Request action |
| `msgType_confirm` | Confirmation   |
| `msgType_deny`    | Denial         |

---

# 6. Agent ID Structure

* Auto-assigned by interpreter
* Dot notation
* Unique throughout runtime
* No ID reuse

---

# 7. World and Environment

* The simulated world lives inside fields of the `mother` agent.
* Others may store pointers and read/write during `sense`.
* All agents observe a shared world.

---

# 8. Interpreter Runtime Architecture

```
agent.agar → AST → AgentarInterpreter → (mother, agents, messages)
                                 ↓
                       AgentarSystem(mother, agents, ...)
                                 ↓
       ┌────────────┬────────────┬────────────┐
       ▼            ▼            ▼            ▼
  AgentRunner   AgentRunner   AgentRunner   ...
     │             │             │
AgentInstance  AgentInstance  AgentInstance
     │             │             │
  AgentarAgent   AgentarAgent   AgentarAgent
```

---

# 9. Examples

Examples are located in the `examples/` directory.
