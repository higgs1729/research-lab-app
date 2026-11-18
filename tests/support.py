"""Isolated test folders inheriting workspace permissions, including on Windows."""
from pathlib import Path
import shutil
from uuid import uuid4


class ProjectDirectory:
    def __init__(self):
        self.base = (Path(__file__).resolve().parents[1] / "runtime" / "test-projects").resolve()
        self.path = self.base / uuid4().hex
        self.path.mkdir(parents=True)
        self.name = str(self.path)

    def cleanup(self):
        target = self.path.resolve()
        if target.parent != self.base or target.name != self.path.name:
            raise ValueError("Test cleanup path escaped its test folder")
        if target.exists():
            shutil.rmtree(target)

    def __enter__(self):
        return self.name

    def __exit__(self, *args):
        self.cleanup()
