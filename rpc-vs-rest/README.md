Ejemplos de cómo se puede implementar un servicio de control de puertas siguiendo diferentes aproximaciones:

- `ice_*`: RMI (con ZeroC Ice)
- `rest_*`: REST (con HTTP + JSON)
- `ri_*`: Remote Invocation con HTTP + JSON (no es REST)

|                        |                      | Ice                    | REST                          | Remote Invocation con HTTP + JSON |
|---|---|---|---|---|
| **Operaciones** |||||
| Abrir puerta x%:       | El cliente envía     | Llamada `open(20)`     | PUT `{"percentage_open": 20}` | PUT `{"operation": "open", "args": [20]}` |
|                        | El servidor retorna  | Nada                   | `201 No Content`              | `{"result": "ok"}` |
| ¿Cuánto está abierta?: | El cliente envía     | Llamada `getOpening()` | GET                           | PUT `{"operation": "getOpening", "args": []}` |
|                        | El servidor retorna  | `20`                   | `{"percentage_open": 20}`     | `{"result": 20}` |
| **Características** |||||
|                        | Transparencia acceso | Sí (parece local)      | No                            | No |
|                        | Quién define ops.    | La aplicación          | HTTP (uniformes)              | La aplicación (HTTP sin semántica) |

REST define un estilo arquitectónico, no operaciones ni una sintaxis específicas. Aunque en la práctica, casi siempre se implementa sobre HTTP:

  - Operaciones: GET, PUT, POST, PATCH, DELETE.
  - Identificadores: URL.
  - Representaciones: JSON, XML, etc.

ninguno de estos elementos es exclusivo de REST:

  - El conjunto de operaciones podría ser cualquier otro conjunto uniforme y bien definido.
  - Los identificadores podrían utilizar otro formato de URI.
  - El protocolo de aplicación podría ser otro distinto.

Ejemplo: CoAP (vs HTTP) ofrece GET, POST, PUT y DELETE sobre UDP, pudiendo mantener el mismo modelo.
