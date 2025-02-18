class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if not s or not words:
            return []

        word_freq = {}
        # set the word freq of words in words list
        for w in words:
            word_freq[w] = 1 + word_freq.get(w, 0)


        word_length = len(words[0])
        window_length = word_length * len(words)

        res = []

        for i in range(len(s) - window_length + 1):
            j = i
            substring_freq = {}
            while j < i + window_length:

                current_word = s[j:j + word_length]

                if current_word not in word_freq:
                    break

                # store the freq of the current word in the current window
                substring_freq[current_word] = 1 + substring_freq.get(current_word, 0)
                
                # check the freq of current word in current window with the freq of the same word in the given word list
                if substring_freq[current_word] > word_freq[current_word]:
                    break

                j += word_length


            if j == i + window_length:
                res.append(i)

        return res 