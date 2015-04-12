# rename.py

### Description

Renames all image files with `.jpg` / `.jpeg`, `.png`, `.gif` extensions (upper or lowercase) to a 10 character long combination of random letters and numbers, example: `r7uh17i986.jpg`
 
Useful for making random assortment of images for slideshows, digital photo frames, etc.

Files without above image extensions are excluded. 

Before renaming, lists number of non image files found and asks user for confirmation before proceeding. Outputs to screen:

`original image filename --> new image filename`   

### Usage

Place images you want to rename in same directory as `rename.py`, then run rename.py:

Linux / OSX: 

```
$ ./rename.py
```

Windows:

```
$ python rename.py
```

##### Fake Image Testing

`fake_images/` Contains code for testing w/ generated fake (0 bytes) images. To test create fake images:

```
$ python fake_images/make_fake_images.py
```

To clean them up:

```
$ python fake_images/cleanup_fake_images.py
```

### Compatibility

* Python 2.7.x
* Python 3.4.x



 


