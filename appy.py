from hmac import trans_36
from pdfminer.high_level import extract_text
import re


# TRANSCRIPT PARSE CODE
def extract_rows_below_keyword(pdf_path, keyword):
    try:
        # Define the words to exclude
        excluded_words = {
            "Main",
            "List",
            "Term",
            "GPA",
            "CEU",
            "and",
            "Type",
            "End",
            "Good",
            "Fall",
            "ted",
            "Enac",
            "The",
            "New",
            "Full",
            "Web",
            "Lin",
            "Alg",
            "Diff",
            "Eqs",
            "Data",
            "Art",
            "Lab",
            "Heal",
            "Eng",
            "Age",
            "with",
            "TA-",
        }

        # Extract text from the PDF file
        with open(pdf_path, "rb") as file:
            pdf_text = extract_text(file)

        # Split the text into lines
        lines = pdf_text.split("\n")

        word_pattern = r"\b[A-Z]{3,4}\b"

        # Search for the keyword
        rows = []
        keyword_found = False
        for line in lines:
            if keyword in line:
                keyword_found = True
                continue  # Skip the line with the keyword
            if (
                keyword_found and line.strip()
            ):  # Check if keyword was found and the line is not empty
                # Split the line into words
                classes = re.findall(word_pattern, line)
                words = line.split()
                # Filter words based on length, exclusion list, and characters to exclude
                filtered_words = []
                for word in words:
                    if (
                        len(word) in (3, 4)
                        and word.strip() not in excluded_words
                        and not any(char in word for char in "/:.")
                    ):
                        if len(word) == 4 and word.isdigit():
                            continue
                        if word.isalpha() and not word.isupper():
                            continue
                        else:
                            filtered_words.append(word.strip())
                rows.extend(filtered_words)
                # print(filtered_words)

        return rows

    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None


def extract_text_first_line(pdf_path):
    try:
        # Extract text from the PDF file
        with open(pdf_path, "rb") as file:
            pdf_text = extract_text(file)

        # Split the text into lines
        lines = pdf_text.split("\n")
        print(lines)  # testing code
        # Extract the text from the first line
        if lines:
            first_line_text = lines[12].strip()
            return first_line_text
        else:
            return None

    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None
