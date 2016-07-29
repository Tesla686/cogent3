#!/usr/bin/env python

"""Properties of proteins are data from 'tables' about residues and their
atoms."""

__author__ = "Marcin Cieslik"
__copyright__ = "Copyright 2007-2016, The Cogent Project"
__credits__ = ["Marcin Cieslik"]
__license__ = "GPL"
__version__ = "3.0a1"
__maintainer__ = "Marcin Cieslik"
__email__ = "mpc4p@virginia.edu"
__status__ = "Production"

AA_PROPERTIES = {
    'ALA': (1.8, 0.0, 0.42, 0.00, 106.0, 'T', 'P', 'A', 'A', 'A', 'A', 9, 'A'),
    'ARG': (-4.5, 1.0, -1.37, -1.88, 248.0, 'C', 'P', 'E', 'K', 'K', 'K', 15, 'R'),
    'ASN': (-3.5, 0.0, -0.82, -1.03, 157.0, 'D', 'P', 'E', 'E', 'E', 'N', 16, 'N'),
    'ASP': (-3.5, -1.0, -1.05, -0.78, 163.0, 'C', 'P', 'E', 'E', 'E', 'D', 19, 'D'),
    # 1kp0.pdb
    'ASX': (-3.5, -0.5, -1.05, -0.78, 160.0, None, 'P', 'E', 'E', 'E', None, None, 'B'),
    'CYS': (2.5, 0.0, 1.34, -0.85, 135.0, 'T', 'H', 'L', 'L', 'C', 'C', 7, 'C'),
    'GLN': (-3.5, 0.0, -0.30, -1.73, 198.0, 'D', 'P', 'E', 'E', 'E', 'Q', 17, 'Q'),
    'GLU': (-3.5, -1.0, -0.87, -1.46, 194.0, 'C', 'P', 'E', 'E', 'E', 'E', 18, 'E'),
    'GLX': (-3.5, -0.5, -0.87, -1.46, 196.0, None, 'P', 'E', 'E', 'E', None, None, 'Z'),
    'GLY': (-0.4, 0.0, 0.00, 0.00, 84.0, 'T', 'P', 'A', 'A', 'G', 'G', 11, 'G'),
    'HIS': (-3.2, 0.0, 0.18, -0.95, 184.0, 'R', 'P', 'E', 'H', 'H', 'H', 10, 'H'),
    'ILE': (4.5, 0.0, 2.46, -0.76, 169.0, 'A', 'H', 'L', 'L', 'L', 'L', 1, 'I'),
    'LEU': (3.8, 0.0, 2.32, -0.71, 164.0, 'A', 'H', 'L', 'L', 'L', 'L', 3, 'L'),
    'LYS': (-3.9, 1.0, -1.35, -1.89, 205.0, 'C', 'P', 'E', 'K', 'K', 'K', 20, 'K'),
    'MET': (1.9, 0.0, 1.68, -1.46, 188.0, 'D', 'H', 'L', 'L', 'L', 'L', 5, 'M'),
    'MSE': (0.0, 0.0, 0.00, 0.00, 000.0, 'D', 'H', 'L', 'L', 'L', 'L', 5, 'M'),  # SeMet
    'PHE': (2.8, 0.0, 2.44, -0.62, 197.0, 'R', 'H', 'F', 'F', 'F', 'F', 2, 'F'),
    'PRO': (-1.6, 0.0, 0.98, -0.06, 136.0, 'D', 'P', 'A', 'P', 'P', 'P', 13, 'P'),
    # SeCys
    'SEC': (2.5, 0.0, 1.34, -0.85, 135.0, 'T', 'H', 'L', 'L', 'C', 'C', 7, 'U'),
    'SER': (-0.8, 0.0, -0.05, -1.11, 130.0, 'T', 'P', 'A', 'S', 'S', 'S', 14, 'S'),
    'THR': (-0.7, 0.0, 0.35, -1.08, 142.0, 'D', 'P', 'A', 'S', 'S', 'T', 12, 'T'),
    'TRP': (-0.9, 0.0, 3.07, -0.99, 227.0, 'R', 'H', 'F', 'F', 'F', 'W', 6, 'W'),
    'TYR': (-1.3, 0.0, 1.31, -1.13, 222.0, 'R', 'H', 'F', 'F', 'F', 'F', 8, 'Y'),
    'UNK': (0.0, 0.0, 0.00, 0.00, 000.0, None, None, None, None, None, None, None, 'X'),
    'VAL': (4.2, 0.0, 1.66, -0.43, 142.0, 'A', 'H', 'L', 'L', 'L', 'L', 4, 'V')
}

