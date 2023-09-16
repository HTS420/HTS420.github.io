import pandas as pd
import sys

def pr_report(file_name):

    # 從MacOS介面抓下來的資料，固定第11行是header （zero indexing）
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
    #
    # for i in range(len(status_filter)):
    #     PR_Status_filter = df['PR Status'] == status_filter[i]
    #     df = df[PR_Status_filter]

    # convert PR Amount to int

    df['PR Amount'] = df['PR Amount'].apply(lambda x: float(x.split()[0].replace(',', ''))) # 先去掉千號符，才能轉float
    df['PR Amount'] = df['PR Amount'].astype(float)


    # save the processed file
    df.to_csv('processed_' + file_name, sep=',', index=False, encoding='utf-8')

    result = df['PR Amount'].sum()

    print(df)
    print(result)
    # 等等來用excel驗算

def main():
    """
    """
    # Get command line arguments
    args = sys.argv[1:]
    pr_report(args[0])



if __name__ == '__main__':
    main()