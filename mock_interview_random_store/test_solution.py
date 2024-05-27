from solution import Store


def test_insert():
    store = Store()

    store.insert(1)
    store.insert(1_000)
    store.insert(1_000_000)

    print([store.get_random() for _ in range(100)])

    store.remove(1_000)

    print([store.get_random() for _ in range(100)])


if __name__ == "__main__":
    test_insert()
