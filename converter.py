import rawpy
import imageio
import os

raw_extensions = (".cr2", ".CR2")
output_extensions = (".jpeg", ".JPEG", ".jpg", ".JPG", ".png", ".PNG")

def convert(input_file: str, output_file: str) -> str:
    """
    Take a file path and the target ouput (jpeg or png) and return the output file path if success.
    Create the ouput path if needed.
    Else: RAISE ERROR
    -------------
    input_file: str, a file path ended with a raw extension
    output_file: str, a file path ended with the desired format (.jpeg or .png)
    """
    output_dir, output_name = os.path.split(output_file) 

    if not os.path.isfile(input_file):
        raise ValueError("Input path must be a file")
    if not input_file.endswith(raw_extensions):
        raise ValueError('Input file does not have a raw extension')
    if not output_name.endswith(output_extensions):
        raise ValueError("Output file does not have a correct extension")

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
       
    with rawpy.imread(input_file) as raw:
        rgb = raw.postprocess()
    imageio.imsave(output_file, rgb)

    return output_file