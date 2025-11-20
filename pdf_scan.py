from pypdf import PdfReader
file_name = input("Enter PDF file name: ")
keywords = ['/JS', 'JavaScript', '/AA', '/OpenAction']
pdf_is_safe = True
reader = PdfReader(file_name)
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ""
    if not text:
        print(f"Page {i} has no text.")
        continue
    for k in keywords:
        if k in text:
            print(f"Found '{k}' on page {i}")
            pdf_is_safe = False
print("The PDF looks safe." if pdf_is_safe else "The PDF might be unsafe.")