import sqlite3 as sql3

def print_first_n_entries(cursor, n):
    """
    :param cursor: points to a Cursor object that points to the target table
    :type cursor: Cursor
    :param n: Number of entries to print from a table.
    :type n: int
    
    Prints the first n entries in the mpa_data table

    :returns:
    :rtype: None
    """
    cursor.execute("SELECT * FROM mpa_data LIMIT ?", (n,))
    results = cursor.fetchall()

    result_num = 1
    for result in results:
        print("=" * 50)
        print(f"Result: {result_num}")
        print("-" * 50)
        print(f"DDInterID_A: {result[0]}")
        print(f"Drug_A: {result[1]}")
        print(f"DDInterID_B: {result[2]}")
        print(f"Drug_B: {result[3]}")
        print(f"Level: {result[4]}")

        result_num += 1


def print_interactions(cursor, drug_a, drug_b):
    """
    :param cursor: points to a Cursor object that points to the target table
    :type cursor: Cursor
    :param drug_a: Name of the first drug in the interaction.
    :type drug_a: String
    :param drug_b: Name of the second drug in the interaction.
    :type drug_b: String

    Prints the interaction level between drug_a and drug_b.

    :returns:
    :rtype: None
    """


if __name__ == "__main__":
    # Connect to the database
    conn = sql3.connect('mpa-data.db')

    # Make cursor
    cursor = conn.cursor()

    # Print first num_entries from mpa_data table in database
    num_entries = 5
    print_first_n_entries(cursor, num_entries)

    # Print interaction level between two drugs
    drugA = "Morphine"
    drugB = "Fentanyl"
    #print_interactions(cursor, drugA, drugB)

    # Close the connection
    conn.close()
