# GpsTag

This tool makes use of another tool, *exiftool* to tag photos based on the name
of the directory they are contained in. The naming scheme is described by
the following regex:

([NS])(\d+) (\d+) (\d+\.\d+) ([EW])(\d+) (\d+) (\d+\.\d+)

For example: N47 29 51.0 E19 2 16.9 becomes the following EXIF tags:

GPSLatitudeRef=N
GPSLatitude="47 29 51.0"
GPSLongitudeRef=E
GPSLongitude="19 2 16.9"

These tags are enough to convince Apple's Photos app to treat the photos as part
of a "Moment", and put them on the map etc. Handy for merging a set of photos
taken on a DSLR into photos taken by a phone.
