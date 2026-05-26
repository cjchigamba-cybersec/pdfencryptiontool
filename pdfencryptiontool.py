import sys
from pypdf import PdfReader, PdfWriter
def protect_pdf(input_file, output_file, password):
    reader = PdfReader(input_file)
    writer = PdfWriter(clone_from=reader)
    writer.encrypt(password)
    with open(output_file, "wb") as output:
        writer.write(output)
    print("Completed," + output_file + " is  now password protected using your provided password.")
if __name__ == "__main__":
    if len(sys.argv) == 4:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        pw = sys.argv[3]
    else:
        input_file = input("Enter your PDF file: ")
        output_file = input("What should the new file be called: ")
        pw = input("Enter a password: ")
    try:
        protect_pdf(input_file, output_file, pw)
    except FileNotFoundError:
        print("Error: could not find " + input_file)
    except Exception as e:
        print("Something went wrong:", e)