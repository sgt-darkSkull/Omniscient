import os, re


def p_list(lst, clr=False):
    rstr = ''
    for val in lst:
        if isinstance(val, list):
            val = p_list(val)
        elif isinstance(val, dict):
            val = p_dict(val)
        if clr:
            rstr += re.sub(r'(\d)\1+', r'\1', str(val).strip()) + '\n'
        else:
            rstr += str(val) + '\n'
    return rstr


def p_dict(dct, clr=False):
    rstr = ''
    for ky in dct:
        val = dct[ky]
        if isinstance(val, list):
            val = p_list(val)
        elif isinstance(val, dict):
            val = p_dict(val)
        if clr:
            rstr += ky + ' : ' + re.sub(r'(\d)\1+', r'\1', str(val).strip()) + '\n'
        if (str(val) != 'None'):
            attribute = ''.join(ky.split('_')[-1])
            res = attribute[0].upper() + attribute[1:]
            rstr += res + ' : ' + clear(str(val)) + '\n'
    return rstr


def clear(txt):
    txt = str(txt)
    txt = txt.replace('�', ' ').replace('\\\\', '\\').replace('\\n', '').replace("''", '').replace("\t", ' ').replace(
        "\r",
        '\n').strip().replace(
        '  ', ' ')
    return txt


class Report:

    def __init__(self, location, file_name, head):
        self.wdir = location
        if not os.path.isdir(self.wdir):
            os.mkdir(self.wdir)
        self.fname = file_name
        self.md = open(location + file_name, 'w')
        self.md.write(f"# {head}\n")
        self.p_fix = -1

    def add_hn(self, hn, txt):
        if hn < 2:
            hn = 2
        elif hn > 6:
            hn = 6
        self.md.write(f"{'#' * hn} {txt}\n")

    def add_cd(self, code):
        self.md.write(f'```\n{code}\n```\n\n')

    def add_txt(self, txt):
        self.md.write(txt + '\n')

    def add_img(self, img_loc, o_name):
        if not os.path.isdir(self.wdir + 'assets.md'):
            os.mkdir(self.wdir + 'assets.md')
        with open(self.wdir + f"assets.md/{o_name}", 'wb') as md_img:
            imgfile = open(img_loc, 'rb').read()
            md_img.write(imgfile)

        self.md.write(f"![Image-{o_name}](assets.md/{o_name})\n")
