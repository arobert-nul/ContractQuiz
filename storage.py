import csv


def save_result(filename, name, score, total):
    """Stores individual test score results"""
    try:
        with open(filename, "a", newline="") as file:
            csv.writer(file).writerow([name, score, total])
        return True
    except OSError:
        return False


def load_results(filename):
    """Returns all saved results"""
    try:
        with open(filename, newline="") as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        return []