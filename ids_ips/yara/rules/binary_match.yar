
/*
    This is a yara rule test
*/

rule binary
{
    strings:
        $match_a = { 61 69 64 20 63 }

    condition:
        $match_a
}