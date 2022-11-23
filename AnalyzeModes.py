def quietAtoms(climax_file, atoms, output_file='output.aclimax', set_to_one=False):
    """Sets the Neutron cross-section of the atoms passed to zero

    Args:
        climax_file (str): name of the (o)aclimax file to be manipulated
        atoms ([list<int>, int]): atom numbers whose cross section will be set to zero. If only one atom is provided, all except that atom are quieted.
        output_file(str, optional): name of the output file. ouput.aclimax is default
    """
    if isinstance(atoms, int):
        atoms = [atoms]

    in_file = open(climax_file, 'r')
    lines = in_file.readlines()
    in_file.close()

    new_lines = []
    for line in lines: 
        parts = line.split()
        if len(parts) >= 8:
            if len(atoms) > 1:
                if int(parts[0]) in atoms:
                    for i in range(7, len(parts)):
                        line = line.replace(parts[i], '0.000000')
            else:
                if int(parts[0]) not in atoms:
                    for i in range(7, len(parts)):
                        line = line.replace(parts[i], '0.000000')
                elif set_to_one:
                    for i in range(7, len(parts)):
                        line = line.replace(parts[i], '1.000000')
        new_lines.append(line)
    out_file = open(output_file, 'w')
    out_file.writelines(new_lines)
    out_file.close()

def quietAtoms(params):
    """Sets the Neutron cross-section of the atoms passed to zero

    Args:
        climax_file (str): name of the (o)aclimax file to be manipulated
        atoms ([list<int>, int]): atom numbers whose cross section will be set to zero. If only one atom is provided, all except that atom are quieted.
        output_file(str, optional): name of the output file. ouput.aclimax is default
    """
    climax_file = params[0]
    atoms = params[1]
    if len(params) > 2:
        output_file = params[2]
    else:
        output_file = 'ouput.aclimax'
    if len(params) > 3:
        set_to_one = params[3]
    else:
        set_to_one = False
    if isinstance(atoms, int):
        atoms = [atoms]

    in_file = open(climax_file, 'r')
    lines = in_file.readlines()
    in_file.close()

    new_lines = []
    for line in lines: 
        parts = line.split()
        if len(parts) >= 8:
            if len(atoms) > 1:
                if int(parts[0]) in atoms:
                    for i in range(7, len(parts)):
                        line = line.replace(parts[i], '0.000000')
            else:
                if int(parts[0]) not in atoms:
                    for i in range(7, len(parts)):
                        line = line.replace(parts[i], '0.000000')
                elif set_to_one:
                    for i in range(7, len(parts)):
                        line = line.replace(parts[i], '1.000000')
        new_lines.append(line)
    out_file = open(output_file, 'w')
    out_file.writelines(new_lines)
    out_file.close()

def runOcliamx(climax_file, output_file='output.csv'):
    """Runs oclimax on the given (o)aclimax file and writes the output to output_file

    Args:
        climax_file (str): the (o)aclimax file you want to run
        output_file (str, optional): The name of the output file. Defaults to 'output.csv'.
    """
    import os
    import glob
    os.system("oclimax run {}".format(climax_file))
    csv_files = glob.glob('*.csv')
    for file in csv_files:
        if 'vis' in file:
            os.rename(file, output_file)

def runOcliamx(climax_file, output_file='output.csv', param_file=None):
    """Runs oclimax on the given (o)aclimax file and writes the output to output_file

    Args:
        climax_file (str): the (o)aclimax file you want to run
        output_file (str, optional): The name of the output file. Defaults to 'output.csv'.
    """
    import os
    import glob
    if param_file:
        print("oclimax run {} {}".format(climax_file, param_file))
        os.system("oclimax run {} {}".format(climax_file, param_file))
    else:
        print("oclimax run {}".format(climax_file))
        os.system("oclimax run {}".format(climax_file))
    csv_files = glob.glob('*.csv')
    for file in csv_files:
        if 'vis' in file:
            os.rename(file, output_file)


def runOcliamx(params):
    """Runs oclimax on the given (o)aclimax file and writes the output to output_file

    Args:
        climax_file (str): the (o)aclimax file you want to run
        output_file (str, optional): The name of the output file. Defaults to 'output.csv'.
    """
    import os
    import glob
    climax_file = params[0]
    if len(params) > 1:
        output_file = params[1]
    else:
        output_file = 'output.csv'
    if len(params) > 2:
        param_file = params[2]
    else:
        param_file = None

    if param_file:
        print("oclimax run {} {}".format(climax_file, param_file))
        os.system("oclimax run {} {}".format(climax_file, param_file))
    else:
        print("oclimax run {}".format(climax_file))
        os.system("oclimax run {}".format(climax_file))
    os.rename(output_file.split('.')[0]+'_vis_inc_0K.csv', output_file)