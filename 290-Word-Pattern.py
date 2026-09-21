class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # dono lists ka len different hai, then false
        words_ = s.split()
        if len(pattern) != len(words_):
            return False
        hashmap_ = {}
        hash_set = set()
        for i in range(len(words_)):
            letter = pattern[i]
            word = words_[i]

            if letter in hashmap_:
                if hashmap_[letter] != word:
                    return False
            else:
                if word in hash_set:
                    return False

                hashmap_[letter] = word
                hash_set.add(word)

        return True