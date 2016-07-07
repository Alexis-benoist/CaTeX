# -*- coding: utf-8 -*-
# TODO Add cli
# TODO unit test
# TODO add continuous integration
# TODO add documentation
# TODO add setup.py for pip


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


class LaTeX:
    def __init__(self, filename):
        f = open(filename, 'r')
        self.lines = [line.replace('\n', '').strip() for line in f]

        first_line_content = 1
        for first_line_content, l in enumerate(self.lines):
            if '\\begin{document}' in l:
                break

        self.preamble = self.lines[:first_line_content - 1]
        self.contents = self.lines[first_line_content:]
        self.packages = []

        for l in self.preamble:
            if '\\usepackage' not in l:
                continue

            pkg_start = l.index('{') + 1
            pkg_end = l.index('}')
            pkg = l[pkg_start:pkg_end]

            if ',' in pkg:
                for pkgl in pkg.split(','):
                    # Not possible that a pkg has options in that case?
                    self.packages.append([pkgl.strip(), []])
                continue

            self.packages.append([pkg, parse_options(l)])
            self.packages = sort_and_deduplicate(self.packages)

        # Was really supposed to be indented once more?
        self.preamble_nopkg = [l for l in self.preamble if '\\usepackage' not in l]

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

    def merge(self, f2):
        # Choose doc class
        doc_class = self.preamble_nopkg[0]
        f2.preamble_nopkg = f2.preamble_nopkg[1:]

        # Remove begin/end doc
        self.contents = self.contents[1:-1]
        f2.contents = f2.contents[1:-1]

        # Merge contents
        self.contents = self.contents + f2.contents

        # Merge packages
        newpackages = []
        pkgl = [pkg for pkg, opt in self.packages]
        for pkg, opt in f2.packages:
            if pkg in pkgl:
                pkgi = pkgl.index(pkg)
                newpackages.append([pkg, sort_and_deduplicate(self.packages[pkgi][1] + opt)])
            else:
                newpackages.append([pkg, list(set(opt))])
        self.packages = newpackages[:]

        self.preamble_nopkg = [doc_class] + self.preamble_nopkg
        self.contents = ['\\begin{document}'] + self.contents + ['\\end{document}']

    def __add__(self, other):
        return self.merge(other)
