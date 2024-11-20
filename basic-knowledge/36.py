def demo(*args,**kw):
  if not args:
    pass
  else:
    for i in args:
      print(i)

if __name__ == "__main__":
  a = demo()
  print(next(a))
  print(next(a))

  # for j in a:
  #   print(j)

