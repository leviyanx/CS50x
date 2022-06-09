import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python path/to/csv-file path/to/text-file")
        return

    # to conveniently debug
    database_file_path = sys.argv[1]
    sequence_file_path = sys.argv[2]
    # database_file_path = "C:/Users/leviy/My Drive/1.Projects/20220503_CS50x/pset6/dna/databases/large.csv"
    # sequence_file_path = "C:/Users/leviy/My Drive/1.Projects/20220503_CS50x/pset6/dna/sequences/5.txt"

    # TODO: Read database file into a variable
    with open(database_file_path, "r") as csv_file:
        database_file = csv.DictReader(csv_file)
        
        database_data = list(database_file)
        # get column name (STR's name)
        # dict_from_csv =  
        # dict(list(database_file)[0])
        column_name = database_file.fieldnames 
        # list(dict_from_csv.keys())

    # TODO: Read DNA sequence file into a variable
    with open(sequence_file_path, "r") as text_file:
        sequence = text_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    match_result = []
    for str in column_name[1:]:
        match_result.append(longest_match(sequence, str))

    # TODO: Check database for matching profiles
    is_none_match = True
    for row in database_data:
        is_match = True
        # match the str one by one
        for i in range(len(match_result)):
            if int(row[column_name[i+1]]) != match_result[i]:
                is_match = False
                break
        
        # matched
        if is_match:
            is_none_match = False
            print(row["name"])

    # there is no anyone matched
    if is_none_match == True:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
