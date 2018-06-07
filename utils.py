def print_file(f):
    print("'''")
    with open(f) as f_real_i_mean_it:
        print(f_real_i_mean_it.read(), end="'''\n")
