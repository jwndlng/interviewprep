
import "hash"

rule simple_hash_rule {
    meta:
        description = "This is a simple hash rule using the hash module"
    
    condition:
        hash.sha256(0, filesize) == "7e66a8ef5ed6dd76124986e2a8be03e8b33809d4770589c17266ef848bf10a17"
}