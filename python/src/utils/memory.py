class MemoryUsageTracker:
    """
    Tracks memory usage of a pandas DataFrame over time.
    """
    def __init__(self, actual_memory_usage):
        self.previous = None
        self.latest = actual_memory_usage
        self.diff = 0

    def update(self, new_memory_usage):
        self.previous = self.latest
        self.latest = new_memory_usage
        self.diff = self.latest - self.previous