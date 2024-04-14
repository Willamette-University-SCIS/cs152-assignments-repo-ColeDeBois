# Welcome To Lyrics Compressor!

The lyrics compressor will take the lyrics to a song in .txt file and compress their physical space on the computer. It achieves this by creating a hash map of the words in the song and their sequential placement in the song (e.g. the first word is 1). This program capable of holding the lyrics in memory, and can store one compressed song in disk space as well! 

To start, run program.py
* Then you'll be prompted to either:
    * provide the name of a file with lyrics in it
    * or you can check the current stored song on the disk.
      * if there is nothing in storage, you'll be returned to the main menu
      * if there is something in storage, you'll be able to either:
        * delete it
        * move it to memory (for decompressing or view the word positions)
        * or do nothing and return to the main menu

Once theres lyrics in memory you'll have the options from before or you can:
* view the word positions
* or decompress the lyrics into another file


Warnings:
* deleting the `disk_storage.txt` will break the program
* providing inputs that are not listed will force you to return to the main menu

## Screenshots:
![Output](https://github.com/Willamette-University-SCIS/cs152-assignments-repo-ColeDeBois/assets/112717966/048a90ef-4057-470a-a27f-1db20480f938)



  


