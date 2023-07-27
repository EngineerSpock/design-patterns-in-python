def is_singleton(factory):
    x = factory()
    y = factory()
    return x is y