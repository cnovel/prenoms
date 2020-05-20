# INSEE Prénoms header
# sexe;preusuel;annais;nombre
# 1;A;1980;3

import os.path
import operator
import argparse

C_1900 = 0
C_1911 = 1
C_1921 = 2
C_1931 = 3
C_1941 = 4
C_1951 = 5
C_1961 = 6
C_1971 = 7
C_1981 = 8
C_1991 = 9
C_2001 = 10
C_2011 = 11


def get_constant(year: int):
    if year < 1911:
        return C_1900
    if year < 1921:
        return C_1911
    if year < 1931:
        return C_1921
    if year < 1941:
        return C_1931
    if year < 1951:
        return C_1941
    if year < 1961:
        return C_1951
    if year < 1971:
        return C_1961
    if year < 1981:
        return C_1971
    if year < 1991:
        return C_1981
    if year < 2001:
        return C_1991
    if year < 2011:
        return C_2001
    return C_2011


def year_to_string(i: int):
    if i == C_1900:
        return '1900'
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
    if i == C_2001:
        return '2001'
    return '2011'


def gender_to_string(i: int):
    if i == 0:
        return 'm'
    return 'f'


def increment_dict(d: dict, key, increment):
    if key in d.keys():
        d[key] += increment
    else:
        d[key] = increment


def parse_insee(insee_file, output_folder):
    distribs = [{C_1900: {}, C_1911: {}, C_1921: {}, C_1931: {}, C_1941: {}, C_1951: {},
                 C_1961: {}, C_1971: {}, C_1981: {}, C_1991: {}, C_2001: {}, C_2011: {}, 'all': {}},
                {C_1900: {}, C_1911: {}, C_1921: {}, C_1931: {}, C_1941: {}, C_1951: {},
                 C_1961: {}, C_1971: {}, C_1981: {}, C_1991: {}, C_2001: {}, C_2011: {}, 'all': {}}
                ]
    max_ids = [{C_1900: [],  C_1911: [], C_1921: [], C_1931: [], C_1941: [], C_1951: [],
                C_1961: [], C_1971: [], C_1981: [], C_1991: [], C_2001: [], C_2011: [], 'all': {}},
               {C_1900: [], C_1911: [], C_1921: [], C_1931: [], C_1941: [], C_1951: [],
                C_1961: [], C_1971: [], C_1981: [], C_1991: [], C_2001: [], C_2011: [], 'all': {}}
               ]
    with open(insee_file, mode='r', encoding='utf-8') as f:
        first_line = True
        for line in f:
            if first_line:
                first_line = False
                continue
            line = line.strip()
            infos = line.split(';')
            if not infos or infos[2] == 'XXXX':
                continue
            if infos[1] == "_PRENOMS_RARES":
                continue
            gender = int(infos[0]) - 1
            name = infos[1].title()
            year = int(infos[2])
            count = int(infos[3])
            increment_dict(distribs[gender][get_constant(year)], name, count)
            increment_dict(distribs[gender]['all'], name, count)

    for gender in [0, 1]:
        genred_distribs = distribs[gender]
        for k in genred_distribs.keys():
            to_list = sorted(genred_distribs[k].items(), key=operator.itemgetter(1), reverse=True)
            genred_distribs[k] = to_list
            if k != 'all':
                genred_distribs[k] = [e for e in genred_distribs[k] if e[1] > 10]

            max_id_common = 0
            max_id_uncommon = 0
            max_id_rare = 0
            max_id = len(genred_distribs[k])
            for i in range(0, len(genred_distribs[k])):
                c = genred_distribs[k][i][1]  # Name occurence in the distrib
                if c < 500 and max_id_common == 0:
                    max_id_common = i
                if c < 100 and max_id_uncommon == 0:
                    max_id_uncommon = i
                if c < 50 and max_id_rare == 0:
                    max_id_rare = i
                    break
            max_ids[gender][k] = (max_id_common, max_id_uncommon, max_id_rare, max_id)

    for gender in [0, 1]:
        for i in range(C_1900, C_2011 + 1):
            with open(os.path.join(output_folder,
                                   'dist.prenoms.{}.{}.txt'.format(gender_to_string(gender),
                                                                   year_to_string(i))),
                      mode='w', encoding='utf-8') as f:
                t = max_ids[gender][i]
                f.write('{} {} {} {}\n'.format(t[0], t[1], t[2], t[3]))
                for name in distribs[gender][i]:
                    f.write(name[0] + ',')
        with open(os.path.join(output_folder,
                               'dist.prenoms.{}.all.txt'.format(gender_to_string(gender))),
                  mode='w', encoding='utf-8') as f:
            t = max_ids[gender]['all']
            f.write('{} {} {} {}\n'.format(t[0], t[1], t[2], t[3]))
            for name in distribs[gender]['all']:
                f.write(name[0] + ',')


def main():
    parser = argparse.ArgumentParser(description='Parse INSEE Prenoms file')
    parser.add_argument('-i', '--input', dest='insee_file',
                        help='Input Insee file')
    parser.add_argument('-o', '--output', dest='output_folder',
                        help='Output folder for files')
    args = parser.parse_args()
    parse_insee(args.insee_file, args.output_folder)


if __name__ == '__main__':
    main()
