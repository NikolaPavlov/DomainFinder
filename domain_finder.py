from whois import whois


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


input_file = 'input.txt'


def domain_names_loader(filename):
    with open(filename, 'r'):
        # lines = [line.rstrip('\n') for line in open(filename)]
        lines = [line.strip() for line in open(filename) if line.strip()]
        return lines


def domain_names_loader_unmarked(lines):
    '''
    remove domains which started with # + -
    they are marked in the input.txt for reference
    '''
    stripped_lines = []
    for line in lines:
        if line[0] == '#':
            pass
        elif line[0] == '+':
            pass
        elif line[0] == '-':
            pass
        else:
            stripped_lines.append(line)
    return stripped_lines


def find_domain_registrar(domain_name):
    try:
        return whois(domain)['registrar']
    except:
        return bcolors.OKGREEN + 'Available!' + bcolors.ENDC


if __name__ == '__main__':
    input_domains = domain_names_loader(input_file)
    domains = domain_names_loader_unmarked(input_domains)

    for domain in domains:
        print(domain + ' ---> ' + find_domain_registrar(domain))
