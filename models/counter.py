class Counter:
    def __init__(self):
        self._count = 0
        self._is_open = False

    def add(self):
        if not self._is_open:
            raise RuntimeError("Counter should be used in a 'with' block")
        self._count += 1

    def get_count(self):
        if self._is_open:
            raise RuntimeError("Counter should be used in a 'with' block")
        return self._count

    def __enter__(self):
        self._is_open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._is_open = False
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        return False
