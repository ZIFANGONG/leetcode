class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        note_set = Counter(ransomNote)
        magazine_set = Counter(magazine)

    

        if note_set & magazine_set == note_set:
            return True
        else:
            return False


        