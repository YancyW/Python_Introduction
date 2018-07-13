# Q1: Speed

  1 check the code, find which part affects the speed
  ```
  import cProfile
  import pstats
  import my_slow_module
  cProfile.run('my_slow_module.run()','restats')
  p = pstats.Stats('restats')
  p.sort_stats('cumulative').print_stats(30)

  ```

  2 normally, the reason is for loop or the array in Numpy module

  3 use Cython to speed up.  (Cython is based on C/C++), in Cython code, the for loop only access Cython object, not Python object
