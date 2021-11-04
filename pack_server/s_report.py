import os


class Report:

    def __init__(self, location, file_name, head):
        self.wdir = location
        self.fname = file_name
        self.md = open(location + file_name, 'w')
        self.md.write(f"# {head}\n")

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
