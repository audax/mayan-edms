# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

DEFAULT_ZOOM_LEVEL = 100
DEFAULT_ROTATION = 0
DEFAULT_PAGE_NUMBER = 1
DEFAULT_FILE_FORMAT = u'jpeg'
DEFAULT_FILE_FORMAT_MIMETYPE = u'image/jpeg'

DIMENSION_SEPARATOR = u'x'

TRANSFORMATION_RESIZE = u'resize'
TRANSFORMATION_ROTATE = u'rotate'
TRANSFORMATION_DENSITY = u'density'
TRANSFORMATION_ZOOM = u'zoom'

TRANSFORMATION_CHOICES = {
    TRANSFORMATION_RESIZE: {
        'label': _(u'Resize'),
        'description': _(u'Resize.'),
        'arguments': [
            {'name': 'width', 'label': _(u'width'), 'required': True},
            {'name': 'height', 'label': _(u'height'), 'required': False},
        ]
    },
    TRANSFORMATION_ROTATE: {
        'label': _(u'Rotate'),
        'description': _(u'Rotate by n degress.'),
        'arguments': [
            {'name': 'degrees', 'label': _(u'degrees'), 'required': True}
        ]
    },
    TRANSFORMATION_DENSITY: {
        'label': _(u'Density'),
        'description': _(u'Change the resolution (ie: DPI) without resizing.'),
        'arguments': [
            {'name': 'width', 'label': _(u'width'), 'required': True},
            {'name': 'height', 'label': _(u'height'), 'required': False},
        ]
    },
    TRANSFORMATION_ZOOM: {
        'label': _(u'Zoom'),
        'description': _(u'Zoom by n percent.'),
        'arguments': [
            {'name': 'percent', 'label': _(u'percent'), 'required': True}
        ]
    },
}

