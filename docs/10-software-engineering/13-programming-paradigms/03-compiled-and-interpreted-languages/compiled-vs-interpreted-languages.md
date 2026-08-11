# Compiled vs. Interpreted Languages

## TL;DR

**Compiled languages** are translated into machine code before execution, while **interpreted languages** are executed by an interpreter at runtime.

|                 | Compiled              | Interpreted              |
| --------------- | --------------------- | ------------------------ |
| Translation     | Before execution      | During execution         |
| Execution       | Native machine code   | Through an interpreter   |
| Typical speed   | Usually faster        | Usually slower           |
| Error detection | Often at compile time | Often at runtime         |
| Examples        | C, C++, Rust, Go      | Python, Ruby, JavaScript |

## Compiled Languages

A compiler translates the source code into machine code or another executable form **before** the program runs.

```text
Source Code
     │
     ▼
  Compiler
     │
     ▼
Machine Code
     │
     ▼
  Execution
```

For example, a C program can be compiled into a native executable:

```text
program.c → compiler → program.exe
```

The resulting program can usually run without the compiler being present.

## Interpreted Languages

An interpreter executes source code at runtime rather than producing a native executable beforehand.

```text
Source Code
     │
     ▼
 Interpreter
     │
     ▼
 Execution
```

For example:

```text
program.py → Python interpreter → execution
```

The interpreter is therefore required to run the program.

## Important: The Distinction Is Not Absolute

Modern programming languages often combine both approaches.

For example, **Java** source code is compiled into **bytecode**, which is then executed by the Java Virtual Machine (JVM). The JVM can interpret the bytecode and also use **Just-In-Time (JIT) compilation** to compile frequently executed code into native machine code.

Python implementations can also use intermediate representations and compilation internally.

Therefore, **"compiled" and "interpreted" describe execution strategies rather than strict categories of programming languages**.

## JIT Compilation

**Just-In-Time (JIT) compilation** combines aspects of compilation and interpretation.

```text
Source Code
     │
     ▼
Intermediate Code
     │
     ▼
 Interpreter / JIT Compiler
     │
     ▼
Machine Code
```

JIT compilation allows code to be compiled **during program execution**, often improving performance while retaining some flexibility of interpreted environments.

## Summary

* **Compiled:** code is translated before execution.
* **Interpreted:** code is executed by a runtime interpreter.
* **JIT:** code is compiled during execution.
* Modern runtimes often use a **combination of these techniques**.
