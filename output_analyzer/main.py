import sys

ouput_file = sys.argv[1]
with open(ouput_file, 'r') as f:
    output_str = f.read()

    patch_start_idx = output_str.find("diffpatch=")
    patch_end_idx = output_str.find("diffpatchoriginal=")
    patch = output_str[patch_start_idx:patch_end_idx]

    total_time_start_idx = output_str.find("TOTAL_TIME=")
    total_time_end_idx = output_str.find("NR_GENERATIONS")
    total_time = output_str[total_time_start_idx:total_time_end_idx]

    generation_start_idx = output_str.find("generation=")
    generation_end_idx = output_str.find("ingredientScope=")
    generation = output_str[generation_start_idx:generation_end_idx]

    print("{}\n{}\n{}\n".format(
        patch, total_time, generation))

    def get_first_str(line):
        if len(line) == 0:
            return ""
        elif len(line) >= 3:
            if line[:3] == "+++":
                return ""
        return line[0]

    first_strs = list(map(get_first_str, patch.split("\n")))
    print("add: {}, del: {}".format(first_strs.count("+"), first_strs.count("-")))
