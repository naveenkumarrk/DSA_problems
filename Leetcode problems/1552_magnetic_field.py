class Solution:
  def maxDistance(self, position: List[int], m: int) -> int:
    position.sort()

    l = 1
    r = position[-1] - position[0]

    def numBalls(force: int) -> int:
      balls = 0
      prevPosition = -force
      for pos in position:
        if pos - prevPosition >= force:
          balls += 1
          prevPosition = pos
      return balls

    while l < r:
      mid = r - (r - l) // 2
      if numBalls(mid) >= m:
        l = mid
      else:
        r = mid - 1

    return l
  




#   class Solution:

#     def maxDistance(self, position: List[int], m: int) -> int:

#         def check(minmax):
#             rem = m - 1
#             lim = position[0] + minmax
#             for p in position[1:]:
#                 if p >= lim:
#                     rem -= 1
#                     lim = p + minmax
#             return rem <= 0

#         position.sort()
#         if m == 2:
#             return position[-1] - position[0]
#         low = 1
#         high = (position[-1] - position[0]) // (m - 1)
#         while low < high:
#             mid = (low + high + 1) // 2
#             if check(mid):
#                 low = mid
#             else:
#                 high = mid -1
#         return low        