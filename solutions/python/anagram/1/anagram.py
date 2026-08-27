"""Exercism : Anagram"""


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Determine if the 'candidates' are anagram's of the 'word'"""

    clean_word = sorted(word.lower())

    return [candidate
            for candidate in candidates
            if candidate.lower() != word.lower()
            and clean_word == sorted(candidate.lower())
    ]

    
        