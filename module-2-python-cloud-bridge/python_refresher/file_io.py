# 📦 File I/O with Reproducibility Notes

with open("ritual.txt", "w") as f:
    f.write("This file was created during Module 2 setup.\n")

with open("ritual.txt", "r") as f:
    content = f.read()
    print("File content:", content)