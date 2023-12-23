def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        foo = False
        track = {}
        for i in nums:
            if i in track:
                foo = True
            else:
                track[i] = True
        return foo