---
title: "Python API Architecture Example - Code Structure"
description: "Python API Architecture Example - Code Structure"
type: "diagram"
author: "Lead Architect"
version: "0.0.1"
date: "2026-07-13"
tags:
  - backend
  - microservices
  - aws
  - code
  - module
  - structure
---

## Feature

```text
portfolio/

    api/

    commands/

        create_portfolio/

        close_portfolio/

        rename_portfolio/

    queries/

        get_portfolio/

        search_portfolios/

    domain/

        entities.py

        value_objects.py

        repository.py

        services.py

        events.py

    contracts/

        commands/

        queries/

        responses/

        events/

        dto/

    persistence/

    integrations/

        pricing/

        compliance/

    tests/
```

## feature/API

```text
features/
└── portfolio/
    └── api/
        ├── create_portfolio/
        │   ├── endpoint.py
        │   ├── request.py
        │   ├── response.py
        │   └── mapper.py
        ├── get_portfolio/
        │   ├── endpoint.py
        │   ├── response.py
        │   └── mapper.py
        ├── search_portfolios/
        │   ├── endpoint.py
        │   ├── request.py
        │   ├── response.py
        │   └── mapper.py
        ├── router.py
        ├── dependencies.py
        └── errors.py
```

## Shared

```text
shared/

    kernel/

    messaging/

    serialization/

    security/

    observability/
```    

## Kernel or _Common_

```text
kernel/

    result.py

    error.py

    problem_details.py

    ids.py

    pagination.py

    money.py

    percentage.py

    currency.py

    date_range.py
```

## Platform

```text
platform/

    startup.py

    dependency_injection.py

    configuration.py

    middleware.py

    routing.py

    lifespan.py
```

## Infrastructure

```text
infrastructure/

    postgres/

    redis/

    kafka/

    kinesis/

    s3/

    dynamodb/

    openai/

    anthropic/

    email/

    filesystem/

    telemetry/

    authentication/
```