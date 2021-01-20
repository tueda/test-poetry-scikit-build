"""Entry point."""

if __name__ == "__main__":
    from . import _hello as hello  # type: ignore[attr-defined]

    hello.hello("World")
