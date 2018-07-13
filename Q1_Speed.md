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

  4 If you want to deal with string, you can use spaCy module

  6 Some useful links
   [Cython ref](http://cython.readthedocs.io/en/latest/src/tutorial/index.html)
   [spaCy ref] (https://spacy.io/api/cython)
   [use Cython class instead of a pure C class] (http://cython.readthedocs.io/en/latest/src/userguide/extension_types.html)
