#!/usr/bin/env python3

import builtins
import inspect


class ColorPalette:
    """Хранит название палитры и список цветов RGB."""

    def __init__(self, name, colors):
        self.name = name
        self.colors = colors

    @property
    def size(self):
        """Количество цветов в палитре."""
        return len(self.colors)

    @property
    def hex_colors(self):
        """Цвета в привычном формате для веб-страниц."""
        return [f"#{red:02X}{green:02X}{blue:02X}" for red, green, blue in self.colors]

    def color_at(self, index):
        """Возвращает цвет по номеру, начиная с нуля."""
        return self.colors[index]

    def __iter__(self):
        """Позволяет перебирать цвета в цикле for."""
        return iter(self.colors)


# Значения RGB идут от тёмно-синего к светло-зелёному.
palette = ColorPalette(
    "Океан",
    [
        (11, 37, 69),
        (20, 99, 130),
        (46, 160, 157),
        (152, 219, 194),
        (237, 247, 239),
    ],
)


def explain_palette():
    print(f"Палитра «{palette.name}»")
    print("RGB — это три числа: красный, зелёный и синий (каждое от 0 до 255).")

    print("\nАтрибуты — данные, которые хранит палитра:")
    attributes = [
        ("name", "название палитры"),
        ("colors", "цвета в виде троек RGB"),
        ("size", "количество цветов"),
        ("hex_colors", "те же цвета в формате #RRGGBB"),
    ]
    for name, explanation in attributes:
        print(f"  {name} — {explanation}: {getattr(palette, name)}")

    print("\nМетоды — действия, которые умеет выполнять палитра:")
    methods = [
        ("color_at", "возвращает цвет по номеру; нумерация начинается с нуля"),
        ("__iter__", "позволяет пройти по всем цветам в цикле for"),
    ]
    for name, explanation in methods:
        method = getattr(palette, name)
        print(f"  {name}{inspect.signature(method)} — {explanation}")


def show_exception_types():
    """Выводит встроенные типы исключений и коротко объясняет, что это."""
    names = []
    for name, item in inspect.getmembers(builtins, inspect.isclass):
        if issubclass(item, BaseException):
            names.append(name)

    print("\nВстроенные типы исключений Python:")
    print("Исключения описывают ошибки, которые можно обработать с помощью try/except.")
    for name in sorted(names, key=str.casefold):
        print(f"  {name}")


def main():
    explain_palette()
    show_exception_types()


if __name__ == "__main__":
    main()
