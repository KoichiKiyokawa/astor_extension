import sys

ouput_file = sys.argv[1]
with open(ouput_file, 'r') as f:
    output_str = f.read()

    patch_start_idx = output_str.find("diffpatch=")
    patch_end_idx = output_str.find("diffpatchoriginal=")
    patch = output_str[patch_start_idx:patch_end_idx+1]

    total_time_start_idx = output_str.find("TOTAL_TIME=")
    total_time_end_idx = output_str.find("NR_GENERATIONS")
    total_time = output_str[total_time_start_idx:total_time_end_idx]

    generation_start_idx = output_str.find("generation=")
    generation_end_idx = output_str.find("ingredientScope=")
    generation = output_str[generation_start_idx:generation_end_idx]

    print("diffpatch: {}\ntotal_time: {}\ngeneration:{}\n".format(
        patch, total_time, generation))
