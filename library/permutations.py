# source: https://en.wikipedia.org/wiki/Heap%27s_algorithm
# implementation to find permutations using Heap algorithm, recursive
def heapPermutations(size, a, tracker):
    if size == 1:
        tracker.add(''.join(a))
    else:
        # permutations with last item fixed
        heapPermutations(size-1, a, tracker)
        for i in range(size-1):
            if size&1 == 0:
                tmp = a[i]
                a[i] = a[size-1]
                a[size-1] = tmp
            else:
                tmp = a[0]
                a[0] = a[size-1]
                a[size-1] = tmp
            heapPermutations(size-1, a, tracker)

# call this to get all permutations
# pulled from my CodeWars
def permutations(s):
    ret = set()
    heapPermutations(len(s), list(s), ret)
    return ret

'''
Other solutions: https://www.codewars.com/kata/5254ca2719453dcc0b00027d/solutions/python
def permutations(string):
  if len(string) == 1: return set(string)
  first = string[0]
  rest = permutations(string[1:])
  result = set()
  for i in range(0, len(string)):
    for p in rest:
      result.add(p[0:i] + first + p[i:])
  return result

def permutations(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))
'''