AA_NAMES_1 = [value_[-1] for value_ in AA_PROPERTIES.values()]
AA_NAMES_3 = [key_ for key_ in AA_PROPERTIES.keys()]
AA_NAMES_3to1 = dict([(key_, value_[-1])
                      for (key_, value_) in AA_PROPERTIES.items()])
AA_GRAVY = dict([(key_, value_[0])
                 for (key_, value_) in AA_PROPERTIES.items()])
AA_CHARGE = dict([(key_, value_[1])
                  for (key_, value_) in AA_PROPERTIES.items()])
AA_SOLVATATION = dict([(key_, value_[2])
                       for (key_, value_) in AA_PROPERTIES.items()])
AA_ENTROPY = dict([(key_, value_[3])
                   for (key_, value_) in AA_PROPERTIES.items()])
AA_ASA = dict([(key_, value_[4]) for (key_, value_) in AA_PROPERTIES.items()])
# (Aliphatic, aRomatic, Charged, Tiny, Diverse)
AA_5 = dict([(key_, value_[5]) for (key_, value_) in AA_PROPERTIES.items()])
# (Hydrphobic, hydroPhylic)
AA_2 = dict([(key_, value_[6]) for (key_, value_) in AA_PROPERTIES.items()])
AA_4MURPHY = dict([(key_, value_[7])
                   for (key_, value_) in AA_PROPERTIES.items()])
AA_8MURPHY = dict([(key_, value_[8])
                   for (key_, value_) in AA_PROPERTIES.items()])
AA_10MURPHY = dict([(key_, value_[9])
                    for (key_, value_) in AA_PROPERTIES.items()])
AA_15MURPHY = dict([(key_, value_[10])
                    for (key_, value_) in AA_PROPERTIES.items()])
AA_POLARITY = dict([(key_, value_[11])
                    for (key_, value_) in AA_PROPERTIES.items()])

# short alternative
AA_NAMES = AA_NAMES_3
AA_3to1 = AA_NAMES_3to1

