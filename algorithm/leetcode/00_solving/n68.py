class Solution(object):
    def __init__(self):
        self.current_words = []
        self.current_line = ''
        self.lines = []

    def appendLine(self, maxWidth: int, lastLine: bool):
        """
        :type maxWidth: int
        :rtype: None
        """
        
        if len(self.current_words) == 1 or lastLine:
            return self.current_line

        space = [0 for _ in range(len(self.current_words))]
        left_space = maxWidth - self.width
        between_space = len(self.current_line)-1 if len(self.current_line) > 1 else 0
        rest = left_space % between_space
        if rest == 0:
            space[0] = space[1] = (left_space // between_space) + 1
        justified_line = (' '*space).join(self.current_line).ljust(maxWidth)
        self.lines.append(justified_line)

    def fullJustify(self, words: list, maxWidth: int):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        for word in words:
            if len(self.current_line) + len(word) > maxWidth:
                self.appendLine(maxWidth, False)
                self.width, self.current_line = len(word), [word]
            else:
                self.current_words.append(word)
                self.current_line += ' ' + word
        self.appendLine(maxWidth, True)
        
        return self.lines


input_words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
input_words = ["This", "is", "an", "example", "of", "text", "justification."]
input_width = 16
solution = Solution()
print(solution.fullJustify(input_words, input_width))



