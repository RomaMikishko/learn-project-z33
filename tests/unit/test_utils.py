from utils import build_path


def test_build_path():
    original = [
        "/",
        "hello",
        "hello/",
    ]
    expected = [
        "/",
        "hello/",
        "hello/",
    ]

    for i in range(3):
        t = original[i]
        e = expected[i]
        got = build_path(t)
        assert got == e, f"path '{t}' normalized to '{got}', while '{e}' expected"

    if isinstance(message, str):
        message = to_bytes(message)