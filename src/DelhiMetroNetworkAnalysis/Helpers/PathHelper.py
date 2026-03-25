import sys
from pathlib import Path


def resource_path(relative_path: Path) -> Path:
    return __get_root() / relative_path


def __get_root() -> Path:
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)

    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "src").exists():
            return parent
    raise RuntimeError("No src folder present in project !")
