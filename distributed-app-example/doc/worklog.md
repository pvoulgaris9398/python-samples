---
name: worklog.md
description: working log for this project
date: 7/19/2026
---

## `Sunday, 7/19/2026`

```bash

curl -X POST http://localhost:5281/products/seed

curl http://localhost:5242/products/1

python -m grpc_tools.protoc -I/path/to/shared/protos --python_out=. --grpc_python_out=. /path/to/shared/protos/inventory.proto


```
