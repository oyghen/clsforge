import clsforge


def main() -> None:
    result = clsforge.__name__
    expected = "clsforge"
    if result == expected:
        print(f"Smoke test for {clsforge.__name__}: PASSED")
    else:
        raise RuntimeError(f"Smoke test for {clsforge.__name__}: FAILED")


if __name__ == "__main__":
    main()
