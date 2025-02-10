
def progress_bar(current: int, total: int, width: int = 50, fill: str = '█') -> None:
    """
    Print progress bar
    current: Current progress
    total: Total value for 100%
    width: Width of progress bar
    fill: Character to use for progress
    """
    percent = (current * 100) // total
    filled = (current * width) // total
    bar = fill * filled + '-' * (width - filled)
    print(f'\r|{bar}| {percent}%', end='', flush=True)
    if current == total:
        print("\n")
        print("Complete")
        print()