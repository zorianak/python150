import sys


def pytest_collect_file(parent, file_path):
    """Add each problem's directory to sys.path so 'from solution import ...' works.
    Also invalidate any cached 'solution' module so each problem gets its own."""
    if file_path.name == "test_solution.py":
        problem_dir = str(file_path.parent)
        # Remove stale cached modules from previous problems
        for mod_name in list(sys.modules):
            if mod_name in ("solution", "test_solution"):
                del sys.modules[mod_name]
        # Ensure this problem's directory is first on sys.path
        sys.path = [p for p in sys.path if p != problem_dir]
        sys.path.insert(0, problem_dir)
