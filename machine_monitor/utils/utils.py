def format_bytes(size_in_bytes: int | None) -> str:
    """Convert a byte value to a readable string."""
    if size_in_bytes is None:
        return "Nao informado"

    units = ("B", "KB", "MB", "GB", "TB", "PB")
    size = float(size_in_bytes)

    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"

