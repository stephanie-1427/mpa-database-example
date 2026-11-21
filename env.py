import sqlite3 as sql3

# Connect to the database
conn = sql3.connect('mpa-data.db')

def print_first_n_entries(n):
    """
    :param n: Number of entries to print from a table.
    :type n: int
    
    Prints the first n entries in the mpa_data table

    :returns:
    :rtype: None
    """

def print_interactions(drug_a, drug_b):
    """
    :param drug_a: Name of the first drug in the interaction.
    :type drug_a: String
    :param drug_b: Name of the second drug in the interaction.
    :type drug_b: String

    Prints the interaction level between drug_a and drug_b.

    :returns:
    :rtype: None
    """

if __name__ == "__main__":
    # Print first num_entries from mpa_data table in database
    num_entries = 5
    print_first_n_entries(num_entries)

    # Print interaction level between two drugs
    drugA = ""
    drugB = ""
    print_interactions(drugA, drugB)
