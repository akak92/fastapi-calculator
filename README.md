# Calculator API (FastAPI)

## Endpoints
- POST `/calculator/suma`
- POST `/calculator/resta`
- POST `/calculator/producto`
- POST `/calculator/division`

### Body (JSON)
```json
{ "a": 10, "b": 5 }


### Response

{ "operation": "suma", "a": 10, "b": 5, "result": 15 }