def modify_file():
    try:
        # 🧪 Ask user for the input file name
        filename = input("Enter the name of the file to read (e.g., input.txt): ")

        # 🖋️ Try opening the input file
        with open(filename, 'r') as infile:
            content = infile.read()

        # 🖋️ Modify the file content: uppercase it and count words
        word_count = len(content.split())
        modified_content = content.upper()

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as outfile:
            outfile.write("MODIFIED CONTENT:\n")
            outfile.write(modified_content)
            outfile.write("\n\nWORD COUNT: {}\n".format(word_count))

        print(f"✅ Success! Modified file saved as '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except IOError:
        print("❌ Error: Could not read the file due to an I/O problem.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Run the program
modify_file()
