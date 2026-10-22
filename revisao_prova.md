# Python Comprehensive Exam Review Guide (Listas 03 – 17)

A technical synthesis of core Python concepts, data structures, OOP, file handling, HTTP APIs, FastAPI, and Streamlit covered across all coursework lists.

---

## 1. Data Structures & Built-in Types

### Strings
* **Slicing**: `s[start:stop:step]`
  * Inversion: `s[::-1]` (e.g., [`lista3.py`](lista3.py#L42))
* **Methods**:
  * `.replace(old, new)`: Returns a copy with replacements ([`lista3.py`](lista3.py#L30)).
  * `.split(delimiter)`: Splits a string into a list of strings ([`lista4.py`](lista4.py#L12)).
  * `.count(sub)`: Frequency of a substring ([`lista3.py`](lista3.py#L47)).
  * `.strip()`: Removes leading/trailing whitespace and newlines.
  * `.upper()` / `.lower()` / `.islower()` ([`lista5.py`](lista5.py#L3)).

### Lists & Tuples
* **Lists** (mutable): `.append(item)`, `.pop()`, `.remove(item)`, `.clear()`.
* **Tuples** (immutable): Fixed elements `(x, y)` accessed by zero-based index ([`lista5.py`](lista5.py#L30)).
* **Step Ranges**: `range(start, stop, step)` with negative steps for countdowns ([`lista4.py`](lista4.py#L71)).

### Dictionaries
* **Key-Value mapping**: Efficient $O(1)$ average lookups.
* **Safe retrieval with fallback**: `d.get(key, default)` avoids `KeyError`.
  ```python
  # Counting word frequency (Lista 10)
  freq[word] = freq.get(word, 0) + 1
  ```
* **Iteration**:
  * `for k, v in d.items():` (keys and values)
  * `for k in d.keys():` / `for v in d.values():`
* **Dictionary Comprehension**:
  ```python
  medias = {nome: round(sum(notas) / len(notas), 2) for nome, notas in alunos.items()}
  ```

### Sets (`set`)
* **Uniqueness & Fast Membership**: Eliminates duplicates automatically.
* **Set Operations**:
  * Intersection (`&`): Common elements between two sets ([`lista09.py`](lista09.py#L16)).
  * Union (`|`), Difference (`-`).
  * `random.sample(range(1, 61), 6)`: Generates $k$ unique elements without replacement ([`lista09.py`](lista09.py#L4)).

---

## 2. File I/O & Serialization

### Context Manager (`with open`)
Guarantees file descriptors are safely closed even if exceptions occur.

| Mode | Behavior |
| :--- | :--- |
| `"r"` | Read only (raises `FileNotFoundError` if missing). |
| `"w"` | Write only (truncates existing file or creates new). |
| `"a"` | Append only (writes to the end without truncating). |

### CSV Handling
* **`csv.DictReader(f)`**: Parses CSV rows into Python dictionaries keyed by header names ([`lista08.py`](lista08.py#L22)).

### JSON Serialization
* **Memory (`str`) vs. Stream (`file`)**:
  * `json.loads(str_data)`: Deserializes JSON string $\rightarrow$ Python object.
  * `json.dumps(obj)`: Serializes Python object $\rightarrow$ JSON string.
  * `json.load(file_obj)`: Deserializes directly from an open file stream.
  * `json.dump(obj, file_obj)`: Serializes directly into an open file stream.

> **Crucial Pitfall**: Passing a file stream `f` to `json.loads(f)` raises `TypeError: the JSON object must be str, bytes or bytearray, not TextIOWrapper`. Always use `json.load(f)`.

---

## 3. Object-Oriented Programming (OOP)

* **Class Definition & Constructor (`__init__`)**:
  ```python
  class Pessoa:
      def __init__(self, nome: str, idade: int):
          self.nome = nome      # Instance attribute
          self.idade = idade
          self.ativo = True
  ```
* **Inheritance & `super()`**:
  ```python
  class Eletrico(Carro):
      def __init__(self, marca: str, modelo: str, autonomia: int):
          super().__init__(marca, modelo)  # Reuses base constructor
          self.autonomia = autonomia
  ```
* **Polymorphism & Method Overriding**: A subclass can re-implement methods defined in a parent class ([`lista12.py`](lista12.py#L28)).
* **Pitfall**: Forgetting `self.attribute = ...` inside `__init__` leaves the attribute missing and raises `AttributeError` at runtime.

---

## 4. REST APIs & HTTP Client (`requests`)

* **Methods**: `requests.get(url, params=...)`, `requests.post(url, json=..., params=...)`, `requests.put(...)`, `requests.delete(...)`.
* **Parsing Response**:
  ```python
  resp = requests.get(url)
  resp.raise_for_status()  # Raises HTTPError on 4xx/5xx status
  dados = resp.json()      # Parses response body as JSON dict/list
  ```
* **Status Codes**:
  * `200 OK`: Successful retrieval.
  * `201 Created`: Resource successfully created.
  * `404 Not Found`: Resource does not exist.
  * `500 Internal Server Error`: Unhandled server exception.

---

## 5. Backend Framework: FastAPI

* **Application Setup**:
  ```python
  from fastapi import FastAPI, HTTPException, status

  app = FastAPI(title="Minha API")
  ```
* **Routing Decorators**:
  * Path Parameter: `@app.get("/tarefas/{id}")`
  * Status Code specification: `@app.post("/tarefas", status_code=status.HTTP_201_CREATED)`
* **Handling Errors**:
  ```python
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item não encontrado")
  ```
* **ASGI Server**: Run using `uvicorn.run(app, host="127.0.0.1", port=8000)`.

---

## 6. Frontend Framework: Streamlit

### Execution Model
Streamlit executes the **entire Python script top-to-bottom on every user interaction** (button click, slider move, input change).

### Session State (`st.session_state`)
Because variables in global scope are recreated on every rerun, persistent state must be stored in `st.session_state`:
```python
if "contador" not in st.session_state:
    st.session_state.contador = 0

if st.button("Incrementar"):
    st.session_state.contador += 1
```

### Layouts & UI Components
* **Configuration**: `st.set_page_config(layout="centered")`
* **Columns**: `col1, col2 = st.columns([1, 1])`
* **Sidebar**: `with st.sidebar:`
* **Inputs**: `st.text_input`, `st.number_input`, `st.selectbox`
* **Feedback Alerts**: `st.success(...)`, `st.warning(...)`, `st.error(...)`, `st.info(...)`
* **Forced Rerun**: `st.rerun()` (triggers an immediate top-to-bottom re-execution)
* **Downloads**: `st.download_button(label=..., data=..., file_name=..., mime="application/json")`

---

## 7. Architecture & System Pitfalls Checklist

1. **Port Collisions**:
   * Streamlit default port: `8501`.
   * FastAPI / Uvicorn default port: `8000`.
   * Never bind both servers to the same port on the same host interface.
2. **Blocking Calls in Streamlit**:
   * Never call `uvicorn.run()` synchronously inside the main Streamlit script; it halts execution and blocks page rendering. Run backend and frontend as separate processes.
3. **EAFP Pattern (Error Handling)**:
   * *Easier to Ask for Forgiveness than Permission*: Prefer `try / except FileNotFoundError` over checking file existence before opening.
4. **Main Entrypoint Guard**:
   * Always guard executable code with `if __name__ == "__main__":` to prevent accidental execution when files are imported.

