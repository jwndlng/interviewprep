
/*
    This is a yara rule test
*/

rule test
{
    strings:
        $identifier = "Lorem"

    condition:
        $identifier
}