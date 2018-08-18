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
        lines = [line.rstrip('\n') for line in open(filename)]
        return lines


def find_domain_registrar(domain_name):
    try:
        return whois(domain)['registrar']
    except:
        return bcolors.OKGREEN + 'Available!'


if __name__ == '__main__':
    input_domains = domain_names_loader(input_file)

    for domain in input_domains:
        print(domain + ' ---> ' + find_domain_registrar(domain))