AA_ATOMS = {
    'ILE': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG1', ' CG2', ' CD1', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB ', 'HG12', 'HG13', 'HG21', 'HG22', 'HG23', 'HD11', 'HD12', 'HD13', ' HXT'],
    'GLN': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD ', ' OE1', ' NE2', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HG2', ' HG3', 'HE21', 'HE22', ' HXT'],
    'GLX': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD ', ' XE1', ' XE2', ' HA ', ' H  ', ' HB1', ' HB2', ' HG1', ' HG2', ' HD '],
    'GLY': [' N  ', ' CA ', ' C  ', ' O  ', ' OXT', ' H  ', ' H2 ', ' HA2', ' HA3', ' HXT'],
    'MSE': [' N  ', ' CA ', ' C  ', ' O  ', ' OXT', ' CB ', ' CG ', 'SE  ', ' CE ', ' H  ', ' HN2', ' HA ', ' HXT', ' HB2', ' HB3', ' HG2', ' HG3', ' HE1', ' HE2', ' HE3'],
    'GLU': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD ', ' OE1', ' OE2', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HG2', ' HG3', ' HE2', ' HXT'],
    'CYS': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' SG ', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HG ', ' HXT'],
    'ASP': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' OD1', ' OD2', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HD2', ' HXT'],
    'SER': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' OG ', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HG ', ' HXT'],
    'PRO': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD ', ' OXT', ' H  ', ' HA ', ' HB2', ' HB3', ' HG2', ' HG3', ' HD2', ' HD3', ' HXT'],
    'ASX': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' XD1', ' XD2', ' HA ', ' H  ', ' HB1', ' HB2', ' HG '],
    'SEC': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' SEG', ' OD1', ' OD2', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HD2', ' HXT'],
    'ASN': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' OD1', ' ND2', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', 'HD21', 'HD22', ' HXT'],
    'VAL': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG1', ' CG2', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB ', 'HG11', 'HG12', 'HG13', 'HG21', 'HG22', 'HG23', ' HXT'],
    'THR': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' OG1', ' CG2', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB ', ' HG1', 'HG21', 'HG22', 'HG23', ' HXT'],
    'HIS': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' ND1', ' CD2', ' CE1', ' NE2', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HD1', ' HD2', ' HE1', ' HE2', ' HXT'],
    'UNK': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB1', ' HB2', ' HG1', ' HG2', ' HG3', ' HXT'],
    'PHE': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD1', ' CD2', ' CE1', ' CE2', ' CZ ', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HD1', ' HD2', ' HE1', ' HE2', ' HZ ', ' HXT'],
    'ALA': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB1', ' HB2', ' HB3', ' HXT'],
    'MET': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' SD ', ' CE ', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HG2', ' HG3', ' HE1', ' HE2', ' HE3', ' HXT'],
    'LEU': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD1', ' CD2', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HG ', 'HD11', 'HD12', 'HD13', 'HD21', 'HD22', 'HD23', ' HXT'],
    'ARG': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD ', ' NE ', ' CZ ', ' NH1', ' NH2', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HG2', ' HG3', ' HD2', ' HD3', ' HE ', 'HH11', 'HH12', 'HH21', 'HH22', ' HXT'],
    'TRP': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD1', ' CD2', ' NE1', ' CE2', ' CE3', ' CZ2', ' CZ3', ' CH2', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HD1', ' HE1', ' HE3', ' HZ2', ' HZ3', ' HH2', ' HXT'],
    'LYS': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD ', ' CE ', ' NZ ', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HG2', ' HG3', ' HD2', ' HD3', ' HE2', ' HE3', ' HZ1', ' HZ2', ' HZ3', ' HXT'],
    'TYR': [' N  ', ' CA ', ' C  ', ' O  ', ' CB ', ' CG ', ' CD1', ' CD2', ' CE1', ' CE2', ' CZ ', ' OH ', ' OXT', ' H  ', ' H2 ', ' HA ', ' HB2', ' HB3', ' HD1', ' HD2', ' HE1', ' HE2', ' HH ', ' HXT']}

# sort atoms in residue according to PDBv3 specification
AA_ATOM_BACKBONE_ORDER = {'N': 3, 'CA': 2, 'C': 1, 'O': 0}
AA_ATOM_REMOTE_ORDER = {'A': 0, 'B': 1, 'G': 2, 'D': 3, 'E': 4, 'Z': 5,
                        'H': 6, 'X': 7, '1': 8, '2': 9, 'N': 9, '3': 10}
# H1, H2, H3 and NH2 in PDV v2.3AA_

