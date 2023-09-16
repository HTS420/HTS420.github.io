import pandas as pd
import sys

def pr_report(file_name):

    # The header is fixed at row 11 when downloading from Mac(zero indexing）
    df = pd.read_csv (file_name, header = 11)

    # Remove duplicates Form ID
    df = df.drop_duplicates(subset=['Form ID'])

    # remove PR6190 using Dustin's budget
    delete_row = df[df["Form ID"] == 6190].index
    df = df.drop(delete_row)


    # PR_Status = df['PR Status']
    # PR_Status = PR_Status.drop_duplicates()
    #
    # print(PR_Status)

    # status_filter = ['OptVPApproved', 'BuyerApproved', 'BuyerFinalCompleted', 'GroupGMAApproved', 'GroupVPApproved', 'Submitted', 'OptHeadApproved', 'CMHeadApproved', 'CMApproved', 'FICompleted']

    cc_filter = df['Cost Center'] == 'EPOMF115'
    df = df[cc_filter]

    df = df[df['PR Status'].str.contains('OptVPApproved|BuyerApproved|BuyerFinalCompleted|GroupGMAApproved|GroupVPApproved|Submitted|OptHeadApproved|CMHeadApproved|CMApproved|FICompleted')]

    # convert PR Amount to int

    df['PR Amount'] = df['PR Amount'].apply(lambda x: float(x.split()[0].replace(',', ''))) # remove dollar sign to transform into float
    df['PR Amount'] = df['PR Amount'].astype(float)


    # save the processed file
    df.to_csv('processed_' + file_name, sep=',', index=False, encoding='utf-8')

    result = df['PR Amount'].sum()

    print(df)
    print(result)

def main():
    """
    """
    # Get command line arguments
    args = sys.argv[1:]
    pr_report(args[0])



if __name__ == '__main__':
    main()
