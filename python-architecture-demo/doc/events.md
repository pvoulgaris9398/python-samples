---
title: "Python API Architecture Example - Events"
description: "Python API Architecture Example - Events"
type: "diagram"
author: "Lead Architect"
version: "0.0.1"
date: "2026-07-13"
tags:
  - backend
  - microservices
  - aws
  - events
  - messaging
  - Kafka
  - Rabbit MQ
  - kinesis
  - publisher
  - subscriber
---

```text
infrastructure/
    messaging/
        publisher.py
        subscriber.py
        in_memory.py
        kafka.py
        kinesis.py
```