import shutil
from pathlib import Path

import skbuild


def build(setup_kwargs):
    pass


def setup(**kwargs):
    skbuild.setup(**kwargs)

    src_dir = Path(skbuild.constants.CMAKE_INSTALL_DIR()) / "hello"
    dest_dir = Path("hello")

    print(f">>> {src_dir}")
    print(f">>> {dest_dir}")

    clear(dest_dir, "**/*.so")
    install(src_dir, dest_dir, "**/*.so")


def clear(target_dir, pattern):
    for path in target_dir.glob(pattern):
        print(f"!!! remove {path}")
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()


def install(src_dir, dest_dir, pattern):
    for src in src_dir.glob(pattern):
        dest = dest_dir / src.relative_to(src_dir)
        print(f"!!! src = {src}")
        print(f"!!! dest = {dest}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            shutil.copytree(src, dest)
        else:
            shutil.copy2(src, dest)
