
import yara, pathlib

# We will use the hash of sample.txt
# » sha256sum sample.txt                                                                                                                                                      jwendling@jwendling
# 7e66a8ef5ed6dd76124986e2a8be03e8b33809d4770589c17266ef848bf10a17  sample.txt

# filepaths
base_dir = pathlib.Path(__file__).parent.absolute()
rule_filepath = base_dir.joinpath('rules', 'hash_match.yar').as_posix()
sample_filepath = base_dir.joinpath('sample.txt').as_posix()

# compile yara rule
rules = yara.compile(filepath=rule_filepath)

# match against file
matches = rules.match(base_dir.joinpath('sample.txt').as_posix())

# print output
main = matches.get('main', [])
if len(main) > 0:
    print(f"Matched findings: {len(main[0].get('strings', []))}")
