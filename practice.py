#!/usr/bin/env python3

"""
Script to facilitate Molly Gebrian's technique of interleaved practice.
"""

import random
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Generator


@dataclass
class Phrase:
    page: int
    from_measure: int
    to_measure: int

    def __str__(self) -> str:
        return f"Page {self.page:3}, measures {self.from_measure:3} – {self.to_measure:3}"

    @property
    def measure_count(self) -> int:
        return self.to_measure - self.from_measure + 1


@dataclass
class InterleavedPractice:
    title: str
    phrases: list[Phrase]

    @property
    def total_measures(self) -> int:
        return sum(phrase.measure_count for phrase in self.phrases)


@dataclass
class SessionStats:
    start_time: datetime
    phrases_practiced: int = 0

    def add_phrase(self) -> None:
        self.phrases_practiced += 1

    def __str__(self) -> str:
        session_duration = datetime.now() - self.start_time
        return (f"Session stats: {self.phrases_practiced} phrases practiced, "
                f"session time {session_duration}")


BACH_GAMBA_SONATA_G = InterleavedPractice(
    title="Gamba sonata in G major",
    phrases=[
        Phrase(1, 1, 6),
        Phrase(1, 6, 13),
        Phrase(2, 13, 21),
        Phrase(3, 21, 28),
        Phrase(4, 1, 9),
        Phrase(4, 9, 20),
        Phrase(5, 21, 33),
        Phrase(5, 33, 43),
        Phrase(6, 43, 48),
        Phrase(6, 50, 61),
        Phrase(7, 61, 78),
        Phrase(8, 78, 93),
        Phrase(9, 94, 108),
        Phrase(9, 108, 113),
    ]
)

FAURÉ_TRIO_OP120 = InterleavedPractice(
    title="Fauré piano trio in d minor",
    phrases=[
        Phrase(1, 1, 23),
        Phrase(1, 21, 35),
        Phrase(2, 31, 41),
        Phrase(2, 41, 51),
        Phrase(2, 51, 67),
        Phrase(3, 67, 82),
        Phrase(4, 82, 106),
        Phrase(5, 107, 126),
        Phrase(5, 127, 135),
        Phrase(6, 135, 151),
        Phrase(6, 151, 165),
        Phrase(7, 165, 179),
        Phrase(7, 179, 191),
        Phrase(8, 191, 202),
        Phrase(8, 203, 211),
        Phrase(9, 211, 230),
        Phrase(9, 231, 250),
        Phrase(10, 251, 274),
        Phrase(11, 271, 291),
        Phrase(11, 289, 307),
        Phrase(12, 306, 319),
        Phrase(13, 319, 323),
        Phrase(13, 322, 331),
        Phrase(13, 331, 342),
    ]
)

# Henle edition
MOZART_K453_PIANO = InterleavedPractice(
    title="Mozart K453, Concerto #17 in G (piano)",
    phrases=[
        Phrase(5, 74, 90),
        Phrase(6, 91, 94),
        Phrase(6, 97, 100),
        Phrase(7, 100, 109),
        Phrase(8, 110, 121),
        Phrase(8, 122, 125),
        Phrase(8, 126, 135),
        Phrase(9, 139, 146),
        Phrase(10, 147, 152),
        Phrase(10, 153, 160),
        Phrase(11, 160, 164),
        Phrase(11, 164, 171),
        Phrase(12, 184, 192),
        Phrase(13, 192, 203),
        Phrase(13, 203, 207),
        Phrase(14, 211, 225),
        Phrase(15, 237, 242),
        Phrase(17, 257, 264),
        Phrase(17, 265, 272),
        Phrase(17, 273, 276),
        Phrase(18, 277, 286),
        Phrase(19, 286, 290),
        Phrase(19, 290, 297),
        Phrase(20, 298, 304),
        Phrase(20, 304, 311),
        Phrase(20, 311, 317),
        Phrase(21, 317, 319),
        Phrase(22, 328, 328),  # Cadenza
        Phrase(26, 30, 34),
        Phrase(26, 35, 42),
        Phrase(27, 45, 54),
        Phrase(28, 56, 64),
        Phrase(28, 69, 74),
        Phrase(29, 74, 80),
        Phrase(29, 81, 86),
        Phrase(30, 90, 94),
        Phrase(30, 95, 102),
        Phrase(31, 105, 111),
        Phrase(31, 115, 122),
        Phrase(32, 122, 123),  # Cadenza
        Phrase(33, 127, 130),
        Phrase(33, 131, 136),
    ]
)

