# https://leetcode.com/problems/flood-fill/description/
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # The length of image and image[0] will be in the range [1, 50].
        # The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
        # The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
        NR, NC, startColor = len(image), len(image[0]), image[sr][sc]
        if startColor == newColor:
            return image

        def floodFillHelper(r, c):
            if image[r][c] == startColor:
                image[r][c] = newColor
                # try to fill up, down, left, right if possible
                if r+1 < NR: floodFillHelper(r+1, c)
                if r-1 >= 0: floodFillHelper(r-1, c)
                if c+1 < NC: floodFillHelper(r, c+1)
                if c-1 >= 0: floodFillHelper(r, c-1)

        floodFillHelper(sr, sc)
        return image
