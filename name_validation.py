def validate_name(name):
    """Return True if name is valid"""
    trimmed_name = name.strip()
    if trimmed_name == "":
        return False
    return True