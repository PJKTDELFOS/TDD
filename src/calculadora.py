def soma(x, y):
    ''' soma x e y

    >>> soma(2, 26)
    4
    '''
    assert isinstance(x, (int, float)),'Valor invalido de x'
    assert isinstance(y, (int, float)),'Valor invalido de y'
    return x + y
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)