AA_ATOM_PROPERTIES = {
    ('ALA', ' C  '): [1.8],
    ('ALA', ' CA '): [1.8],
    ('ALA', ' CB '): [1.8],
    ('ALA', ' H  '): [0.0],
    ('ALA', ' H2 '): [0.0],
    ('ALA', ' HA '): [0.0],
    ('ALA', ' HB1'): [0.0],
    ('ALA', ' HB2'): [0.0],
    ('ALA', ' HB3'): [0.0],
    ('ALA', ' HXT'): [0.0],
    ('ALA', ' N  '): [1.65],
    ('ALA', ' O  '): [1.60],
    ('ALA', ' OXT'): [1.60],
    ('ARG', ' C  '): [1.8],
    ('ARG', ' CA '): [1.8],
    ('ARG', ' CB '): [1.8],
    ('ARG', ' CD '): [1.8],
    ('ARG', ' CG '): [1.8],
    ('ARG', ' CZ '): [1.8],
    ('ARG', ' H  '): [0.0],
    ('ARG', ' H2 '): [0.0],
    ('ARG', ' HA '): [0.0],
    ('ARG', ' HB2'): [0.0],
    ('ARG', ' HB3'): [0.0],
    ('ARG', ' HD2'): [0.0],
    ('ARG', ' HD3'): [0.0],
    ('ARG', ' HE '): [0.0],
    ('ARG', ' HG2'): [0.0],
    ('ARG', ' HG3'): [0.0],
    ('ARG', ' HXT'): [0.0],
    ('ARG', ' N  '): [1.65],
    ('ARG', ' NE '): [1.65],
    ('ARG', ' NH1'): [1.65],
    ('ARG', ' NH2'): [1.65],
    ('ARG', ' O  '): [1.60],
    ('ARG', ' OXT'): [1.60],
    ('ARG', 'HH11'): [0.0],
    ('ARG', 'HH12'): [0.0],
    ('ARG', 'HH21'): [0.0],
    ('ARG', 'HH22'): [0.0],
    ('ASN', ' C  '): [1.8],
    ('ASN', ' CA '): [1.8],
    ('ASN', ' CB '): [1.8],
    ('ASN', ' CG '): [1.8],
    ('ASN', ' H  '): [0.0],
    ('ASN', ' H2 '): [0.0],
    ('ASN', ' HA '): [0.0],
    ('ASN', ' HB2'): [0.0],
    ('ASN', ' HB3'): [0.0],
    ('ASN', ' HXT'): [0.0],
    ('ASN', ' N  '): [1.65],
    ('ASN', ' ND2'): [1.65],
    ('ASN', ' O  '): [1.60],
    ('ASN', ' OD1'): [1.60],
    ('ASN', ' OXT'): [1.60],
    ('ASN', 'HD21'): [0.0],
    ('ASN', 'HD22'): [0.0],
    ('ASP', ' C  '): [1.8],
    ('ASP', ' CA '): [1.8],
    ('ASP', ' CB '): [1.8],
    ('ASP', ' CG '): [1.8],
    ('ASP', ' H  '): [0.0],
    ('ASP', ' H2 '): [0.0],
    ('ASP', ' HA '): [0.0],
    ('ASP', ' HB2'): [0.0],
    ('ASP', ' HB3'): [0.0],
    ('ASP', ' HD2'): [0.0],
    ('ASP', ' HXT'): [0.0],
    ('ASP', ' N  '): [1.65],
    ('ASP', ' O  '): [1.60],
    ('ASP', ' OD1'): [1.60],
    ('ASP', ' OD2'): [1.60],
    ('ASP', ' OXT'): [1.60],
    ('ASX', ' C  '): [1.8],
    ('ASX', ' CA '): [1.8],
    ('ASX', ' CB '): [1.8],
    ('ASX', ' CG '): [1.8],
    ('ASX', ' H  '): [0.0],
    ('ASX', ' HA '): [0.0],
    ('ASX', ' HB1'): [0.0],
    ('ASX', ' HB2'): [0.0],
    ('ASX', ' HG '): [0.0],
    ('ASX', ' N  '): [1.65],
    ('ASX', ' O  '): [1.60],
    ('ASX', ' XD1'): [1.65],
    ('ASX', ' XD2'): [1.65],
    ('CYS', ' C  '): [1.8],
    ('CYS', ' CA '): [1.8],
    ('CYS', ' CB '): [1.8],
    ('CYS', ' H  '): [0.0],
    ('CYS', ' H2 '): [0.0],
    ('CYS', ' HA '): [0.0],
    ('CYS', ' HB2'): [0.0],
    ('CYS', ' HB3'): [0.0],
    ('CYS', ' HG '): [0.0],
    ('CYS', ' HXT'): [0.0],
    ('CYS', ' N  '): [1.65],
    ('CYS', ' O  '): [1.60],
    ('CYS', ' OXT'): [1.60],
    ('CYS', ' SG '): [1.850],
    ('GLN', ' C  '): [1.8],
    ('GLN', ' CA '): [1.8],
    ('GLN', ' CB '): [1.8],
    ('GLN', ' CD '): [1.8],
    ('GLN', ' CG '): [1.8],
    ('GLN', ' H  '): [0.0],
    ('GLN', ' H2 '): [0.0],
    ('GLN', ' HA '): [0.0],
    ('GLN', ' HB2'): [0.0],
    ('GLN', ' HB3'): [0.0],
    ('GLN', ' HG2'): [0.0],
    ('GLN', ' HG3'): [0.0],
    ('GLN', ' HXT'): [0.0],
    ('GLN', ' N  '): [1.65],
    ('GLN', ' NE2'): [1.65],
    ('GLN', ' O  '): [1.60],
    ('GLN', ' OE1'): [1.60],
    ('GLN', ' OXT'): [1.60],
    ('GLN', 'HE21'): [0.0],
    ('GLN', 'HE22'): [0.0],
    ('GLU', ' C  '): [1.8],
    ('GLU', ' CA '): [1.8],
    ('GLU', ' CB '): [1.8],
    ('GLU', ' CD '): [1.8],
    ('GLU', ' CG '): [1.8],
    ('GLU', ' H  '): [0.0],
    ('GLU', ' H2 '): [0.0],
    ('GLU', ' HA '): [0.0],
    ('GLU', ' HB2'): [0.0],
    ('GLU', ' HB3'): [0.0],
    ('GLU', ' HE2'): [0.0],
    ('GLU', ' HG2'): [0.0],
    ('GLU', ' HG3'): [0.0],
    ('GLU', ' HXT'): [0.0],
    ('GLU', ' N  '): [1.65],
    ('GLU', ' O  '): [1.60],
    ('GLU', ' OE1'): [1.60],
    ('GLU', ' OE2'): [1.60],
    ('GLU', ' OXT'): [1.60],
    ('GLX', ' C  '): [1.8],
    ('GLX', ' CA '): [1.8],
    ('GLX', ' CB '): [1.8],
    ('GLX', ' CD '): [1.8],
    ('GLX', ' CG '): [1.8],
    ('GLX', ' H  '): [0.0],
    ('GLX', ' HA '): [0.0],
    ('GLX', ' HB1'): [0.0],
    ('GLX', ' HB2'): [0.0],
    ('GLX', ' HD '): [0.0],
    ('GLX', ' HG1'): [0.0],
    ('GLX', ' HG2'): [0.0],
    ('GLX', ' N  '): [1.65],
    ('GLX', ' O  '): [1.60],
    ('GLX', ' XE1'): [1.65],
    ('GLX', ' XE2'): [1.65],
    ('GLY', ' C  '): [1.8],
    ('GLY', ' CA '): [1.8],
    ('GLY', ' H  '): [0.0],
    ('GLY', ' H2 '): [0.0],
    ('GLY', ' HA2'): [0.0],
    ('GLY', ' HA3'): [0.0],
    ('GLY', ' HXT'): [0.0],
    ('GLY', ' N  '): [1.65],
    ('GLY', ' O  '): [1.60],
    ('GLY', ' OXT'): [1.60],
    ('HIS', ' C  '): [1.8],
    ('HIS', ' CA '): [1.8],
    ('HIS', ' CB '): [1.8],
    ('HIS', ' CD2'): [1.8],
    ('HIS', ' CE1'): [1.8],
    ('HIS', ' CG '): [1.8],
    ('HIS', ' H  '): [0.0],
    ('HIS', ' H2 '): [0.0],
    ('HIS', ' HA '): [0.0],
    ('HIS', ' HB2'): [0.0],
    ('HIS', ' HB3'): [0.0],
    ('HIS', ' HD1'): [0.0],
    ('HIS', ' HD2'): [0.0],
    ('HIS', ' HE1'): [0.0],
    ('HIS', ' HE2'): [0.0],
    ('HIS', ' HXT'): [0.0],
    ('HIS', ' N  '): [1.65],
    ('HIS', ' ND1'): [1.65],
    ('HIS', ' NE2'): [1.65],
    ('HIS', ' O  '): [1.60],
    ('HIS', ' OXT'): [1.60],
    ('ILE', ' C  '): [1.8],
    ('ILE', ' CA '): [1.8],
    ('ILE', ' CB '): [1.8],
    ('ILE', ' CD1'): [1.8],
    ('ILE', ' CG1'): [1.8],
    ('ILE', ' CG2'): [1.8],
    ('ILE', ' H  '): [0.0],
    ('ILE', ' H2 '): [0.0],
    ('ILE', ' HA '): [0.0],
    ('ILE', ' HB '): [0.0],
    ('ILE', ' HXT'): [0.0],
    ('ILE', ' N  '): [1.65],
    ('ILE', ' O  '): [1.60],
    ('ILE', ' OXT'): [1.60],
    ('ILE', 'HD11'): [0.0],
    ('ILE', 'HD12'): [0.0],
    ('ILE', 'HD13'): [0.0],
    ('ILE', 'HG12'): [0.0],
    ('ILE', 'HG13'): [0.0],
    ('ILE', 'HG21'): [0.0],
    ('ILE', 'HG22'): [0.0],
    ('ILE', 'HG23'): [0.0],
    ('LEU', ' C  '): [1.8],
    ('LEU', ' CA '): [1.8],
    ('LEU', ' CB '): [1.8],
    ('LEU', ' CD1'): [1.8],
    ('LEU', ' CD2'): [1.8],
    ('LEU', ' CG '): [1.8],
    ('LEU', ' H  '): [0.0],
    ('LEU', ' H2 '): [0.0],
    ('LEU', ' HA '): [0.0],
    ('LEU', ' HB2'): [0.0],
    ('LEU', ' HB3'): [0.0],
    ('LEU', ' HG '): [0.0],
    ('LEU', ' HXT'): [0.0],
    ('LEU', ' N  '): [1.65],
    ('LEU', ' O  '): [1.60],
    ('LEU', ' OXT'): [1.60],
    ('LEU', 'HD11'): [0.0],
    ('LEU', 'HD12'): [0.0],
    ('LEU', 'HD13'): [0.0],
    ('LEU', 'HD21'): [0.0],
    ('LEU', 'HD22'): [0.0],
    ('LEU', 'HD23'): [0.0],
    ('LYS', ' C  '): [1.8],
    ('LYS', ' CA '): [1.8],
    ('LYS', ' CB '): [1.8],
    ('LYS', ' CD '): [1.8],
    ('LYS', ' CE '): [1.8],
    ('LYS', ' CG '): [1.8],
    ('LYS', ' H  '): [0.0],
    ('LYS', ' H2 '): [0.0],
    ('LYS', ' HA '): [0.0],
    ('LYS', ' HB2'): [0.0],
    ('LYS', ' HB3'): [0.0],
    ('LYS', ' HD2'): [0.0],
    ('LYS', ' HD3'): [0.0],
    ('LYS', ' HE2'): [0.0],
    ('LYS', ' HE3'): [0.0],
    ('LYS', ' HG2'): [0.0],
    ('LYS', ' HG3'): [0.0],
    ('LYS', ' HXT'): [0.0],
    ('LYS', ' HZ1'): [0.0],
    ('LYS', ' HZ2'): [0.0],
    ('LYS', ' HZ3'): [0.0],
    ('LYS', ' N  '): [1.65],
    ('LYS', ' NZ '): [1.65],
    ('LYS', ' O  '): [1.60],
    ('LYS', ' OXT'): [1.60],
    ('MET', ' C  '): [1.8],
    ('MET', ' CA '): [1.8],
    ('MET', ' CB '): [1.8],
    ('MET', ' CE '): [1.8],
    ('MET', ' CG '): [1.8],
    ('MET', ' H  '): [0.0],
    ('MET', ' H2 '): [0.0],
    ('MET', ' HA '): [0.0],
    ('MET', ' HB2'): [0.0],
    ('MET', ' HB3'): [0.0],
    ('MET', ' HE1'): [0.0],
    ('MET', ' HE2'): [0.0],
    ('MET', ' HE3'): [0.0],
    ('MET', ' HG2'): [0.0],
    ('MET', ' HG3'): [0.0],
    ('MET', ' HXT'): [0.0],
    ('MET', ' N  '): [1.65],
    ('MET', ' O  '): [1.60],
    ('MET', ' OXT'): [1.60],
    ('MET', ' SD '): [1.850],
    ('MSE', ' C  '): [1.8],
    ('MSE', ' CA '): [1.8],
    ('MSE', ' CB '): [1.8],
    ('MSE', ' CE '): [1.8],
    ('MSE', ' CG '): [1.8],
    ('MSE', ' H  '): [0.0],
    ('MSE', ' HA '): [0.0],
    ('MSE', ' HB2'): [0.0],
    ('MSE', ' HB3'): [0.0],
    ('MSE', ' HE1'): [0.0],
    ('MSE', ' HE2'): [0.0],
    ('MSE', ' HE3'): [0.0],
    ('MSE', ' HG2'): [0.0],
    ('MSE', ' HG3'): [0.0],
    ('MSE', ' HN2'): [0.0],
    ('MSE', ' HXT'): [0.0],
    ('MSE', ' N  '): [1.65],
    ('MSE', ' O  '): [1.60],
    ('MSE', ' OXT'): [1.60],
    ('MSE', 'SE  '): [1.90],
    ('PHE', ' C  '): [1.8],
    ('PHE', ' CA '): [1.8],
    ('PHE', ' CB '): [1.8],
    ('PHE', ' CD1'): [1.8],
    ('PHE', ' CD2'): [1.8],
    ('PHE', ' CE1'): [1.8],
    ('PHE', ' CE2'): [1.8],
    ('PHE', ' CG '): [1.8],
    ('PHE', ' CZ '): [1.8],
    ('PHE', ' H  '): [0.0],
    ('PHE', ' H2 '): [0.0],
    ('PHE', ' HA '): [0.0],
    ('PHE', ' HB2'): [0.0],
    ('PHE', ' HB3'): [0.0],
    ('PHE', ' HD1'): [0.0],
    ('PHE', ' HD2'): [0.0],
    ('PHE', ' HE1'): [0.0],
    ('PHE', ' HE2'): [0.0],
    ('PHE', ' HXT'): [0.0],
    ('PHE', ' HZ '): [0.0],
    ('PHE', ' N  '): [1.65],
    ('PHE', ' O  '): [1.60],
    ('PHE', ' OXT'): [1.60],
    ('PRO', ' C  '): [1.8],
    ('PRO', ' CA '): [1.8],
    ('PRO', ' CB '): [1.8],
    ('PRO', ' CD '): [1.8],
    ('PRO', ' CG '): [1.8],
    ('PRO', ' H  '): [0.0],
    ('PRO', ' HA '): [0.0],
    ('PRO', ' HB2'): [0.0],
    ('PRO', ' HB3'): [0.0],
    ('PRO', ' HD2'): [0.0],
    ('PRO', ' HD3'): [0.0],
    ('PRO', ' HG2'): [0.0],
    ('PRO', ' HG3'): [0.0],
    ('PRO', ' HXT'): [0.0],
    ('PRO', ' N  '): [1.65],
    ('PRO', ' O  '): [1.60],
    ('PRO', ' OXT'): [1.60],
    ('SEC', ' C  '): [1.8],
    ('SEC', ' CA '): [1.8],
    ('SEC', ' CB '): [1.8],
    ('SEC', ' H  '): [0.0],
    ('SEC', ' H2 '): [0.0],
    ('SEC', ' HA '): [0.0],
    ('SEC', ' HB2'): [0.0],
    ('SEC', ' HB3'): [0.0],
    ('SEC', ' HD2'): [0.0],
    ('SEC', ' HXT'): [0.0],
    ('SEC', ' N  '): [1.65],
    ('SEC', ' O  '): [1.60],
    ('SEC', ' OD1'): [1.60],
    ('SEC', ' OD2'): [1.60],
    ('SEC', ' OXT'): [1.60],
    ('SEC', ' SEG'): [1.85],
    ('SER', ' C  '): [1.8],
    ('SER', ' CA '): [1.8],
    ('SER', ' CB '): [1.8],
    ('SER', ' H  '): [0.0],
    ('SER', ' H2 '): [0.0],
    ('SER', ' HA '): [0.0],
    ('SER', ' HB2'): [0.0],
    ('SER', ' HB3'): [0.0],
    ('SER', ' HG '): [0.0],
    ('SER', ' HXT'): [0.0],
    ('SER', ' N  '): [1.65],
    ('SER', ' O  '): [1.60],
    ('SER', ' OG '): [1.60],
    ('SER', ' OXT'): [1.60],
    ('THR', ' C  '): [1.8],
    ('THR', ' CA '): [1.8],
    ('THR', ' CB '): [1.8],
    ('THR', ' CG2'): [1.8],
    ('THR', ' H  '): [0.0],
    ('THR', ' H2 '): [0.0],
    ('THR', ' HA '): [0.0],
    ('THR', ' HB '): [0.0],
    ('THR', ' HG1'): [0.0],
    ('THR', ' HXT'): [0.0],
    ('THR', ' N  '): [1.65],
    ('THR', ' O  '): [1.60],
    ('THR', ' OG1'): [1.60],
    ('THR', ' OXT'): [1.60],
    ('THR', 'HG21'): [0.0],
    ('THR', 'HG22'): [0.0],
    ('THR', 'HG23'): [0.0],
    ('TRP', ' C  '): [1.8],
    ('TRP', ' CA '): [1.8],
    ('TRP', ' CB '): [1.8],
    ('TRP', ' CD1'): [1.8],
    ('TRP', ' CD2'): [1.8],
    ('TRP', ' CE2'): [1.8],
    ('TRP', ' CE3'): [1.8],
    ('TRP', ' CG '): [1.8],
    ('TRP', ' CH2'): [1.8],
    ('TRP', ' CZ2'): [1.8],
    ('TRP', ' CZ3'): [1.8],
    ('TRP', ' H  '): [0.0],
    ('TRP', ' H2 '): [0.0],
    ('TRP', ' HA '): [0.0],
    ('TRP', ' HB2'): [0.0],
    ('TRP', ' HB3'): [0.0],
    ('TRP', ' HD1'): [0.0],
    ('TRP', ' HE1'): [0.0],
    ('TRP', ' HE3'): [0.0],
    ('TRP', ' HH2'): [0.0],
    ('TRP', ' HXT'): [0.0],
    ('TRP', ' HZ2'): [0.0],
    ('TRP', ' HZ3'): [0.0],
    ('TRP', ' N  '): [1.65],
    ('TRP', ' NE1'): [1.65],
    ('TRP', ' O  '): [1.60],
    ('TRP', ' OXT'): [1.60],
    ('TYR', ' C  '): [1.8],
    ('TYR', ' CA '): [1.8],
    ('TYR', ' CB '): [1.8],
    ('TYR', ' CD1'): [1.8],
    ('TYR', ' CD2'): [1.8],
    ('TYR', ' CE1'): [1.8],
    ('TYR', ' CE2'): [1.8],
    ('TYR', ' CG '): [1.8],
    ('TYR', ' CZ '): [1.8],
    ('TYR', ' H  '): [0.0],
    ('TYR', ' H2 '): [0.0],
    ('TYR', ' HA '): [0.0],
    ('TYR', ' HB2'): [0.0],
    ('TYR', ' HB3'): [0.0],
    ('TYR', ' HD1'): [0.0],
    ('TYR', ' HD2'): [0.0],
    ('TYR', ' HE1'): [0.0],
    ('TYR', ' HE2'): [0.0],
    ('TYR', ' HH '): [0.0],
    ('TYR', ' HXT'): [0.0],
    ('TYR', ' N  '): [1.65],
    ('TYR', ' O  '): [1.60],
    ('TYR', ' OH '): [1.60],
    ('TYR', ' OXT'): [1.60],
    ('UNK', ' C  '): [1.8],
    ('UNK', ' CA '): [1.8],
    ('UNK', ' CB '): [1.8],
    ('UNK', ' CG '): [1.8],
    ('UNK', ' H  '): [0.0],
    ('UNK', ' H2 '): [0.0],
    ('UNK', ' HA '): [0.0],
    ('UNK', ' HB1'): [0.0],
    ('UNK', ' HB2'): [0.0],
    ('UNK', ' HG1'): [0.0],
    ('UNK', ' HG2'): [0.0],
    ('UNK', ' HG3'): [0.0],
    ('UNK', ' HXT'): [0.0],
    ('UNK', ' N  '): [1.65],
    ('UNK', ' O  '): [1.60],
    ('UNK', ' OXT'): [1.60],
    ('VAL', ' C  '): [1.8],
    ('VAL', ' CA '): [1.8],
    ('VAL', ' CB '): [1.8],
    ('VAL', ' CG1'): [1.8],
    ('VAL', ' CG2'): [1.8],
    ('VAL', ' H  '): [0.0],
    ('VAL', ' H2 '): [0.0],
    ('VAL', ' HA '): [0.0],
    ('VAL', ' HB '): [0.0],
    ('VAL', ' HXT'): [0.0],
    ('VAL', ' N  '): [1.65],
    ('VAL', ' O  '): [1.60],
    ('VAL', ' OXT'): [1.60],
    ('VAL', 'HG11'): [0.0],
    ('VAL', 'HG12'): [0.0],
    ('VAL', 'HG13'): [0.0],
    ('VAL', 'HG21'): [0.0],
    ('VAL', 'HG22'): [0.0],
    ('VAL', 'HG23'): [0.0]}
# AREAIMOL_VDW_RADII

AREAIMOL_VDW_RADII = dict([(k, v[0]) for k, v in AA_ATOM_PROPERTIES.items()])
DEFAULT_AREAIMOL_VDW_RADIUS = 1.7
