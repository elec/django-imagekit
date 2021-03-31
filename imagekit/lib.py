# flake8: noqa

# Required PIL classes may or may not be available from the root namespace
# depending on the installation method used.
try:
    from PIL import Image, ImageChops, ImageColor, ImageDraw, ImageEnhance, ImageFile, ImageFilter, ImageStat
except ImportError:
    try:
        import Image
        import ImageChops
        import ImageColor
        import ImageDraw
        import ImageEnhance
        import ImageFile
        import ImageFilter
        import ImageStat
    except ImportError:
        raise ImportError('ImageKit was unable to import the Python Imaging Library. Please confirm it`s installed and available on your current Python path.')
