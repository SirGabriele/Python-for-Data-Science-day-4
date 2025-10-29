# Paths names
TEST_FILE = test.py

# Executable
PYTHON_VERSION = python3.10

# Rules
all: test

test:
	$(PYTHON_VERSION) $(TEST_FILE)

fclean:
	rm -rf __pycache__

re: fclean all

.PHONY: all test fclean re
