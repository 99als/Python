def concatenate_files(filename1, filename2, new_filename):
    newfile = open(new_filename, 'a')
    file_one = open(filename1, 'r')
    file_two = open(filename2, 'r')
    file1 = file_one.read()
    file2 = file_two.read()
    newfile.write(file1)
    newfile.write(file2)
    file_one.close()
    file_two.close()
    newfile.close()

