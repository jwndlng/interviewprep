
/*
    This is a yara rule test
*/

rule test
{
    strings:
        $id_hit = "Lorem"
        $id_not = "trust"

    condition:
        $id_hit and not $id_not
}