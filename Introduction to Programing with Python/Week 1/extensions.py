# import sys
#
# user_input = input("File Name: ")
# words = user_input.split(sep = ".")
# list = { "gif", "jpg", "jpeg", "png", "pdf", "txt", "txt", "zip" }
# if len(words) == 1:
#     print("application/octet-stream")
#     sys.exit()
# if words[1] in list:
#     print(f"{words[0]}/{words[1]}")
#     sys.exit()
# print("application/octet-stream")


import sys

def main():
    try:
        filename = input("File name: ").strip()
        mime_type = determine_mime_type(filename)
        print(mime_type)
    except FileNotFoundError:
        sys.exit("File does not exist")

def determine_mime_type(filename):

    extensions = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
        "bin": "application/octet-stream"
    }

    if "." not in filename:
        return "application/octet-stream"

    extension = filename.rsplit(".", 1)[-1].lower()

    if extension in extensions:
        return extensions[extension]

    return "application/octet-stream"

if __name__ == "__main__":
    main()
