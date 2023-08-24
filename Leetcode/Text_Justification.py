class Solution:
    def get_words_in_line(
        self, words: list[str], starting_index: int, max_width: int
    ) -> tuple[list[str], bool]:
        """
        Returns a list of all the words in current line. (starting from starting_index in words)
        And a bool denoting if this line is the last line in our input.
        """
        index = starting_index
        width = 0
        line: list[str] = []
        while index < len(words):
            width += len(words[index])
            if width <= max_width:
                line.append(words[index])
            else:
                break
            width += 1
            index += 1
        return line, index == len(words)

    def get_length(self, words: list[str]) -> int:
        """
        Return length of "sentence", adding length of all words.
        """
        length = 0
        for word in words:
            length += len(word)
        return length

    def whitespace_array(self, line: list[str]) -> list[int]:
        """
        Returns an array where each element denotes the number of spaces to be
        added in every space between words in the given line.
        """
        required_spaces = self.max_width - self.get_length(line)
        whitespace_words = len(line) - 1
        spaces = []
        if whitespace_words > 0:
            lowest_denominator_space = required_spaces // whitespace_words
            spaces_taken = lowest_denominator_space * whitespace_words
            spaces = [lowest_denominator_space] * whitespace_words

            index = 0
            while spaces_taken < required_spaces:
                spaces[index] += 1
                index += 1
                spaces_taken += 1

        return spaces

    def fullJustify(self, words: list[str], max_width: int) -> list[str]:
        self.max_width = max_width
        out: list[str] = []
        idx = 0
        while idx < len(words):
            # Get words to go in current line.
            line, end_line = self.get_words_in_line(words, idx, max_width)
            idx += len(line)
            # Get spaces array, or create spaces array for last line / line with single word.
            spaces_reqd = max_width - self.get_length(line)
            if end_line:  # Add all remaining whitespaces @ the end of the last line.
                spaces = [1] * spaces_reqd
            else:
                spaces = self.whitespace_array(line)  # normal spaces array
            line_arr: list[str] = []  # Construct line
            i = 0
            while i < len(line):
                line_arr.append(line[i])  # Add word
                if i < len(spaces):  # Add space (if not last word)
                    line_arr.append(" " * spaces[i])
                i += 1
            if end_line or len(line_arr) == 1:  # If last line or line with single word
                total = self.get_length(line_arr)
                print(line_arr, total)
                if total != max_width:
                    line_arr.append(
                        " " * (max_width - total)
                    )  # Add all spaces at the end of the line
            out.append("".join(line_arr))

        return out


def print_list(lst: list[str]):
    for i in lst:
        print(i)


if __name__ == "__main__":
    sol = Solution()
    print_list(
        sol.fullJustify(
            words=["This", "is", "an", "example", "of", "text", "justification."], max_width=16
        )
    )
    print_list(
        sol.fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], max_width=16)
    )
    print_list(
        sol.fullJustify(
            words=[
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            max_width=20,
        )
    )
    print_list(
        sol.fullJustify(
            words=[
                "ask",
                "not",
                "what",
                "your",
                "country",
                "can",
                "do",
                "for",
                "you",
                "ask",
                "what",
                "you",
                "can",
                "do",
                "for",
                "your",
                "country",
            ],
            max_width=16,
        )
    )
