=============
Tombola tests
=============

Every concrete subcls of Tombola should pass there tests.

Create and load instance from iterable:

  >>> balls = list(range(3))
  >>> globe = ConcreteTombola(balls)
  >>> globe.loaded()
  True
  >>> globe.inspect()
  (0, 1, 2)

Pick and collect balls::
  
  >>> pick = []
  >>> pick.append(globe.pick())
  >>> pick.append(globe.pick())
  >>> pick.append(globe.pick())

Check state and results::

  >>> globe.loaded()
  False
  >>> sorted(picks) == balls
  True
