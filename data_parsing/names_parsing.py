# INSEE Names format header is the following, separated by tabs
# NOM _1891_1900 _1901_1910 _1911_1920 _1921_1930 _1931_1940 _1941_1950 _1951_1960 _1961_1970
# _1971_1980 _1981_1990 _1991_2000

import os.path
import argparse

C_1891 = 0
C_1901 = 1
C_1911 = 2
C_1921 = 3
C_1931 = 4
C_1941 = 5
C_1951 = 6
C_1961 = 7
C_1971 = 8
C_1981 = 9
C_1991 = 10


def year_to_string(i: int):
    if i == C_1891:
        return '1891'
    if i == C_1901:
        return '1901'
    if i == C_1911:
        return '1911'
    if i == C_1921:
        return '1921'
    if i == C_1931:
        return '1931'
    if i == C_1941:
        return '1941'
    if i == C_1951:
        return '1951'
    if i == C_1961:
        return '1961'
    if i == C_1971:
        return '1971'
    if i == C_1981:
        return '1981'
    if i == C_1991:
        return '1991'


def parse_insee(insee_name_file: str, output_folder: str):
    distribs = {C_1891: [], C_1901: [], C_1911: [], C_1921: [], C_1931: [], C_1941: [], C_1951: [],
                C_1961: [], C_1971: [], C_1981: [], C_1991: [], 'all': []}
    max_ids = {C_1891: [], C_1901: [], C_1911: [], C_1921: [], C_1931: [], C_1941: [], C_1951: [],
               C_1961: [], C_1971: [], C_1981: [], C_1991: [], 'all': []}
    with open(insee_name_file, mode='r', encoding='utf-8') as f:
        first_line = True
        for line in f:
            if first_line:  # Skipping the header
                first_line = False
                continue
            line = line.strip()
            infos = line.split('\t')
            if not infos:
                continue
            if infos[0] == "AUTRES NOMS":
                continue
            name = infos[0].title()
            total_count = 0
            for i in range(C_1891, C_1991+1):
                count = int(infos[i+1])
                total_count += count
                if count < 10:
                    continue
                distribs[i].append((name, count))
            distribs['all'].append((name, total_count))

    for k in distribs.keys():
        distribs[k].sort(key=lambda tup: tup[1], reverse=True)
        max_id_common = 0
        max_id_uncommon = 0
        max_id_rare = 0
        max_id = len(distribs[k])
        for i in range(0, len(distribs[k])):
            c = distribs[k][i][1]  # Name occurence in the distrib
            if c < 500 and max_id_common == 0:
                max_id_common = i
            if c < 100 and max_id_uncommon == 0:
                max_id_uncommon = i
            if c < 50 and max_id_rare == 0:
                max_id_rare = i
                break
        max_ids[k] = (max_id_common, max_id_uncommon, max_id_rare, max_id)

    # Dump info
    for i in range(C_1891, C_1991 + 1):
        with open(os.path.join(output_folder, 'dist.noms.{}.txt'.format(year_to_string(i))),
                  mode='w', encoding='utf-8') as f:
            t = max_ids[i]
            f.write('{} {} {} {}\n'.format(t[0], t[1], t[2], t[3]))
            for name in distribs[i]:
                f.write(name[0] + ',')
    with open(os.path.join(output_folder, 'dist.noms.all.txt'),
              mode='w', encoding='utf-8') as f:
        t = max_ids['all']
        f.write('{} {} {} {}\n'.format(t[0], t[1], t[2], t[3]))
        for name in distribs['all']:
            f.write(name[0] + ',')


def main():
    parser = argparse.ArgumentParser(description='Parse INSEE Names file')
    parser.add_argument('-i', '--input', dest='insee_file',
                        help='Input Insee file')
    parser.add_argument('-o', '--output', dest='output_folder',
                        help='Output folder for files')
    args = parser.parse_args()
    parse_insee(args.insee_file, args.output_folder)


if __name__ == '__main__':
    main()
