# Convenience targets — see README for the per-exercise workflow.

.PHONY: check-solutions check-all fmt lint typecheck

# Verify all reference solutions pass their tests (maintenance).
check-solutions:
	pytest solutions/

# Run everything — only clean once ALL exercises are solved.
check-all:
	pytest exercises/

# List files that are not ruff-formatted (maintenance; solutions/ should always be clean).
fmt:
	ruff format --check solutions/

lint:
	ruff check solutions/

typecheck:
	mypy --strict solutions/
