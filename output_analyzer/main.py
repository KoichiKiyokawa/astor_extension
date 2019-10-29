import sys

ouput_file = sys.argv[1]
with open(ouput_file, 'r') as f:
    output_str = f.read()

    bug_id = output_str[output_str.find(
        "-id ") + len("-id "): output_str.find(" -failing")]
    scope = output_str[output_str.find(
        "-scope ") + len("-scope "):output_str.find("-population")]

    output_status_start_idx = output_str.find("OUTPUT_STATUS=")
    output_status_end_idx = output_str.find("Patch stats:")
    output_status = output_str[output_status_start_idx: output_status_end_idx - 1]

    whole_time_start_idx = output_str.find("Time Total(s):")
    whole_time_end_idx = output_str.find("Node: ")
    whole_time = output_str[whole_time_start_idx:whole_time_end_idx]

    patch_start_idx = output_str.find("diffpatch=")
    patch_end_idx = output_str.find("diffpatchoriginal=")
    patch = output_str[patch_start_idx:patch_end_idx]

    total_time_start_idx = output_str.find("TOTAL_TIME=")
    total_time_end_idx = output_str.find("NR_GENERATIONS")
    total_time = output_str[total_time_start_idx:total_time_end_idx]

    generation_start_idx = output_str.find("generation=")
    generation_end_idx = output_str.find("ingredientScope=")
    generation = output_str[generation_start_idx:generation_end_idx]

    print("{}\n{}\n{}\n{}\n{}\n".format(
        output_status, whole_time, patch, total_time, generation))

    def get_first_str(line):
        if len(line) == 0:
            return ""
        elif len(line) >= 3:
            if line[:3] == "+++":
                return ""
        return line[0]

    first_strs = list(map(get_first_str, patch.split("\n")))
    add_del_stat = "add: {} del: {}".format(
        first_strs.count("+"), first_strs.count("-"))
    print(add_del_stat)

    stat = ""
    if output_status == "OUTPUT_STATUS=ERROR\n":
        stat = "error"
    elif output_status == "OUTPUT_STATUS=TIME_OUT\n":
        stat = "timeout"
    else:
        stat = whole_time[len("Time Total(s):"):-3]
    print("csv:\n{},{},{},{},{},{}".format(
        bug_id, scope, stat, total_time[len("TOTAL_TIME="):-1], add_del_stat, generation[len("generation= "):]))
