import re
from pypdf import PdfReader


def extract_and_save_stressed_words(pdf_path, output_txt_path):
    sections = [
        "Имена существительные",
        "Имена прилагательные",
        "Глаголы",
        "Причастия и отглагольные прилагательные",
        "Деепричастия",
        "Наречия",
    ]

    result = {sec: [] for sec in sections}
    current_section = None
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

    word_pattern = re.compile(
        r"\b(?=[а-яё]*[А-ЯЁ][а-яё]*\b)[а-яёА-ЯЁёЁ]+(?:-[а-яёА-ЯЁёЁ]+)*\b"
    )

    reader = PdfReader(pdf_path)

    for page in reader.pages:
        text = page.extract_text()
        if not text:
            continue

        for line in text.splitlines():
            line = line.strip()

            if current_section == "Наречия" and (
                "обратите внимание" in line.lower()
                or "где взять" in line.lower()
                or "номер:" in line.lower()
            ):
                current_section = None

            found_section = False
            for sec in sections:
                if sec.lower() in line.lower():
                    current_section = sec
                    found_section = True
                    break

            if found_section:
                continue

            if current_section:
                words = word_pattern.findall(line)
                for word in words:
                    if len(word) <= 1:
                        continue

                    upper_letters = [c for c in word if c.isupper()]
                    if upper_letters:
                        stressed_letter = upper_letters[0]
                        if stressed_letter in vowels:
                            if word not in result[current_section]:
                                result[current_section].append(word)

    with open(output_txt_path, "w", encoding="utf-8") as f:
        for pos, words in result.items():
            f.write(f"--- {pos} (всего: {len(words)}) ---\n")
            if words:
                words_sorted = sorted(words, key=lambda s: s.lower())
                for i in range(0, len(words_sorted), 10):
                    line_to_write = ", ".join(words_sorted[i : i + 10])
                    f.write(line_to_write + "\n")
            else:
                f.write("(слова не найдены)\n")
            f.write("\n\n")

    print(f"Готово! Все слова успешно сохранены в файл: {output_txt_path}")


if __name__ == "__main__":
    pdf_file_path = "Фонетика и орфоэпия.pdf"
    output_file_path = "stressed_words.txt"

    try:
        extract_and_save_stressed_words(pdf_file_path, output_file_path)
    except FileNotFoundError:
        print(f"Ошибка: Файл {pdf_file_path} не найден.")
