"""Exercism : House"""

NURSERY = (
    ("", "the house that Jack built."),
    ("that lay in", "the malt"),
    ("that ate", "the rat"),
    ("that killed", "the cat"),
    ("that worried", "the dog"),
    ("that tossed", "the cow with the crumpled horn"),
    ("that milked", "the maiden all forlorn"),
    ("that kissed", "the man all tattered and torn"),
    ("that married", "the priest all shaven and shorn"),
    ("that woke", "the rooster that crowed in the morn"),
    ("that kept", "the farmer sowing his corn"),
    ("that belonged to", "the horse and the hound and the horn")
)


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite the nursery rhyme verses from start_verse to end_verse inclusive."""

    final = []
    
    for verse_number in range(start_verse, end_verse + 1):
        
        parts = [f"This is {NURSERY[verse_number - 1][1]}"]
        
        for i in range(verse_number - 1, 0, -1):
            
            action = NURSERY[i][0]
            previous_subject = NURSERY[i - 1][1]
            parts.append(f"{action} {previous_subject}")

        final.append(" ".join(parts))
        
    return final