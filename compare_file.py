# coding = utf-8

'''
比较两个文件（按二进制内容对比），并输出比较结果信息.
'''

import os


def compare_file_content(filename1, filename2):
    ''' 对比两个文件的内容.
    '''
    if not os.path.exists(filename1) or not os.path.exists(filename2):
        print('[Error] one of the file doesnt exists\n')
        return

    file_len_1 = os.path.getsize(filename1)
    file_len_2 = os.path.getsize(filename2)

    file_len = min(file_len_1, file_len_2)
    same_cnt = 0

    # 打印信息.
    print('=============================\n')
    print('file {} : {} bytes'.format(filename1, file_len_1))
    print('file {} : {} bytes'.format(filename2, file_len_2))
    print('compare {} bytes'.format(file_len))
    print('comparing ...')

    total_len = file_len
    with open(filename1, 'rb') as file1:
        with open(filename2, 'rb') as file2:
            while total_len > 0:
                cmp_len = min(file_len, 64 * 1024)
                data1 = file1.read(cmp_len)
                data2 = file2.read(cmp_len)
                for i in range(cmp_len):
                    if data1[i] == data2[i]:
                        same_cnt += 1
                total_len -= cmp_len
    
    print('\r===========================')
    print('same data : {} bytes'.format(same_cnt))
    print('diff data : {} bytes'.format(file_len - same_cnt))


if __name__ == '__main__':
    filename_1 = "c:/data/gpssim.bin"
    filename_2 = "c:/data/test.bin"
    compare_file_content(filename_1, filename_2)
