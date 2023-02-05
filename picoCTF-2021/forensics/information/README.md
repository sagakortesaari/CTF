# information

Files can always be changed in a secret way. Can you find the flag? cat.jpg

## Solution

Here's a cute lil cat from `cat.jpg`:

![cat](cat.jpg)

First thought was to look at the .jpg's metadata and see if anything has been modified:

```
$  exiftool cat.jpg
ExifTool Version Number         : 11.88
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 kB
File Modification Date/Time     : 2023:02:04 17:09:46+01:00
File Access Date/Time           : 2023:02:04 17:13:17+01:00
File Inode Change Date/Time     : 2023:02:04 17:09:46+01:00
File Permissions                : rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

`cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9` seems interesting. Base64 decoding this reveals a flag: `picoCTF{the_m3tadata_1s_modified}`.