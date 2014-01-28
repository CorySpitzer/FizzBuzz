print "\n".join(map(lambda y: y[1].lstrip('0123456789') + "buzz" if not y[0] % 5 else y[1] + '', [(x,y) for x, y in enumerate(map(lambda x: x[1] + "fizz" if not x[0] % 3 else x[1] + str(x[0]), [(x,y) for x, y in enumerate([''] * 101)]))])[1:])


