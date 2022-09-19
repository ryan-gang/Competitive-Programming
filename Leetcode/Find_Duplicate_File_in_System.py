from collections import defaultdict
from typing import List
import hashlib


class Solution:
    # Runtime: 248 ms, faster than 11.52% of Python3 online submissions.
    # Memory Usage: 23.9 MB, less than 67.80% of Python3 online submissions.
    # T : O(N), S : O(N)
    def findDuplicateNaive(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            dir_path, *files = path.split(" ")
            for file in files:
                file_name, file_contents = file[:-1].split("(")
                d[file_contents].append(dir_path + "/" + file_name)

        return [d[k] for k in d if len(d[k]) > 1]

    """The previous code, used the entire file content as the dictionary key. But that is
    terribly inefficient. So, we are encoding the contents using md5 which converts the entire
    file content into a 128 bit hash value. This reduces space usage, for some extra compute
    power. We spend more compute to run the md5 encodings.

    library -> hashlib.
    MD5. Ref : https://datagy.io/python-sha256/
    encode() : Converts the string into bytes to be acceptable by hash function.
    digest() : Returns the encoded data in byte format.
    hexdigest() : Returns the encoded data in hexadecimal format.

    SHA256. Ref : https://datagy.io/python-sha256/
    The sha256 constructor takes a byte-like
    input, returning a hashed value.The function has a number of associated with hashing
    values, which are especially useful given that normal strings can't easily be processed.
    encode() : Convert a string to bytes, meaning that the string can be passed into the
    sha256 function.
    hexdigest() : Convert our data into hexadecimal format.
    """
    # Runtime: 299 ms, faster than 5.93% of Python3 online submissions.
    # Memory Usage: 26.5 MB, less than 5.25% of Python3 online submissions.
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            dir_path, *files = path.split(" ")
            for file in files:
                file_name, file_contents = file[:-1].split("(")
                encoded_file_contents = hashlib.md5(file_contents.encode()).hexdigest()
                d[encoded_file_contents].append(dir_path + "/" + file_name)

        return [d[k] for k in d if len(d[k]) > 1]

    def check_contents_files(string1, string2):
        if len(string1) != len(string2):
            return False
        i = j = 0
        while i < len(string1):
            if string1[i] != string2[j]:
                return False
            i += 1
            j += 1
        return True


sol = Solution()
assert sol.findDuplicate(
    paths=[
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
        "root 4.txt(efgh)",
    ]
) == [["root/a/1.txt", "root/c/3.txt"], ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"]]

###################################################################################################
"""
Follow up questions

    Imagine you are given a real file system, how will you search files? DFS or BFS?
    If the file content is very large (GB level), how will you modify your solution?
    If you can only read the file by 1kb each time, how will you modify your solution?
    What is the time complexity of your modified solution? What is the most time-consuming part and
    memory-consuming part of it? How to optimize?
    How to make sure the duplicated files you find are not false positive?
"""

"""
BFS can be used for great concurrency. Also, seek time would be greatly reduced as the files are
co-located. Where as DFS would be requiring a lock on root node, if you are simultaneous
processing the contents.

If the files are too large, its better to Navigate first to get a list of file paths and then
process the hash-map.

Check the sizes of the files, if they match we need further processing.
Maintain a checksum for the similar sizes, hash functions like sha256(hashes hardly collide) can be
used to calculate checksums.

If we can read only, 1Kb at a time, we can still use checksum for the blocks and calculate till the
point they differ. May be read 0.5 kb from file 1 and 0.5 kb from file2 to check if they differ.

Time Complexty:
For navigating, the files O(n), where n is the total number of files. For, calculating the
checksums in case of similar sizes, we could approximate this as O( c + xb), where b is the
number of blocks required to read till the files being compared differ, x is the constant for
per-block overhead, and c is the constant for initialization and finalization. Further O(n) time
is required to loop over the hashmap(key = f(size, checksum till they branch)) and return the
once having more than 1 file path.

Should consider to read the whole file content byte to byte.
"""

"""
BFS vs DFS

BFS explores neighbors first. This means that files which are located close to each other are
also accessed one after another. This is great for space locality and that's why BFS is expected
to be faster. Also, BFS is easier to parallelize (more fine-grained locking). DFS will require a
lock on the root node.

For very large files we should do the following comparisons in this order:
Compare sizes, if not equal, then files are different and stop here!
Hash them with a fast algorithm e.g. MD5 or use SHA256 (no collisions found yet),
if not equal then stop here!
Compare byte by byte to avoid false positives due to collisions.


Complexity
Runtime - Worst case (which is very unlikely to happen): O(N^2 * L) where L is the size of the
maximum bytes that need to be compared
Space - Worst case: all files are hashed and inserted in the hashmap, so O(H^2*L), H is the
hash code size and L is the filename size
"""

"""
Imagine you are given a real file system, how will you search files? DFS or BFS?
DFS. In this case the directory path could be large. DFS can reuse the shared the parent directory
before leaving that directory.
But BFS cannot.

If the file content is very large (GB level), how will you modify your solution?
In this case, not realistic to match the whole string of the content. So we use file signatures to
judge if two files are identical. Signatures can include file size, as well as sampled contents on
the same positions. They could have different file names and time stamps though.
Hashmaps are necessary to store the previous scanned file info.
S = O(|keys| + |list(directory)|). The key and the directory strings are the main space consumption.

a. Sample to obtain the sliced indices in the strings stored in the RAM only once and used for all
the scanned files. Accessing the strings is on-the-fly. But transforming them to hashcode used to
look up in hashmap and storing the keys and the directories in the hashmap can be time consuming.
The directory string can be compressed to directory id. The keys are hard to compress.
b. Use fast hashing algorithm e.g. MD5 or use SHA256 (no collisions found yet). If no worry about
the collision, meaning the hashcode is 1-1. Thus in the hashmap, the storage consumption on key
string can be replaced by key_hashcode, space usage compressed.

If you can only read the file by 1kb each time, how will you modify your solution?
That is the file cannot fit the whole ram. Use a buffer to read controlled by a loop; read until not
 needed or to the end. The sampled slices are offset by the times the buffer is called.

What is the time complexity of your modified solution?
What is the most time-consuming part and memory consuming part of it? How to optimize?
T = O(|num_files||sample||directory_depth|) + O(|hashmap.keys()|)

How to make sure the duplicated files you find are not false positive?
Add a round of final check which checks the whole string of the content.
T = O(|num_output_list||max_list_size||file_size|).
"""
