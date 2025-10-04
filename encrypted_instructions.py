# ID: 143844203

from typing import List, Tuple

# Константы
DIGITS: str = "0123456789"
DECIMAL_BASE: int = 10
OPEN_BRACKET: str = "["
CLOSE_BRACKET: str = "]"

CharBuffer = List[str]
StackFrame = Tuple[CharBuffer, int]


def decode_instructions(encoded: str) -> str:
    """
    Декодирует сжатую строку инструкций с повторами и вложенными скобками.
    Примеры:
      3[a]2[bc]      -> aaabcbc
      3[a2[c]]       -> accaccacc
      2[abc]3[cd]ef  -> abcabccdcdcdef
    Сложность: O(n) по времени и памяти.
    """
    context_stack: List[StackFrame] = []  # Стек кадров (prefix_chars, repeat)
    current_chars: CharBuffer = []  # Текущая собираемая последовательность
    current_repeat: int = 0  # Множитель перед следующей '['

    for char in encoded:
        if char in DIGITS:
            current_repeat = current_repeat * DECIMAL_BASE + int(char)  # Сдвиг
        elif char == OPEN_BRACKET:
            context_stack.append((current_chars, current_repeat))
            current_chars = []
            current_repeat = 0
        elif char == CLOSE_BRACKET:
            prefix_chars, repeat = context_stack.pop()
            current_chars = prefix_chars + current_chars * repeat
            # current_chars * repeat — повторяет список
            # (например, ['a','b'] * 3 -> ['a','b','a','b','a','b']);
        else:
            current_chars.append(char)

    return "".join(current_chars)


if __name__ == "__main__":
    encoded_input: str = input().strip()
    print(decode_instructions(encoded_input))