# Henle edition 932 (Jost, Groethuysen)
MOZART_K497_SECONDO = InterleavedPractice(
    title="Mozart K497, Sonata in D for piano four-hands (secondo)",
    phrases=[
        Phrase(32, 1, 16),
        Phrase(32, 17, 35),
        Phrase(34, 35, 58),
        Phrase(34, 59, 64),
        Phrase(34, 65, 89),
        Phrase(36, 90, 117),
        Phrase(36, 118, 138),
        Phrase(36, 139, 153),
        Phrase(38, 154, 185),
        Phrase(38, 186, 208),
        Phrase(40, 209, 263),
        Phrase(42, 264, 287),
        Phrase(44, 288, 312),
        Phrase(46, 1, 20),
        Phrase(46, 21, 33),
        Phrase(48, 35, 43),
        Phrase(48, 43, 48),
        Phrase(48, 49, 64),
        Phrase(48, 64, 83),
        Phrase(50, 84, 100),
        Phrase(52, 102, 110),
        Phrase(52, 110, 123),
        Phrase(54, 1, 20),
        Phrase(54, 22, 36),
        Phrase(54, 37, 52),
        Phrase(56, 53, 76),
        Phrase(56, 76, 99),
        Phrase(58, 96, 114),
        Phrase(60, 119, 146),
        Phrase(60, 146, 164),
        Phrase(62, 164, 191),
        Phrase(64, 196, 229),
        Phrase(66, 231, 254),
        Phrase(66, 254, 264),
        Phrase(66, 264, 292),
        Phrase(68, 295, 299),
        Phrase(70, 299, 306),
        Phrase(70, 306, 324),
    ]
)


def next_from_list(phrases: list[Phrase]) -> Generator[Phrase, Any, Any]:
    """Generate phrases, hitting each one once before reshuffling."""
    i = 0
    while True:
        if i == 0:
            print(f"🔄 Shuffling {len(phrases)} phrases")
            random.shuffle(phrases)

        yield phrases[i]

        i = (i + 1) % len(phrases)


def practice(passages: InterleavedPractice) -> None:
    """Main practice session."""
    print(f"🎼 Interleaved practice for {passages.title}")
    print(f"📊 {len(passages.phrases)} phrases, {passages.total_measures} measures")
    print()

    stats = SessionStats(datetime.now())

    print("🎵 Starting practice session...")
    print("📝 Commands: [Enter] = next phrase, [s] = stats, [q] = quit")
    print("=" * 60)

    try:
        for i, next_passage in enumerate(next_from_list(passages.phrases), 1):
            print(f"\n[{i}] {next_passage}")
            print(f"📏 {next_passage.measure_count} measures")

            response = input("👉 ").strip().lower()

            # Record that we practiced a phrase
            stats.add_phrase()

            if response == 'q':
                break
            elif response == 's':
                print(f"\n📈 {stats}")
                input("Press Enter to continue...")
            # Default: continue to next phrase

    except KeyboardInterrupt:
        print("\n\n⏹️  Practice session interrupted")

    # Final statistics
    session_duration = datetime.now() - stats.start_time
    print("\n" + "=" * 60)
    print("📊 Session Summary")
    print("=" * 60)
    print(f"⏱️  Total session time: {session_duration}")
    print(f"🎵 Phrases practiced: {stats.phrases_practiced}")
    print("\n🎉 Hope it was good!")


def select_piece() -> InterleavedPractice:
    """Enhanced piece selection with better UI."""
    choices = [
        MOZART_K453_PIANO,
        FAURÉ_TRIO_OP120,
        BACH_GAMBA_SONATA_G,
        MOZART_K497_SECONDO,
    ]

    print("🎼 Interleaved Practice Assistant")
    print("=" * 40)

    while True:
        print("\n📚 Available pieces:")
        for i, choice in enumerate(choices, 1):
            print(f"{i:2}: {choice.title}")
            print(f"    {len(choice.phrases)} phrases, {choice.total_measures} measures")

        print("\n0: Quit")

        try:
            selection = input("\n🎯 Select a piece (1-{}): ".format(len(choices))).strip()

            if selection == '0':
                print("👋 Goodbye!")
                exit(0)

            selected = int(selection)
            if 1 <= selected <= len(choices):
                return choices[selected - 1]
            else:
                print(f"❌ Please enter a number between 1 and {len(choices)}")

        except ValueError:
            print("❌ Please enter a valid number")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            exit(0)


if __name__ == '__main__':
    try:
        selected_piece = select_piece()
        practice(selected_piece)
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
