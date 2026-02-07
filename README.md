# Python Logging for Data Engineering Pipelines

This repository demonstrates progressive, production-ready Python logging patterns
used in data engineering pipelines, from basic logging to multi-handler setups
(console + file) for observability and debugging.

---
## Core Functions
- ```file_logging.py```	shows how critical errors are saved to log files for post-failure investigation.
- ```file_handlers.py```	Shows how production pipelines separate INFO logs (console) from ERROR logs (saved file storage)
- ```log_RotationFileHandler.py``` Shows log rotation to prevent log files from growing indefinitely in production pipelines.