FILE_FORMATS = {
    '3FR': _(u'Hasselblad Photo RAW, CFV/H3D39II'),
    '8BIM': _(u'Photoshop resource format'),
    '8BIN': _(u'Photoshop resource format'),
    '8BIMTEXT': _(u'Photoshop resource text format'),
    '8BIMWTEXT': _(u'Photoshop resource wide text format'),

    'A': _(u'Raw alpha samples'),
    'AI': _(u'Adobe Illustrator CS2'),
    'APP1': _(u'Raw application information'),
    'APP1JPEG': _(u'Raw JPEG binary data'),
    'ART': _(u'PFS: 1st Publisher Clip Art'),
    'ARW': _(u'Sony Alpha DSLR Raw Image Format'),
    'AVI': _(u'Microsoft Audio/Visual Interleaved'),
    'AVS': _(u'AVS X image'),

    'B': _(u'Raw blue samples'),
    'BGR': _(u'Raw blue, green, and red samples'),
    'BGRA': _(u'Raw blue, green, red and alpha samples'),
    'BMP': _(u'Microsoft Windows bitmap image'),
    'BMP2': _(u'Microsoft Windows bitmap image version 2'),
    'BMP3': _(u'Microsoft Windows bitmap image version 3'),
    'BRF': _(u'BRF ASCII Braille format'),
    'BRG': _(u'Raw blue, red, and green samples'),

    'C': _(u'Raw cyan samples'),
    'CACHE': _(u'Magick Persistent Cache image format'),
    'CAL': _(u'Continuous Acquisition and Life-cycle Support Type 1 image'),
    'CALS': _(u'Continuous Acquisition and Life-cycle Support Type 1 image'),
    'CAPTION': _(u'Image caption'),
    'CIN': _(u'Cineon Image File'),
    'CIP': _(u'Cisco IP phone image format'),
    'CLIP': _(u'Image Clip Mask'),
    'CMYK': _(u'Raw cyan, magenta, yellow, and black samples'),
    'CMYKA': _(u'Raw cyan, magenta, yellow, black, and opacity samples'),
    'CR2': _(u'Canon Digital Camera Raw Image Format'),
    'CRW': _(u'Canon Digital Camera Raw Image Format'),
    'CUR': _(u'Microsoft Cursor Icon'),
    'CUT': _(u'DR Halo'),

    'DCM': _(u'Digital Imaging and Communications in Medicine image'),
    'DCR': _(u'Kodak Digital Camera Raw Image File'),
    'DCX': _(u'ZSoft IBM PC multi-page Paintbrush'),
    'DDS': _(u'Microsoft DirectDraw Surface'),
    'DFONT': _(u'Multi-face font package (Freetype 2.4.2)'),
    'DJVU': _(u'Déjà vu'),
    'DNG': _(u'Adobe Digital Negative'),
    'DOT': _(u'Graphviz'),
    'DPX': _(u'SMPTE 268M-2003 (DPX 2.0)'),

    'EPDF': _(u'Encapsulated Portable Document Format'),
    'EPI': _(u'Adobe Encapsulated PostScript Interchange format'),
    'EPS': _(u'Adobe Encapsulated PostScript'),
    'EPS2': _(u'Adobe Level II Encapsulated PostScript'),
    'EPS3': _(u'Adobe Level III Encapsulated PostScript'),
    'EPSF': _(u'Adobe Encapsulated PostScript'),
    'EPSI': _(u'Adobe Encapsulated PostScript Interchange format'),
    'EPT': _(u'Adobe Encapsulated PostScript with TIFF preview'),
    'EPT2': _(u'Adobe Level II Encapsulated PostScript with TIFF preview'),
    'EPT3': _(u'Adobe Level III Encapsulated PostScript with TIFF preview'),
    'ERF': _(u'Epson RAW Format'),
    'EXIF': _(u'Exif digital camera binary data'),
    'EXR': _(u'High Dynamic-range (HDR)'),

    'FAX': _(u'Group 3 FAX (Not TIFF Group3 FAX)'),
    'FLI': _(u'Autodesk FLI animations file'),
    'FLC': _(u'Autodesk FLC animations file'),
    'FITS': _(u'Flexible Image Transport System'),
    'FPX': _(u'Kodak FlashPix file'),
    'FRACTAL': _(u'Plasma fractal image'),
    'FTS': _(u'Flexible Image Transport System'),

    'G': _(u'Raw green samples'),
    'G3': _(u'Group 3 FAX'),
    'GBR': _(u'Raw green, blue, and red samples'),
    'GBR_PIL': _(u'GIMP brush file'),
    'GIF': _(u'CompuServe graphics interchange format (version 89a)'),
    'GIF87': _(u'CompuServe graphics interchange format (version 87a)'),
    'GRADIENT': _(u'Gradual passing from one shade to another'),
    'GRAY': _(u'Raw gray samples'),
    'GRB': _(u'Raw green, red, and blue samples'),
    'GROUP4': _(u'Raw CCITT Group4'),

    'HISTOGRAM': _(u'Histogram of the image'),
    'HRZ': _(u'HRZ: Slow scan TV'),
    'HTM': _(u'Hypertext Markup Language and a client-side image map'),
    'HTML': _(u'Hypertext Markup Language and a client-side image map'),

    'ICB': _(u'Truevision Targa image'),
    'ICC': _(u'ICC Color Profile'),
    'ICM': _(u'ICC Color Profile'),
    'ICO': _(u'Microsoft Icon'),
    'ICON': _(u'Microsoft Icon'),
    'IDENTITY': _(u'Hald CLUT identity image'),
    'IM': _(u'LabEye image format'),
    'IMAGE': _(u'GraphicsMagick Embedded Image'),
    'INFO': _(u'The image format and characteristics'),
    'INLINE': _(u'Base64-encoded inline images'),
    'IPL': _(u'IPL Image Sequence'),
    'IPTC': _(u'IPTC Newsphoto'),
    'IPTCTEXT': _(u'IPTC Newsphoto text format'),
    'IPTCWTEXT': _(u'IPTC Newsphoto text format'),
    'ISOBRL': _(u'ISO/TR 11548-1 format'),

    'J2C': _(u'JPEG-2000 Code Stream Syntax'),
    'JNG': _(u'JPEG Network Graphics (libpng 1.2.42,1.2.44, zlib 1.2.3.3,1.2.3.4)'),
    'JP2': _(u'JPEG-2000 JP2 File Format Syntax'),
    'JPC': _(u'JPEG-2000 Code Stream Syntax'),
    'JPEG': _(u'Joint Photographic Experts Group JFIF format (IJG JPEG 62)'),
    'JPG': _(u'Joint Photographic Experts Group JFIF format (IJG JPEG 62)'),
    'JPX': _(u'JPEG-2000 File Format Syntax'),

    'K': _(u'Raw black samples'),
    'K25': _(u'Kodak Digital Camera Raw Image Format'),
    'KDC': _(u'Kodak Digital Camera Raw Image Format'),

    'LABEL': _(u'Image label'),

    'M': _(u'Raw magenta samples'),
    'M2V': _(u'MPEG Video Stream'),
    'M4V': _(u'Raw MPEG-4 Video'),
    'MAP': _(u'Colormap intensities and indices'),
    'MAT': _(u'MATLAB image format'),
    'MATTE': _(u'MATTE raw opacity format'),
    'MCIDAS': _(u'8-bit McIdas area file'),
    'MIC': _(u'Microsoft Image Composer (MIC) file'),
    'MIFF': _(u'Magick Image File Format'),
    'MNG': _(u'Multiple-image Network Graphics (libpng 1.2.42,1.2.44, zlib 1.2.3.3,1.2.3.4)'),
    'MONO': _(u'Raw Bi-level bitmap in least-significant-byte first order'),
    'MOV': _(u'MPEG Video Stream'),
    'MP4': _(u'MPEG-4 Video Stream'),
    'MPC': _(u'Magick Persistent Cache image format'),
    'MPEG': _(u'MPEG Video Stream'),
    'MPG': _(u'MPEG Video Stream'),
    'MRW': _(u'Sony (Minolta) Raw Image File'),
    'MSL': _(u'Magick Scripting Language'),
    'MSP': _(u'Windows 1 and 2 MSP file format'),
    'MSVG': _(u'ImageMagick\'s own SVG internal renderer'),
    'MTV': _(u'MTV Raytracing image format'),
    'MVG': _(u'Magick Vector Graphics'),

    'NEF': _(u'Nikon Digital SLR Camera Raw Image File'),
    'NULL': _(u'Constant image of uniform color'),

    'O': _(u'Raw opacity samples'),
    'ORF': _(u'Olympus Digital Camera Raw Image File'),
    'OTB': _(u'On-the-air bitmap'),
    'OTF': _(u'Open Type font (Freetype 2.4.2)'),

    'P7': _(u'Xv thumbnail format'),
    'PAL': _(u'16bit/pixel interleaved YUV'),
    'PALM': _(u'Palm pixmap'),
    'PAM': _(u'Common 2-dimensional bitmap format'),
    'PATTERN': _(u'Predefined pattern'),
    'PBM': _(u'Portable bitmap format (black and white)'),
    'PCD': _(u'Photo CD'),
    'PCDS': _(u'Photo CD'),
    'PCL': _(u'Page Control Language'),
    'PCT': _(u'Apple Macintosh QuickDraw/PICT'),
    'PCX': _(u'ZSoft IBM PC Paintbrush'),
    'PDB': _(u'Palm Database ImageViewer Format'),
    'PDF': _(u'Portable Document Format'),
    'PDFA': _(u'Portable Document Archive Format'),
    'PEF': _(u'Pentax Electronic File'),
    'PES': _(u'Embrid Embroidery Format'),
    'PFA': _(u'Postscript Type 1 font (ASCII) (Freetype 2.4.2)'),
    'PFB': _(u'Postscript Type 1 font (binary) (Freetype 2.4.2)'),
    'PFM': _(u'Portable float format'),
    'PGM': _(u'Portable graymap format (gray scale)'),
    'PGX': _(u'JPEG-2000 VM Format'),
    'PICON': _(u'Personal Icon'),
    'PICT': _(u'Apple Macintosh QuickDraw/PICT'),
    'PIX': _(u'Alias/Wavefront RLE image format'),
    'PIXAR': _(u'PIXAR raster file'),
    'PJPEG': _(u'Joint Photographic Experts Group JFIF format (62)'),
    'PLASMA': _(u'Plasma fractal image'),
    'PNG': _(u'Portable Network Graphics (libpng 1.2.42,1.2.44, zlib 1.2.3.3,1.2.3.4)'),
    'PNG24': _(u'24-bit RGB PNG, opaque only (libpng 1.2.42,1.2.44, zlib 1.2.3.3,1.2.3.4)'),
    'PNG32': _(u'32-bit RGBA PNG, semitransparency OK (libpng 1.2.42,1.2.44, zlib 1.2.3.3,1.2.3.4)'),
    'PNG8': _(u'8-bit indexed PNG, binary transparency only (libpng 1.2.42,1.2.44, zlib 1.2.3.3,1.2.3.4)'),
    'PNM': _(u'Portable anymap'),
    'PPM': _(u'Portable pixmap format (color)'),
    'PREVIEW': _(u'Show a preview an image enhancement, effect, or f/x'),
    'PS': _(u'Adobe PostScript'),
    'PS2': _(u'Adobe Level II PostScript'),
    'PS3': _(u'Adobe Level III PostScript'),
    'PSB': _(u'Adobe Large Document Format'),
    'PSD': _(u'Adobe Photoshop bitmap'),
    'PTIF': _(u'Pyramid encoded TIFF'),
    'PWP': _(u'Seattle Film Works'),

    'R': _(u'Raw red samples'),
    'RAF': _(u'Fuji CCD-RAW Graphic File'),
    'RAS': _(u'SUN Rasterfile'),
    'RBG': _(u'Raw red, blue, and green samples'),
    'RGB': _(u'Raw red, green, and blue samples'),
    'RGBA': _(u'Raw red, green, blue, and matte samples'),
    'RGBO': _(u'Raw red, green, blue, and opacity samples'),
    'RLA': _(u'Alias/Wavefront image'),
    'RLE': _(u'Utah Run length encoded image'),

    'SCR': _(u'ZX-Spectrum SCREEN$'),
    'SCT': _(u'Scitex HandShake'),
    'SFW': _(u'Seattle Film Works'),
    'SGI': _(u'Irix RGB image'),
    'SHTML': _(u'Hypertext Markup Language and a client-side image map'),
    'SR2': _(u'Sony Raw Format 2'),
    'SRF': _(u'Sony Raw Format'),
    'STEGANO': _(u'Steganographic image'),
    'SUN': _(u'SUN Rasterfile'),
    'SVG': _(u'Scalable Vector Graphics (XML 2.7.6, RSVG 2.32.0)'),
    'SVGZ': _(u'Scalable Vector Graphics (ZIP compressed) (XML 2.7.6, RSVG 2.32.0)'),

    'TEXT': _(u'Text'),
    'TGA': _(u'Truevision Targa image'),
    'THUMBNAIL': _(u'EXIF Profile Thumbnail'),
    'TIFF': _(u'Tagged Image File Format (LIBTIFF, Version 3.9.4)'),
    'TIFF64': _(u'Tagged Image File Format (64-bit) (LIBTIFF, Version 3.9.4)'),
    'TILE': _(u'Tile image with a texture'),
    'TIM': _(u'PSX TIM'),
    'TOPOL': _(u'TOPOL X Image'),
    'TTC': _(u'TrueType font collection (Freetype 2.4.2)'),
    'TTF': _(u'TrueType font (Freetype 2.4.2)'),
    'TXT': _(u'Text'),

    'UBRL': _(u'Unicode Text format'),
    'UIL': _(u'X-Motif UIL table'),
    'UYVY': _(u'16bit/pixel interleaved YUV'),

    'VDA': _(u'Truevision Targa image'),
    'VICAR': _(u'VICAR rasterfile format'),
    'VID': _(u'Visual Image Directory'),
    'VIFF': _(u'Khoros Visualization image'),
    'VST': _(u'Truevision Targa image'),

    'WBMP': _(u'Wireless Bitmap (level 0) image'),
    'WMF': _(u'Windows Meta File'),
    'WPG': _(u'Word Perfect Graphics'),
    'WMV': _(u'Windows Media Video'),
    'WMZ': _(u'Compressed Windows Meta File'),

    'X': _(u'X Window System'),
    'X3F': _(u'Foveon X3 (Sigma/Polaroid) Raw picture file'),
    'XBM': _(u'X Windows system bitmap (black and white)'),
    'XC': _(u'Constant image uniform color'),
    'XCF': _(u'GIMP image'),
    'XMP': _(u'Adobe XML metadata'),
    'XPM': _(u'X Windows system pixmap (color)'),
    'XPS': _(u'Microsoft XML Paper Specification'),
    'XV': _(u'Khoros Visualization image'),
    'XVTHUMB': _(u'XV thumbnail file'),
    'XWD': _(u'X Windows system window dump (color)'),

    'Y': _(u'Raw yellow samples'),
    'YUV': _(u'CCIR 601 4:1:1 or 4:2:2 (8-bit only)'),
}

DEFAULT_LIBREOFFICE_PATH = '/usr/bin/libreoffice'
