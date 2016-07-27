# -*- coding: utf-8 -*-


def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item


def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))


def parse_options(l):
    """
    :param l: str
    :return: [opt1, opt2,... ]
    """
    if '[' not in l:
        return []
    options_start = l.index('[') + 1
    options_end = l.index(']')
    return [o.strip() for o in l[options_start:options_end].split(',')]


def make_package_list(preamble):
    """
    :param preamble: lst of str in the preamble.
    :return: [
        ['package_name1', [opt1, opt2,...]],
        ....
     ]
    """
    packages = []

    for l in preamble:
        if '\\usepackage' not in l:
            continue

        pkg_start = l.index('{') + 1
        pkg_end = l.index('}')
        pkg = l[pkg_start:pkg_end]

        if ',' in pkg:
            for pkgl in pkg.split(','):
                # Not possible that a pkg has options in that case?
                packages.append([pkgl.strip(), []])
            continue

        packages.append([pkg, parse_options(l)])
        packages = sort_and_deduplicate(packages)
    return packages


def merge_packages(pkg1, pkg2):
    newpackages = []
    pkgl = [pkg for pkg, opt in pkg1]
    for pkg, opt in pkg2:
        if pkg in pkgl:
            pkgi = pkgl.index(pkg)
            newpackages.append([pkg, sort_and_deduplicate(pkg1[pkgi][1] + opt)])
        else:
            newpackages.append([pkg, list(set(opt))])
    return newpackages


class LaTeX:
    def __init__(self, lines=None):
        """
        We model a LaTeX document as:
         - a list of lines composed of:
            * preamble:
                - packages: list of packages.
                - preamble_nopkg:
            * content: the content of the document with
            the `\\begin{document}` and `\\end{document}`.
        :param lines:
        :return:
        """
        if lines is None:
            return
        first_line_content = 1
        for first_line_content, l in enumerate(lines):
            if '\\begin{document}' in l:
                break
        self.first_line_content = first_line_content

        preamble = lines[:first_line_content]
        self.contents = lines[first_line_content:]
        self.packages = make_package_list(preamble)
        # Was really supposed to be indented once more?
        self.preamble_nopkg = [l for l in preamble if '\\usepackage' not in l]

    @staticmethod
    def from_file(filename):
        f = open(filename, 'r')
        lines = [line.replace('\n', '').strip() for line in f]
        return LaTeX(lines)

    def reconstruct_pkg(self):
        document_class_line = 0
        for document_class_line, l in enumerate(self.preamble_nopkg):
            if l.startswith('\\documentclass'):
                break
        prefix = self.preamble_nopkg[:document_class_line + 1]
        suffix = self.preamble_nopkg[document_class_line + 1:]

        pkglist = []
        for pkg, opt in self.packages:
            pkglist.append("\\usepackage[%s]{%s}" % (','.join(opt), pkg))

        return '\n'.join(prefix) + '\n' * 2 + '\n'.join(pkglist) + '\n' * 2 + '\n'.join(suffix)

    def reconstruct_doc(self):
        return (self.reconstruct_pkg() + '\n' + '\n'.join(self.contents)).replace('\n\n\n', '\n')

    def merge(self, other):
        out = LaTeX()
        # Choose doc class
        doc_class = self.preamble_nopkg[0]
        # TODO Sha: why do we take the preamble nopkg from other?
        # TODO Sha: This method creates a replication of the documentclass in the test.
        out.preamble_nopkg = [doc_class] + other.preamble_nopkg[1:]

        # Slicing removes begin/end doc
        merged_contents = self.contents[1:-1] + other.contents[1:-1]

        out.packages = merge_packages(self.packages, other.packages)

        out.contents = ['\\begin{document}'] + merged_contents + ['\\end{document}']
        return out

    def __add__(self, other):
        return self.merge(other)

    def repr_pkg(self):
        return [
            '\usepackage[{}]{{{}}}'.format(', '.join(opts), pkg)
            if opts != []
            else '\usepackage{{{}}}'.format(pkg)
            for pkg, opts in self.packages
        ]

    @property
    def preamble(self):
        return self.preamble_nopkg + self.repr_pkg()

    def __repr__(self):
        return '\n'.join(self.preamble + self.contents)


def merge(*files):
    """
    Merges all the files to a single LaTeX object.
    :param files:
    :return:
    """
    if len(files) < 2:
        raise ValueError('More than two files are needed.')

    rv = LaTeX.from_file(files[0])
    for file_name in files[1:]:
        rv = rv + LaTeX.from_file(file_name)
    return rv
