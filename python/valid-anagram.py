def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    track = {}
    sl = len(s)
    tl = len(t)
    if(sl != tl):
        return False
    for i in range(sl):
        if s[i] in track:
            track[s[i]] += 1
        else:
            track[s[i]] = 1
        if t[i] in track:
            track[t[i]] += 1
        else:
            track[t[i]] = 1
    for key in track:
        if track[key] != 2:
            return False
    return True
