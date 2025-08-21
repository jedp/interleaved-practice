#!/usr/bin/env python3

"""
Script to facilitate Molly Gebrian's technique of interleaved practice.
"""

import random
from dataclasses import dataclass
from typing import Any, Generator


@dataclass
class Phrase:
    page: int
    from_measure: int
    to_measure: int

    def __str__(self) -> str:
        return f"Page {self.page:3}, measures {self.from_measure:3} \u2013 {self.to_measure:3}"


@dataclass
class InterleavedPractice:
    title: str
    phrases: list[Phrase]


# Henle edition 932 (Jost, Groethuysen)
MOZART_K497_SECONDO = InterleavedPractice(
    title="Mozart K497",
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


def next_from_list(l: list[Phrase]) -> Generator[Phrase, Any, Any]:
    i = 0
    while True:
        if i == 0:
            print(f"Shuffling {len(l)} phrases")
            random.shuffle(l)

        yield l[i]

        i = (i + 1) % len(l)


def practice(passages: InterleavedPractice) -> None:
    print(f"Interleaved practice for {passages.title}. {len(passages.phrases)} phrases.")

    i = 0

    try:
        for next_passage in next_from_list(passages.phrases):
            i += 1
            print(f"{i:2}: {next_passage}. (enter to continue)")
            input()

    except KeyboardInterrupt:
        print("\nHope it went ok!")


if __name__ == '__main__':
    practice(MOZART_K497_SECONDO)
