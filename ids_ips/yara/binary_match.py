
import yara, pathlib, binascii

# filepaths
base_dir = pathlib.Path(__file__).parent.absolute()
rule_filepath = base_dir.joinpath('rules', 'binary_match.yar').as_posix()
sample_filepath = base_dir.joinpath('sample.txt').as_posix()

bin_out = open(base_dir.joinpath('sample_bin.txt'), "w")
with open(sample_filepath, "rb") as fp:
    bin_out.write(binascii.hexlify(fp.read()).decode("utf-8"))
    bin_out.close()

# compile yara rule
rules = yara.compile(filepath=rule_filepath)

# match against file
matches = rules.match(base_dir.joinpath('sample.txt').as_posix())

# print output
main = matches.get('main', [])
if len(main) > 0:
    print(f"Matched findings: {len(main[0].get('strings', []))}")

# Output will be 44
# if you double check the "sample_bin.txt" file and search for "6169642063", you will find 44 occurrences!